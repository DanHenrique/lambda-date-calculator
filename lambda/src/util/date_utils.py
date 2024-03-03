from datetime import datetime


def convert_date(*, date_iso8601):
    """Convert ISO 8601 formatted date to the desired format."""
    date_obj = datetime.fromisoformat(date_iso8601)
    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")  # Desired format, for example

    return formatted_date
