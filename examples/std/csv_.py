from mypkg.std.csv import from_csv as from_csv_000
print(from_csv_000)


from mypkg.std import from_csv
print(from_csv)

print(id(from_csv_000) == id(from_csv))
