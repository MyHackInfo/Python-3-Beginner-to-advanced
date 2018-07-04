'''
    ### All about List ###
    List store all type of data like- Number,String,Boolean,list etc.
    We can access list value with indexs and slice operator.
    List use Square brackets.
'''

# 1-Create list
# Using Square Brackets []
print('\n1-Create list')
our_list=[1,2,3,'a','b','String',1947,'narsi']  # Single
nul_list=[[1,2,3],[4,5,6],[5,8,9]]              # Multi_dimensional_list
print(our_list)
print(nul_list)


# 2-Access List Using Indexs
print('\n2-Access List Using Indexs')
print(our_list[0])
print(our_list[4])
print(our_list[7])

# 3-Access List Using Slicing [:]
print('\n3-Access List Using Slicing [:]')
print(our_list[:])
print(our_list[3:])
print(our_list[:2])
print(our_list[-1])
print(our_list[::-1])

# 4-Deleting List Elements Using del keyword
print('\n4-Deleting List Elements Using del keyword')
del our_list[2]
print(our_list)


# 5-Update List
print('\n5-Update List')
lis=[1,2,3,4]
lis[2]=56
print(lis)


# 6-List Operations
print('\n6-List Operations')
print(len(our_list))                #1-Len method len()
print([1,2,3] + ['narsi','jeetu'])  #2-Concatenation +
print(['repetition']*2)             #3-Repetition    *
print(3 in [1,2,4,5])               #4-Membership    in
print(max([1,2,3]))                 #5-Max           max
print(min([1,2,3]))                 #6-Min           min

# 6-List Method
print('\n6-List Method')
list1=[1,34,5,6]
print(list1.append(342))

print(list1.insert(3,44))

print(list1.remove(6))

print(list1.reverse())
