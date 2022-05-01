__all__ = [
    'from_csv'
]

import csv

def from_csv(fname):
    """Return list of rows from CSV (or TSV [tab]) file

    TODO: [ ] if fname is a string, use StringIO
    """
    with open(fname, 'r') as inf:
        dialect = csv.Sniffer().sniff(inf.readline(), delimiters=['\t',','])
        inf.seek(0)
        dr = csv.DictReader(inf, dialect=dialect)
        dat = [d for d in dr]
    return dat