from collections import OrderedDict
from sqlalchemy import func, cast, Date

from dataactcore.models.stagingModels import DetachedAwardProcurement, AwardProcurement

file_model = DetachedAwardProcurement
staging_model = AwardProcurement

mapping = OrderedDict([
    ('piid', 'piid'),
    ('awardingsubtieragencycode', 'awarding_sub_tier_agency_c'),
    ('awardingsubtieragencyname', 'awarding_sub_tier_agency_n'),
    ('awardingagencycode', 'awarding_agency_code'),
    ('awardingagencyname', 'awarding_agency_name'),
    ('parentawardid', 'parent_award_id'),
    ('awardmodificationamendmentnumber', 'award_modification_amendme'),
    ('typeofcontractpricing', 'type_of_contract_pricing'),
    ('contractawardtype', 'contract_award_type'),
    ('naics', 'naics'),
    ('naics_description', 'naics_description'),
    ('awardeeorrecipientuniqueidentifier', 'awardee_or_recipient_uniqu'),
    ('ultimateparentlegalentityname', 'ultimate_parent_legal_enti'),
    ('ultimateparentuniqueidentifier', 'ultimate_parent_unique_ide'),
    ('awarddescription', 'award_description'),
    ('primaryplaceofperformancezip_4', 'place_of_performance_zip4a'),
    ('primaryplaceofperformancecongressionaldistrict', 'place_of_performance_congr'),
    ('awardeeorrecipientlegalentityname', 'awardee_or_recipient_legal'),
    ('legalentitycityname', 'legal_entity_city_name'),
    ('legalentitystatedescription', 'legal_entity_state_descrip'),
    ('legalentityzip_4', 'legal_entity_zip4'),
    ('legalentitycongressionaldistrict', 'legal_entity_congressional'),
    ('legalentityaddressline1', 'legal_entity_address_line1'),
    ('legalentityaddressline2', 'legal_entity_address_line2'),
    ('legalentityaddressline3', 'legal_entity_address_line3'),
    ('legalentitycountrycode', 'legal_entity_country_code'),
    ('legalentitycountryname', 'legal_entity_country_name'),
    ('periodofperformancestartdate', 'period_of_performance_star'),
    ('periodofperformancecurrentenddate', 'period_of_performance_curr'),
    ('periodofperformancepotentialenddate', 'period_of_perf_potential_e'),
    ('orderingperiodenddate', 'ordering_period_end_date'),
    ('actiondate', 'action_date'),
    ('actiontype', 'action_type'),
    ('federalactionobligation', 'federal_action_obligation'),
    ('currenttotalvalueofaward', 'current_total_value_award'),
    ('potentialtotalvalueofaward', 'potential_total_value_awar'),
    ('fundingsubtieragencycode', 'funding_sub_tier_agency_co'),
    ('fundingsubtieragencyname', 'funding_sub_tier_agency_na'),
    ('fundingofficecode', 'funding_office_code'),
    ('fundingofficename', 'funding_office_name'),
    ('awardingofficecode', 'awarding_office_code'),
    ('awardingofficename', 'awarding_office_name'),
    ('referenced_idv_agency_identifier', 'referenced_idv_agency_iden'),
    ('fundingagencycode', 'funding_agency_code'),
    ('fundingagencyname', 'funding_agency_name'),
    ('primaryplaceofperformancestatecode', 'place_of_performance_state'),
    ('primaryplaceofperformancecountrycode', 'place_of_perform_country_c'),
    ('idv_type', 'idv_type'),
    ('vendor_doing_as_business_name', 'vendor_doing_as_business_n'),
    ('vendor_phone_number', 'vendor_phone_number'),
    ('vendor_fax_number', 'vendor_fax_number'),
    ('multiple_or_single_award_idv', 'multiple_or_single_award_i'),
    ('type_of_idc', 'type_of_idc'),
    ('a76_fair_act_action', 'a_76_fair_act_action'),
    ('dod_claimant_program_code', 'dod_claimant_program_code'),
    ('clinger_cohen_act_planning_compliance', 'clinger_cohen_act_planning'),
    ('commercial_item_acquisition_procedures', 'commercial_item_acquisitio'),
    ('commercial_item_test_program', 'commercial_item_test_progr'),
    ('consolidated_contract', 'consolidated_contract'),
    ('contingency_humanitarian_or_peacekeeping_operation', 'contingency_humanitarian_o'),
    ('contract_bundling', 'contract_bundling'),
    ('contract_financing', 'contract_financing'),
    ('contracting_officer_determination_of_business_size', 'contracting_officers_deter'),
    ('cost_accounting_standards_clause', 'cost_accounting_standards'),
    ('cost_or_pricing_data', 'cost_or_pricing_data'),
    ('country_of_product_or_service_origin', 'country_of_product_or_serv'),
    ('construction_wage_rate_req', 'construction_wage_rate_req'),
    ('evaluated_preference', 'evaluated_preference'),
    ('extent_competed', 'extent_competed'),
    ('fedbizopps', 'fed_biz_opps'),
    ('foreign_funding', 'foreign_funding'),
    ('gfe_gfp', 'government_furnished_prope'),
    ('information_technology_commercial_item_category', 'information_technology_com'),
    ('interagency_contracting_authority', 'interagency_contracting_au'),
    ('local_area_set_aside', 'local_area_set_aside'),
    ('major_program', 'major_program'),
    ('purchase_card_as_payment_method', 'purchase_card_as_payment_m'),
    ('multi_year_contract', 'multi_year_contract'),
    ('national_interest_action', 'national_interest_action'),
    ('number_of_actions', 'number_of_actions'),
    ('number_of_offers_received', 'number_of_offers_received'),
    ('other_statutory_authority', 'other_statutory_authority'),
    ('performance_based_service_acquisition', 'performance_based_service'),
    ('place_of_manufacture', 'place_of_manufacture'),
    ('price_evaluation_adjustment_preference_percent_difference', 'price_evaluation_adjustmen'),
    ('product_or_service_code', 'product_or_service_code'),
    ('program_acronym', 'program_acronym'),
    ('other_than_full_and_open_competition', 'other_than_full_and_open_c'),
    ('recovered_materials_sustainability', 'recovered_materials_sustai'),
    ('research', 'research'),
    ('sea_transportation', 'sea_transportation'),
    ('labor_standards', 'labor_standards'),
    ('small_business_competitiveness_demonstration_program', 'small_business_competitive'),
    ('solicitation_identifier', 'solicitation_identifier'),
    ('solicitation_procedures', 'solicitation_procedures'),
    ('fair_opportunity_limited_sources', 'fair_opportunity_limited_s'),
    ('subcontracting_plan', 'subcontracting_plan'),
    ('dod_acquisition_program', 'program_system_or_equipmen'),
    ('type_set_aside', 'type_set_aside'),
    ('epa_designated_product', 'epa_designated_product'),
    ('materials_supplies_article', 'materials_supplies_article'),
    ('transaction_number', 'transaction_number'),
    ('sam_exception', 'sam_exception'),
    ('city_local_government', 'city_local_government'),
    ('county_local_government', 'county_local_government'),
    ('inter_municipal_local_government', 'inter_municipal_local_gove'),
    ('local_government_owned', 'local_government_owned'),
    ('municipality_local_government', 'municipality_local_governm'),
    ('school_district_local_government', 'school_district_local_gove'),
    ('township_local_government', 'township_local_government'),
    ('us_state_government', 'us_state_government'),
    ('us_federal_government', 'us_federal_government'),
    ('federal_agency', 'federal_agency'),
    ('federally_funded_research_and_development_corp', 'federally_funded_research'),
    ('us_tribal_government', 'us_tribal_government'),
    ('foreign_government', 'foreign_government'),
    ('community_developed_corporation_owned_firm', 'community_developed_corpor'),
    ('labor_surplus_area_firm', 'labor_surplus_area_firm'),
    ('corporate_entity_not_tax_exempt', 'corporate_entity_not_tax_e'),
    ('corporate_entity_tax_exempt', 'corporate_entity_tax_exemp'),
    ('partnership_or_limited_liability_partnership', 'partnership_or_limited_lia'),
    ('sole_proprietorship', 'sole_proprietorship'),
    ('small_agricultural_cooperative', 'small_agricultural_coopera'),
    ('international_organization', 'international_organization'),
    ('us_government_entity', 'us_government_entity'),
    ('emerging_small_business', 'emerging_small_business'),
    ('c8a_program_participant', 'c8a_program_participant'),
    ('sba_certified_8a_joint_venture', 'sba_certified_8_a_joint_ve'),
    ('dot_certified_disadvantaged_business_enterprise', 'dot_certified_disadvantage'),
    ('self_certified_small_disadvantaged_business', 'self_certified_small_disad'),
    ('historically_underutilized_business_zone_hubzone_firm', 'historically_underutilized'),
    ('small_disadvantaged_business', 'small_disadvantaged_busine'),
    ('the_abilityone_program', 'the_ability_one_program'),
    ('historically_black_college_or_university', 'historically_black_college'),
    ('c1862_land_grant_college', 'c1862_land_grant_college'),
    ('c1890_land_grant_college', 'c1890_land_grant_college'),
    ('c1994_land_grant_college', 'c1994_land_grant_college'),
    ('minority_institution', 'minority_institution'),
    ('private_university_or_college', 'private_university_or_coll'),
    ('school_of_forestry', 'school_of_forestry'),
    ('state_controlled_institution_of_higher_learning', 'state_controlled_instituti'),
    ('tribal_college', 'tribal_college'),
    ('veterinary_college', 'veterinary_college'),
    ('educational_institution', 'educational_institution'),
    ('alaskan_native_servicing_institution', 'alaskan_native_servicing_i'),
    ('community_development_corporation', 'community_development_corp'),
    ('native_hawaiian_servicing_institution', 'native_hawaiian_servicing'),
    ('domestic_shelter', 'domestic_shelter'),
    ('manufacturer_of_goods', 'manufacturer_of_goods'),
    ('hospital_flag', 'hospital_flag'),
    ('veterinary_hospital', 'veterinary_hospital'),
    ('hispanic_servicing_institution', 'hispanic_servicing_institu'),
    ('foundation', 'foundation'),
    ('woman_owned_business', 'woman_owned_business'),
    ('minority_owned_business', 'minority_owned_business'),
    ('women_owned_small_business', 'women_owned_small_business'),
    ('economically_disadvantaged_women_owned_small_business', 'economically_disadvantaged'),
    ('joint_venture_women_owned_small_business', 'joint_venture_women_owned'),
    ('joint_venture_economically_disadvantaged_women_owned_small_business', 'joint_venture_economically'),
    ('veteran_owned_business', 'veteran_owned_business'),
    ('service_disabled_veteran_owned_business', 'service_disabled_veteran_o'),
    ('contracts', 'contracts'),
    ('grants', 'grants'),
    ('receives_contracts_and_grants', 'receives_contracts_and_gra'),
    ('airport_authority', 'airport_authority'),
    ('council_of_governments', 'council_of_governments'),
    ('housing_authorities_public_tribal', 'housing_authorities_public'),
    ('interstate_entity', 'interstate_entity'),
    ('planning_commission', 'planning_commission'),
    ('port_authority', 'port_authority'),
    ('transit_authority', 'transit_authority'),
    ('subchapter_scorporation', 'subchapter_s_corporation'),
    ('limited_liability_corporation', 'limited_liability_corporat'),
    ('foreign_owned_and_located', 'foreign_owned_and_located'),
    ('american_indian_owned_business', 'american_indian_owned_busi'),
    ('alaskan_native_owned_corporation_or_firm', 'alaskan_native_owned_corpo'),
    ('indian_tribe_federally_recognized', 'indian_tribe_federally_rec'),
    ('native_hawaiian_owned_business', 'native_hawaiian_owned_busi'),
    ('tribally_owned_business', 'tribally_owned_business'),
    ('asian_pacific_american_owned_business', 'asian_pacific_american_own'),
    ('black_american_owned_business', 'black_american_owned_busin'),
    ('hispanic_american_owned_business', 'hispanic_american_owned_bu'),
    ('native_american_owned_business', 'native_american_owned_busi'),
    ('subcontinent_asian_asian_indian_american_owned_business', 'subcontinent_asian_asian_i'),
    ('other_minority_owned_business', 'other_minority_owned_busin'),
    ('for_profit_organization', 'for_profit_organization'),
    ('nonprofit_organization', 'nonprofit_organization'),
    ('other_not_for_profit_organization', 'other_not_for_profit_organ'),
    ('us_local_government', 'us_local_government'),
    ('referenced_idv_modification_number', 'referenced_idv_modificatio'),
    ('undefinitized_action', 'undefinitized_action'),
    ('domestic_or_foreign_entity', 'domestic_or_foreign_entity'),
    ('lastmodifieddate', 'last_modified'),
    ('referenced_idv_multiple_or_single', 'referenced_mult_or_single'),
    ('referenced_idv_agency_name', 'referenced_idv_agency_desc'),
    ('baseandexercisedoptionsvalue', 'base_exercised_options_val'),
    ('baseandalloptionsvalue', 'base_and_all_options_value'),
    ('primaryplaceofperformancecountryname', 'place_of_perf_country_desc'),
    ('award_or_idv_flag', 'pulled_from'),
    ('primaryplaceofperformancestatename', 'place_of_perfor_state_desc'),
    ('primaryplaceofperformancecountyname', 'place_of_perform_county_na'),
    ('referenced_idv_type', 'referenced_idv_type'),
    ('primaryplaceofperformancecityname', 'place_of_perform_city_name'),
    ('cage_code', 'cage_code'),
    ('inherently_governmental_function', 'inherently_government_func'),
    ('organizational_type', 'organizational_type'),
    ('number_of_employees', 'number_of_employees')
])
db_columns = [val for key, val in mapping.items()]


def query_data(session, agency_code, start, end, page_start, page_stop):
    """ Request D1 file data

        Args:
            session - DB session
            agency_code - FREC or CGAC code for generation
            start - Beginning of period for D file
            end - End of period for D file
            page_start - Beginning of pagination
            page_stop - End of pagination
    """
    rows = initial_query(session).\
        filter(file_model.awarding_agency_code == agency_code).\
        filter(func.cast_as_date(file_model.action_date) >= start).\
        filter(func.cast_as_date(file_model.action_date) <= end).\
        slice(page_start, page_stop)

    return rows


def initial_query(session):
    return session.query(
        file_model.piid,
        file_model.awarding_sub_tier_agency_c,
        file_model.awarding_sub_tier_agency_n,
        file_model.awarding_agency_code,
        file_model.awarding_agency_name,
        file_model.parent_award_id,
        file_model.award_modification_amendme,
        file_model.type_of_contract_pricing,
        file_model.contract_award_type,
        file_model.naics,
        file_model.naics_description,
        file_model.awardee_or_recipient_uniqu,
        file_model.ultimate_parent_legal_enti,
        file_model.ultimate_parent_unique_ide,
        file_model.award_description,
        file_model.place_of_performance_zip4a,
        file_model.place_of_performance_congr,
        file_model.awardee_or_recipient_legal,
        file_model.legal_entity_city_name,
        file_model.legal_entity_state_descrip,
        file_model.legal_entity_zip4,
        file_model.legal_entity_congressional,
        file_model.legal_entity_address_line1,
        file_model.legal_entity_address_line2,
        file_model.legal_entity_address_line3,
        file_model.legal_entity_country_code,
        file_model.legal_entity_country_name,
        func.to_char(cast(file_model.period_of_performance_star, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.period_of_performance_curr, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.period_of_perf_potential_e, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.ordering_period_end_date, Date), 'YYYYMMDD'),
        func.to_char(cast(file_model.action_date, Date), 'YYYYMMDD'),
        file_model.action_type,
        file_model.federal_action_obligation,
        file_model.current_total_value_award,
        file_model.potential_total_value_awar,
        file_model.funding_sub_tier_agency_co,
        file_model.funding_sub_tier_agency_na,
        file_model.funding_office_code,
        file_model.funding_office_name,
        file_model.awarding_office_code,
        file_model.awarding_office_name,
        file_model.referenced_idv_agency_iden,
        file_model.funding_agency_code,
        file_model.funding_agency_name,
        file_model.place_of_performance_state,
        file_model.place_of_perform_country_c,
        file_model.idv_type,
        file_model.vendor_doing_as_business_n,
        file_model.vendor_phone_number,
        file_model.vendor_fax_number,
        file_model.multiple_or_single_award_i,
        file_model.type_of_idc,
        file_model.a_76_fair_act_action,
        file_model.dod_claimant_program_code,
        file_model.clinger_cohen_act_planning,
        file_model.commercial_item_acquisitio,
        file_model.commercial_item_test_progr,
        file_model.consolidated_contract,
        file_model.contingency_humanitarian_o,
        file_model.contract_bundling,
        file_model.contract_financing,
        file_model.contracting_officers_deter,
        file_model.cost_accounting_standards,
        file_model.cost_or_pricing_data,
        file_model.country_of_product_or_serv,
        file_model.construction_wage_rate_req,
        file_model.evaluated_preference,
        file_model.extent_competed,
        file_model.fed_biz_opps,
        file_model.foreign_funding,
        file_model.government_furnished_prope,
        file_model.information_technology_com,
        file_model.interagency_contracting_au,
        file_model.local_area_set_aside,
        file_model.major_program,
        file_model.purchase_card_as_payment_m,
        file_model.multi_year_contract,
        file_model.national_interest_action,
        file_model.number_of_actions,
        file_model.number_of_offers_received,
        file_model.other_statutory_authority,
        file_model.performance_based_service,
        file_model.place_of_manufacture,
        file_model.price_evaluation_adjustmen,
        file_model.product_or_service_code,
        file_model.program_acronym,
        file_model.other_than_full_and_open_c,
        file_model.recovered_materials_sustai,
        file_model.research,
        file_model.sea_transportation,
        file_model.labor_standards,
        file_model.small_business_competitive,
        file_model.solicitation_identifier,
        file_model.solicitation_procedures,
        file_model.fair_opportunity_limited_s,
        file_model.subcontracting_plan,
        file_model.program_system_or_equipmen,
        file_model.type_set_aside,
        file_model.epa_designated_product,
        file_model.materials_supplies_article,
        file_model.transaction_number,
        file_model.sam_exception,
        file_model.city_local_government,
        file_model.county_local_government,
        file_model.inter_municipal_local_gove,
        file_model.local_government_owned,
        file_model.municipality_local_governm,
        file_model.school_district_local_gove,
        file_model.township_local_government,
        file_model.us_state_government,
        file_model.us_federal_government,
        file_model.federal_agency,
        file_model.federally_funded_research,
        file_model.us_tribal_government,
        file_model.foreign_government,
        file_model.community_developed_corpor,
        file_model.labor_surplus_area_firm,
        file_model.corporate_entity_not_tax_e,
        file_model.corporate_entity_tax_exemp,
        file_model.partnership_or_limited_lia,
        file_model.sole_proprietorship,
        file_model.small_agricultural_coopera,
        file_model.international_organization,
        file_model.us_government_entity,
        file_model.emerging_small_business,
        file_model.c8a_program_participant,
        file_model.sba_certified_8_a_joint_ve,
        file_model.dot_certified_disadvantage,
        file_model.self_certified_small_disad,
        file_model.historically_underutilized,
        file_model.small_disadvantaged_busine,
        file_model.the_ability_one_program,
        file_model.historically_black_college,
        file_model.c1862_land_grant_college,
        file_model.c1890_land_grant_college,
        file_model.c1994_land_grant_college,
        file_model.minority_institution,
        file_model.private_university_or_coll,
        file_model.school_of_forestry,
        file_model.state_controlled_instituti,
        file_model.tribal_college,
        file_model.veterinary_college,
        file_model.educational_institution,
        file_model.alaskan_native_servicing_i,
        file_model.community_development_corp,
        file_model.native_hawaiian_servicing,
        file_model.domestic_shelter,
        file_model.manufacturer_of_goods,
        file_model.hospital_flag,
        file_model.veterinary_hospital,
        file_model.hispanic_servicing_institu,
        file_model.foundation,
        file_model.woman_owned_business,
        file_model.minority_owned_business,
        file_model.women_owned_small_business,
        file_model.economically_disadvantaged,
        file_model.joint_venture_women_owned,
        file_model.joint_venture_economically,
        file_model.veteran_owned_business,
        file_model.service_disabled_veteran_o,
        file_model.contracts,
        file_model.grants,
        file_model.receives_contracts_and_gra,
        file_model.airport_authority,
        file_model.council_of_governments,
        file_model.housing_authorities_public,
        file_model.interstate_entity,
        file_model.planning_commission,
        file_model.port_authority,
        file_model.transit_authority,
        file_model.subchapter_s_corporation,
        file_model.limited_liability_corporat,
        file_model.foreign_owned_and_located,
        file_model.american_indian_owned_busi,
        file_model.alaskan_native_owned_corpo,
        file_model.indian_tribe_federally_rec,
        file_model.native_hawaiian_owned_busi,
        file_model.tribally_owned_business,
        file_model.asian_pacific_american_own,
        file_model.black_american_owned_busin,
        file_model.hispanic_american_owned_bu,
        file_model.native_american_owned_busi,
        file_model.subcontinent_asian_asian_i,
        file_model.other_minority_owned_busin,
        file_model.for_profit_organization,
        file_model.nonprofit_organization,
        file_model.other_not_for_profit_organ,
        file_model.us_local_government,
        file_model.referenced_idv_modificatio,
        file_model.undefinitized_action,
        file_model.domestic_or_foreign_entity,
        func.to_char(cast(file_model.last_modified, Date), 'YYYYMMDD'),
        file_model.referenced_mult_or_single,
        file_model.referenced_idv_agency_desc,
        file_model.base_exercised_options_val,
        file_model.base_and_all_options_value,
        file_model.place_of_perf_country_desc,
        file_model.pulled_from,
        file_model.place_of_perfor_state_desc,
        file_model.place_of_perform_county_na,
        file_model.referenced_idv_type,
        file_model.place_of_perform_city_name,
        file_model.cage_code,
        file_model.inherently_government_func,
        file_model.organizational_type,
        file_model.number_of_employees)
