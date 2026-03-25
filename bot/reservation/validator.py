from dateutil.parser import parse as date_parse

def is_empty(value):
    return value in [None, ""]


def parse_date_or_none(value):
    try:
        return date_parse(value, dayfirst=True).date()
    except:
        return None