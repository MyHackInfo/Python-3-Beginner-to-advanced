'''
Condition statements are use for checking condition its true show true result and
condition are false then show false result.
 *** In python conditions Statements are ***
     1- if-statement
     2- if-else-statement
     3- elif-statement
     4- ternary-operator (this operator use for conditions checking 
'''

# if-statement
a=50
if a>49:
    print(" a is :",a)



# if-else-statement
a=50
b=60
if a>b:
    print(" a is :",a)

else:
    print(" a is less :",b)


# elif-statement
a=50
b=60
if a>b:
    print('a is :',a)
    
elif b>a:
    print('b is greate then a:',b)
else:
    print('b is:',b)


# ternary-operator
# On String
a='narsi'
b='python' if a == 'anrsi' else 'this is python 3'
print(b)

# On Number
age=20
b='narsi age is:',age if age == 20 else 'Narsi age is :20+'
print(b)

