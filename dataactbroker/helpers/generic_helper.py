import re
import calendar

from dataactcore.utils.responseException import ResponseException
from dataactcore.utils.statusCode import StatusCode


def year_period_to_dates(year, period):
    """ Converts a year and period to the real-life start and end dates they represents.

        Args:
            year: integer representing the year to use
            period: integer representing the period (month of the fiscal year) to use

        Returns:
            Strings representing the start and end dates of the given quarter
    """
    # Make sure year is in the proper format
    if not year or not re.match('^\d{4}$', str(year)):
        raise ResponseException('Year must be in YYYY format.', StatusCode.CLIENT_ERROR)
    # Make sure period is a number 2-12
    if not period or period not in list(range(2, 13)):
        raise ResponseException('Period must be an integer 2-12.', StatusCode.CLIENT_ERROR)

    # Set the actual month, add 12 if it's negative so it loops around and adjusts the year
    month = period - 3
    if month < 1:
        month += 12
        year -= 1

    # Get the last day of the month
    last_day_of_month = calendar.monthrange(year, month)[1]

    start = str(month).zfill(2) + '/01/' + str(year)
    end = str(month).zfill(2) + '/' + str(last_day_of_month) + '/' + str(year)

    return start, end


def format_internal_tas(row):
    """ Concatenate TAS components into a single field for internal use.

        Args:
            row: row of data with TAS elements

        Returns:
            TAS components concatenated into a single string
    """
    # This formatting should match formatting in dataactcore.models.stagingModels concat_tas
    tas = ''.join([
        row['allocation_transfer_agency'] if row['allocation_transfer_agency'] else '000',
        row['agency_identifier'] if row['agency_identifier'] else '000',
        row['beginning_period_of_availa'] if row['beginning_period_of_availa'].strip() else '0000',
        row['ending_period_of_availabil'] if row['ending_period_of_availabil'].strip() else '0000',
        row['availability_type_code'].strip() if row['availability_type_code'].strip() else ' ',
        row['main_account_code'] if row['main_account_code'] else '0000',
        row['sub_account_code'] if row['sub_account_code'] else '000'
    ])
    return tas
