'''
    Defining and calling function or Return value
    Passing-arguments and Default-parameter
    Recursive-function
    Lambda-function
'''

# 1-Defining Funcion
print('\n1-Defining Funcion')
def python3():
    print('This is python3 function')

python3()                 # calling python3() function


# 2-Return value function
print('\n2-Return value function')
def retval():
    return 'This is retrun value function'

print(retval())           # calling retval() function 


# 3-Passing arguments function
print('\n3-Passing arguments function')
def arg(a,b):
    a=a+b
    return a

print(arg(4,6))           # calling arg() function


# 4-Default parameter function
print('\n4-Default parameter function')
def defaults(a,b='you put'):
    print(a,b)

print(defaults(20))        # calling defaults() function


# 5-Recursive Function
# When a function call itself is knows as recursion.
print('\n5-Recursive Function')
print('When a function call itself is knows as recursion.')
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

# 6-Lambda Function
print('\n6-Lambda Function')
lam= lambda a,b:a+b
print(lam(4,5))
