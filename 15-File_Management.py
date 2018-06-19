'''
      ###File Management###
      
    #1- File open and close using open()and close()
    #2- We can access text file text line by line using for loop
    #3- File name ,close and mode operation
    #4- File inside write some text using write() function

'''

# 1- File open and close using open()and close()
# open(filename,access,buffering)
print('\n1- File open and close using open()and close()')
file=open('textfile.txt','r')             # Here use 'r' r mode for read fiel
print(file.read())                        # read() function use for read text in textfile
print(file.tell())                        # tell() function use for current position of cursor
file.seek(2)                              # seek() function use for moving cursor position
#file.close()                              # close() function is good for every time close open file



# 2- We can access text file text line by line using for loop
print('\n2-We can access text file text line by line using for loop')
for line in file:
    print(line)

file.close()

# 3- We can access file_name,
# file_close and not close,
# file mode
print('\n3-File name ,close and mode operation')
print('File name is :' +file.name)
print('File is close and not : '+str(file.closed))
print('File Mode : ' + file.mode)


# 4- File inside write some text using write() function
print('\n4-File inside write some text using write() function')
file2=open('two.txt','w+')                            
file2.write('this is write function working')       
file2.seek(0)
print(file2.read())
file2.close()



