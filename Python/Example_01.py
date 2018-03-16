# Importing the required libraries
import hashlib, json, sys

"""
def HashFunc(msg=""):
    
    if type(msg) != str:
        msg = json.dumps(msg,sort_keys=True)        
    
    if sys.version_info.major == 2: 
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
"""


# Here We are Creating an Dictionary
# The Dictionary has Key and Value
# Key = 'A' 'B' 'C' and Value 1,2,3
D = {}
D['A'] = 1
D['B'] = 2
D['C'] = 3

# Here we use a for loop to print the contents of Dicitonary
for k in D.keys():
    print(D[k])
    
# Here we print both key value pair
for k,v in D.items():
    print(k,v)
    
# Create Two Arrays for Key and Values

Key_Arr = {'M','O','N','K'}
Val_Arr = {10,20,30,40}

Hash_Var = {k:v for k,v in zip(Key_Arr,Val_Arr)}
Hash_Var

map(hash,Val_Arr)
hash('0')


hash_obj = hashlib.sha256(b'Hello')
hash_obj.hexdigest()


