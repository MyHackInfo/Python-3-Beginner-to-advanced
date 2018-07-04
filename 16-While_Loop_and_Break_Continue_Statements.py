'''
    1- While-loop example
    2- break statement example
    3- continur statement example
'''


# 1-while-loop
print('1-while-loop')
python=3
while python <10:
    print("yes this is python 3.",python)
    python=python + 1




# 2-while-loop with break statement
# we can use break statement with for-loop, and conditios statement
print('\n2-while-loop with break statement')
numpy=3.5
while numpy== 3.5:
    print("yes this is break statement with while-loop")
    break


# 3-continue statements with for-loop
print('\n3-continue statements with for-loop')
for n in range(1,10):
    if n == 5:
        continue

    print(n)
