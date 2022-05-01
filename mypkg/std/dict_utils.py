def kwargs_to_dict(**kwargs):
    """Convert the 'keyword arguments' to a dict.

    // https://stackoverflow.com/a/44412679

    >>> kwargs_to_dict(a=123, b='Bob', c={'code':'AB_12'})
    {'a': 123, 'b': 'Bob', 'c': {'code': 'AB_12'}}
    """
    return locals()['kwargs']


'''
## How to RENAME keys in a dict
https://www.geeksforgeeks.org/python-ways-to-change-keys-in-dictionary/

## Using `pop`
ini_dict = {'nikhil': 1, 'vashu' : 5, 
            'manjeet' : 10, 'akshat' : 15}
# printing initial json
print ("initial 1st dictionary", ini_dict)
  
# changing keys of dictionary
ini_dict['akash'] = ini_dict.pop('akshat')
  
# printing final result
print ("final dictionary", str(ini_dict))

## initial 1st dictionary {‘akshat’: 15, ‘manjeet’: 10, ‘vashu’: 5, ‘nikhil’: 1}
## final dictionary {‘akash’: 15, ‘manjeet’: 10, ‘vashu’: 5, ‘nikhil’: 1}


## Using `zip`  
# inititialising dictionary
ini_dict = {'nikhil': 1, 'vashu' : 5, 
            'manjeet' : 10, 'akshat' : 15}
  
# initialising list
ini_list = ['a', 'b', 'c', 'd']
  
# printing initial json
print ("initial 1st dictionary", ini_dict)
  
# changing keys of dictionary
final_dict = dict(zip(ini_list, list(ini_dict.values())))
  
# printing final result
print ("final dictionary", str(final_dict))

## initial 1st dictionary {‘akshat’: 15, ‘manjeet’: 10, ‘vashu’: 5, ‘nikhil’: 1}
## final dictionary {‘c’: 5, ‘d’: 1, ‘a’: 15, ‘b’: 10}
'''
