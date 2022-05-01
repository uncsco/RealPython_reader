# OKAY
'''
import mypkg

print(mypkg.__version__)
print(mypkg.hello('Amy'))
print(mypkg.hello('Barbara', do_filter=True))
'''

from mypkg import hello

def my_filter(s):
    return s

print(hello.hello('Amy'))
print(hello.hello('Barbara', do_filter=True))

# REDEFINE
hello._filter = my_filter
print(hello.hello('Barbara', do_filter=True))
