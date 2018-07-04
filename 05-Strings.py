'''
Python can also manipulate Strings, which can be expressed in several ways.
1 -They can be enclosed in single quotes ('...')
2 -or double quotes ("...") with the same result.
3 -"\" can be used to escape quotes.
4 -Here \n means newline!.
5 -Strings can be Concatenated with the + Operator, and repeated with Asterisk(*)
6 -Subset of String using Slice operator
'''
print('1 -single quotes Strings')
print("2 -Double quotes Strings")
print('3 -Both "Single" \'and\' "Double" quotes')
print('4 -Here "\ n" means \n newline!')
print('5 -Strings' + ' Concatenated with + operator' + '\n' + 2 * 'and repeated with Asterisk(*)')

# Subset of String using Slice operator
print("6 -Subset of String using Slice[] operator")
str="this is string"
print(str[0:])
print(str[:3])
print(str[3:])
print(str[2:5])
print(str[:-1])




