'''
    ### All about Tuple ###
    Tuple are same as list and store any data-type.
    But Tuple cannot be chaged unlike list.
    Tuple use Parentheses.
'''
# 1-Create Tuple
# Using Parentheses ()
print('\n1-Create Tuple')
our_tuple=(1,2,3,'a','good',1233)
print(our_tuple)

# Empty Tuple
print('\nEmpty Tuple')
tup=()
print(tup)

# Single value Tuple
print('\nSingle value Tuple')
tup2=(3,)
print(tup2)

# 2-Access Tuple Using Indexs same as List
print('\n2-Access Tuple Using Indexs same as List')
print(our_tuple[5])
print(our_tuple[3])

# 3-Access Tuple Using Slicing [:]
print('\n3-Access Tuple Using Slicing [:]')
print(our_tuple[:])
print(our_tuple[2:])
print(our_tuple[-2])
print(our_tuple[::-1])


# 4-Update Tuple But not its give error
print('\n4-Update Tuple But not its give error Like this')
tuple1=(1,2,3)
#tuple1[2]=3                # Plese uncomment for see result
print(tuple1)

# 5-Delete Tuple
print('\n5-Delete Tuple')
tuple123=(1,2,3,4,5,6,9)
del tuple123
print('done')

# 6-Tuple Operations
print('\n6-Tuple Operations')
new_tup=(1,2,3,4,5,6)
print(len(new_tup))
print(max(new_tup))
print(min(new_tup))



