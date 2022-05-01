from mypkg.std.csv_ import from_csv as from_csv_000
print(from_csv_000)

'''
from mypkg.std import from_csv
print(from_csv)

print(id(from_csv_000) == id(from_csv))
'''

from mypkg.std.csv_ import convert_dicts_to_csv

res = [{'id':110, 'name':'Amy', 'age':30}]

print(convert_dicts_to_csv(res))