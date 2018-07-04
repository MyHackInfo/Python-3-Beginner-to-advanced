# Exception Handling

# Simple Error ZeroDivisionError
print('1-Simple Error ZeroDivisionError')
try:
    a=500/0
except Exception as e:
    print(e)



# User define Error message

print('\n2-User define Error message')
try:
    file=open('test.txt','r')

except IOError:
    print('you cant find this file ')


# finally message
print('\n3-finally message by user')
try:
    b=5040/0

except Exception as e:
    print(e)

finally:
    print('Error is my creation do not warry about this ok')
