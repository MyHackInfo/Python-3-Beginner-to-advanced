import  timeit
# Here we can test any program its runnig time condition in second useing timeit#
# in this first exp use generater
# and second exp use list
input_list = range(100)
def div_by_five(num):
    if num % 5 == 0 :
        return True
    else:
        return False
xyz=(i for i in input_list if div_by_five(i))
for i in xyz:
    x = i
    
a = 99999**999




print(timeit.timeit('''a = 99999**9 ''' , number= 10000))
