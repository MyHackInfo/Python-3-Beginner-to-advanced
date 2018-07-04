'''
    ### All about Dictionary ###
    Dictionaray store value using key (key:value).
    We can access value using key.
    Dictionary use Curly braces.
'''
# 1-Create Dictionary
print('\n1-Create Dictionary')
dicts={'name':'narsi','age':20}
print(dicts)

# 2-Access Dictionary Using key
print('\n2-Access Dictionary Using key')
print(dicts['name'])
print(dicts['age'])

# 3-Update Dictionary
print('\n3-Update Dictionary')
dicts['name']='ghost'
dicts['age']=21
print(dicts)

# 4-Delete Dictionary Elements
print('\n4-Delete Dictionary Elements')
del dicts['age']
print(dicts)

# 5-Dictionary Method
print('\n5-Dictionary Method')
print(str(dicts))

print(len(dicts))

print(dicts.keys())

print(dicts.values())




