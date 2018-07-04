'''
    ### Packing and Unpacking In function
    # Use (*) this symbole front on args to Unpacking
    # Use (*) for  store many value in args
    # Use (**) front on Kwargs
    
'''

#1-Use (*) for unpacking of args
print('\n1-Use (*) for unpacking of args')
num=[1,2,3,4,5]
print('\n# Without Unpacking')
print(num)               # Without Unpacking
print('\n# With Unpacking')
print(*num)              # With Unpacking


#2-Use (*) for  store many value in args
print('\n2-Use (*) for  store many value in args')
def num(*num):            #Here *num store many and any data-type    
    print(num)
num(2,3,4,5,6,7,8,[1,2,3],'sthl','this',234)

#3-Use (**) front on Kwargs
print('\n3-Use (**) front on Kwargs')
def datas(name,age,live):
    print(name)
    print(age)
    print(live)

dis={"name":"narsi","age":20,"live":"India"}
datas(**dis)                # Here **dis is dictionary and put in function kwargs




