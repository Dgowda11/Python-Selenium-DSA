#Dictionary allows to store key,value pairs.

captions =  {
    'India' : 'Virat',
    'Pakistan': 'Sarfaraz',
    'Bangladesh': 'dimuth'
}

print(type(captions))
print(captions['India'])
print(captions.keys())
print(captions.values())
# Dictionary is basically a hashmap data structure. It is also called unordered map or hashtable
# Add new key value pair
captions['England'] = 'Someone'
print(captions)
# Delete the key and value
del captions['England']
print(captions)