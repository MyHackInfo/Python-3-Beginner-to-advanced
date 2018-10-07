import multiprocessing

# Same in this function add args
# def spawn(num):
#   print("Spawned! {} ".format(num))
def spawn():
    print("Spawned!")

if __name__ == '__main__':
    for i in range(50):
        # Here you can add some args (target=spawn,args=(i,)
        p = multiprocessing.Process(target=spawn)
        # random way 
        p.start()
        # order way
        p.join()
        
