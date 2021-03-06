from collections import namedtuple, OrderedDict
import itertools

import iso3166

from dataactcore.interfaces.db import GlobalDB
from dataactcore.models.fsrs import FSRSGrant, FSRSProcurement, FSRSSubcontract, FSRSSubgrant
from dataactcore.models.stagingModels import AwardFinancialAssistance, AwardProcurement
import logging


logger = logging.getLogger(__name__)


def _country_name(code):
    """Convert a country code to the country name; return None if invalid"""
    country = iso3166.countries.get(code, None)
    if country:
        return country.name


def _zipcode_guard(model, field_prefix, match_usa):
    """Get the zip code or not depending on country value"""
    is_usa = getattr(model, field_prefix + '_country') == 'USA'
    zipcode = getattr(model, field_prefix + '_zip')
    if (match_usa and is_usa) or (not match_usa and not is_usa):
        return zipcode


class CopyValues:
    """Copy a field value from one of our existing models"""
    # Order to check fields
    MODEL_TYPES = ('subcontract', 'subgrant', 'procurement', 'grant', 'award')

    def __init__(self, subcontract=None, subgrant=None, procurement=None, grant=None, award=None):
        self.procurement_field = procurement
        self.subcontract_field = subcontract
        self.grant_field = grant
        self.subgrant_field = subgrant
        self.award_field = award

    def __call__(self, models):
        for model_type in self.MODEL_TYPES:
            field_name = getattr(self, model_type + '_field')
            model = getattr(models, model_type)
            if model and field_name:
                return getattr(model, field_name)


def copy_subaward_field(field_name):
    return CopyValues(field_name, field_name)


def copy_prime_field(field_name):
    return CopyValues(procurement=field_name, grant=field_name)


class SubawardLogic:
    """Perform custom logic relating to the subaward (i.e. subcontract or
    subgrant). Instantiated with two functions: one for subcontracts, one for
    subawards"""
    def __init__(self, subcontract_fn, subgrant_fn):
        self.subcontract_fn = subcontract_fn
        self.subgrant_fn = subgrant_fn

    def __call__(self, models):
        if models.subcontract:
            return self.subcontract_fn(models.subcontract)
        elif models.subgrant:
            return self.subgrant_fn(models.subgrant)


# Collect the models associated with a single F CSV row
ModelRow = namedtuple(
    'ModelRow',
    ['award', 'procurement', 'subcontract', 'grant', 'subgrant', 'naics_desc'])
ModelRow.__new__.__defaults__ = (None, None, None, None, None)


# A collection of mappers (callables which convert a ModelRow into a string to
# be placed in a CSV cell), keyed by the CSV column name for that cell. Order
# matters as it defines the CSV column order
mappings = OrderedDict([
    ('SubAwardeeOrRecipientLegalEntityName', CopyValues('company_name', 'awardee_name')),
    ('SubAwardeeOrRecipientUniqueIdentifier', copy_subaward_field('duns')),
    ('SubAwardeeUltimateParentUniqueIdentifier', copy_subaward_field('parent_duns')),
    ('SubAwardeeUltimateParentLegalEntityName', CopyValues(subcontract='parent_company_name')),
    ('LegalEntityAddressLine1', CopyValues('company_address_street', 'awardee_address_street')),
    ('LegalEntityCityName', CopyValues('company_address_city', 'awardee_address_city')),
    ('LegalEntityStateCode', CopyValues('company_address_state', 'awardee_address_state')),
    ('LegalEntityStateName', CopyValues('company_address_state_name', 'awardee_address_state_name')),
    ('LegalEntityZIP+4', SubawardLogic(
        lambda subcontract: _zipcode_guard(subcontract, 'company_address', True),
        lambda subgrant: _zipcode_guard(subgrant, 'awardee_address', True)
    )),
    ('LegalEntityForeignPostalCode', SubawardLogic(
        lambda subcontract: _zipcode_guard(subcontract, 'company_address', False),
        lambda subgrant: _zipcode_guard(subgrant, 'awardee_address', False)
    )),
    ('LegalEntityCongressionalDistrict', CopyValues('company_address_district', 'awardee_address_district')),
    ('LegalEntityCountryCode', CopyValues('company_address_country', 'awardee_address_country')),
    ('LegalEntityCountryName', SubawardLogic(
        lambda subcontract: _country_name(subcontract.company_address_country),
        lambda subgrant: _country_name(subgrant.awardee_address_country)
    )),
    ('HighCompOfficer1FullName', copy_subaward_field('top_paid_fullname_1')),
    ('HighCompOfficer1Amount', copy_subaward_field('top_paid_amount_1')),
    ('HighCompOfficer2FullName', copy_subaward_field('top_paid_fullname_2')),
    ('HighCompOfficer2Amount', copy_subaward_field('top_paid_amount_2')),
    ('HighCompOfficer3FullName', copy_subaward_field('top_paid_fullname_3')),
    ('HighCompOfficer3Amount', copy_subaward_field('top_paid_amount_3')),
    ('HighCompOfficer4FullName', copy_subaward_field('top_paid_fullname_4')),
    ('HighCompOfficer4Amount', copy_subaward_field('top_paid_amount_4')),
    ('HighCompOfficer5FullName', copy_subaward_field('top_paid_fullname_5')),
    ('HighCompOfficer5Amount', copy_subaward_field('top_paid_amount_5')),
    ('SubcontractAwardAmount', CopyValues(subcontract='subcontract_amount')),
    ('TotalFundingAmount', CopyValues(subgrant='subaward_amount')),
    ('NAICS', CopyValues(subcontract='naics')),
    ('NAICS_Description', lambda models: models.naics_desc),
    ('CFDA_NumberAndTitle', CopyValues(subgrant='cfda_numbers')),
    ('AwardingSubTierAgencyName', copy_subaward_field('funding_agency_name')),
    ('AwardingSubTierAgencyCode', copy_subaward_field('funding_agency_id')),
    ('AwardDescription', CopyValues('overall_description', 'project_description')),
    ('ActionDate', CopyValues(subcontract='subcontract_date', grant='obligation_date')),
    ('PrimaryPlaceOfPerformanceCityName', copy_subaward_field('principle_place_city')),
    ('PrimaryPlaceOfPerformanceAddressLine1', copy_subaward_field('principle_place_street')),
    ('PrimaryPlaceOfPerformanceStateCode', copy_subaward_field('principle_place_state')),
    ('PrimaryPlaceOfPerformanceStateName', copy_subaward_field('principle_place_state_name')),
    ('PrimaryPlaceOfPerformanceZIP+4', copy_subaward_field('principle_place_zip')),
    ('PrimaryPlaceOfPerformanceCongressionalDistrict', copy_subaward_field('principle_place_district')),
    ('PrimaryPlaceOfPerformanceCountryCode', copy_subaward_field('principle_place_country')),
    ('PrimaryPlaceOfPerformanceCountryName', SubawardLogic(
        lambda subcontract: _country_name(subcontract.principle_place_country),
        lambda subgrant: _country_name(subgrant.principle_place_country)
    )),
    ('Vendor Doing As Business Name', copy_subaward_field('dba_name')),
    ('PrimeAwardReportID', CopyValues(procurement='contract_number', grant='fain')),
    ('ParentAwardId', CopyValues(procurement='idv_reference_number')),
    ('AwardReportMonth', copy_prime_field('report_period_mon')),
    ('AwardReportYear', copy_prime_field('report_period_year')),
    ('RecModelQuestion1', CopyValues('recovery_model_q1', 'compensation_q1')),
    ('RecModelQuestion2', CopyValues('recovery_model_q2', 'compensation_q2')),
    ('SubawardNumber', CopyValues('subcontract_num', 'subaward_num')),
    ('SubawardeeBusinessType', CopyValues(subcontract='bus_types')),
    ('AwardeeOrRecipientUniqueIdentifier', copy_prime_field('duns'))
])


def submission_procurements(submission_id):
    """Fetch procurements and subcontracts"""
    sess = GlobalDB.db().session
    log_data = {
        'message': 'Starting file F submission procurements',
        'message_type': 'CoreDebug',
        'submission_id': submission_id,
        'file_type': 'F'
    }
    logger.debug(log_data)

    award_proc_sub = sess.query(AwardProcurement.piid, AwardProcurement.parent_award_id,
                                AwardProcurement.naics_description, AwardProcurement.awarding_sub_tier_agency_c,
                                AwardProcurement.submission_id).\
        filter(AwardProcurement.submission_id == submission_id).distinct().cte("award_proc_sub")

    results = sess.query(award_proc_sub, FSRSProcurement, FSRSSubcontract).\
        filter(FSRSProcurement.contract_number == award_proc_sub.c.piid).\
        filter(FSRSProcurement.idv_reference_number.isnot_distinct_from(award_proc_sub.c.parent_award_id)).\
        filter(FSRSProcurement.contracting_office_aid == award_proc_sub.c.awarding_sub_tier_agency_c).\
        filter(FSRSSubcontract.parent_id == FSRSProcurement.id)

    # The cte returns a set of columns, not an AwardProcurement object, so we have to unpack each column
    for award_piid, award_parent_id, award_naics_desc, award_sub_tier, award_sub_id, proc, sub in results:
        # need to combine those columns again here so we can get a proper ModelRow
        award = AwardProcurement(piid=award_piid, parent_award_id=award_parent_id, naics_description=award_naics_desc,
                                 awarding_sub_tier_agency_c=award_sub_tier, submission_id=award_sub_id)
        yield ModelRow(award, proc, sub, naics_desc=award.naics_description)

    log_data['message'] = 'Finished file F submission procurements'
    logger.debug(log_data)


def submission_grants(submission_id):
    """Fetch grants and subgrants"""
    sess = GlobalDB.db().session
    log_data = {
        'message': 'Starting file F submission grants',
        'message_type': 'CoreDebug',
        'submission_id': submission_id,
        'file_type': 'F'
    }
    logger.debug(log_data)

    afa_sub = sess.query(AwardFinancialAssistance.fain, AwardFinancialAssistance.submission_id).\
        filter(AwardFinancialAssistance.submission_id == submission_id).distinct().cte("afa_sub")

    triplets = sess.query(afa_sub, FSRSGrant, FSRSSubgrant).\
        filter(FSRSGrant.fain == afa_sub.c.fain).\
        filter(FSRSSubgrant.parent_id == FSRSGrant.id)

    # The cte returns a set of columns, not an AwardFinancialAssistance object, so we have to unpack each column
    for afa_sub_fain, afa_sub_id, grant, sub in triplets:
        # need to combine those columns again here so we can get a proper ModelRow
        award = AwardFinancialAssistance(fain=afa_sub_fain, submission_id=afa_sub_id)
        yield ModelRow(award, grant=grant, subgrant=sub)

    log_data['message'] = 'Finished file F submission grants'
    logger.debug(log_data)


def generate_f_rows(submission_id):
    """Generated OrderedDicts representing File F rows. Subawards are filtered
    to those relevant to a particular submissionId"""
    log_data = {
        'message': 'Starting to generate_f_rows',
        'message_type': 'CoreDebug',
        'submission_id': submission_id,
        'file_type': 'F'
    }
    logger.debug(log_data)

    row_num = 1
    log_block_length = 1000
    for model_row in itertools.chain(submission_procurements(submission_id),
                                     submission_grants(submission_id)):
        result = OrderedDict()
        for key, mapper in mappings.items():
            value = mapper(model_row)
            if value is None:
                result[key] = ''
            else:
                result[key] = str(value)
        yield result
        if row_num % log_block_length == 0:
            log_data['message'] = 'Generated rows {}-{}'.format(row_num-(log_block_length-1), row_num)
            logger.debug(log_data)
        row_num += 1

    log_data['message'] = 'Finished generate_f_rows'
    logger.debug(log_data)
