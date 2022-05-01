__all__ = [
    'convert_dicts_to_csv',
    'from_csv'
]

from csv import DictReader, Sniffer

def from_csv(fname):
    """Return list of rows from CSV (or TSV [tab]) file

    TODO: [ ] if fname is a string, use StringIO
    """
    with open(fname, 'r') as inf:
        dialect = Sniffer().sniff(inf.readline(), delimiters=['\t',','])
        inf.seek(0)
        dr = DictReader(inf, dialect=dialect)
        dat = [d for d in dr]
    return dat


from csv import DictWriter
from io import StringIO

from .str_ import str_remove_whitespace


# SOURCE: [sbsapi-ethrev] pn_dict.py
def convert_dicts_to_csv(rows: list, fields: list = None) -> str:
    """Convert dicts to CSV

    >>> res = convert_dicts_to_csv([
    ...   {'id':110, 'name':'Amy', 'age':30},
    ...   {'id':120, 'name':'Bob', 'age':80},
    ...   {'id':130, 'name':'Cat', 'age':40},
    ... ])
    >>> csv_txt = '''
    ... id,name,age
    ... 110,Amy,30
    ... 120,Bob,80
    ... 130,Cat,40
    ... '''.strip()
    >>> str_remove_whitespace(res) == str_remove_whitespace(csv_txt)
    True
    """
    fieldnames = fields if fields else rows[0].keys()

    sio = StringIO()
    dw = DictWriter(sio, fieldnames=fieldnames)
    dw.writeheader()
    dw.writerows(rows)
    return sio.getvalue()
