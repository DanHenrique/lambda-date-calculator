from datetime import datetime


def convert_date(*, date_iso8601, desired_format: str = '%Y-%m-%d %H:%M:%S'):
    '''Convert ISO 8601 formatted date to the desired format.'''
    if desired_format is None:
        raise ValueError('The provided value for desired_format is invalid.')

    date_obj = datetime.fromisoformat(date_iso8601)
    formatted_date = date_obj.strftime(desired_format)

    return {
        'date': formatted_date,
        'format': desired_format
    }
