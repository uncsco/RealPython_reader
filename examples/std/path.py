from mypkg.std.path import get_script_path

my_path = get_script_path(__file__)
print(my_path)

fname = str(my_path / 'dummy.txt')
print(fname)