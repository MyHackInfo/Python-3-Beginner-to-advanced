#Regular Expressions

import re
match=re.search('good','your dog is  good')
print(match)               #Show the match
print(match.re.pattern)    #Show the what match
print(match.string)        #Show the all String in match 
print(match.start())       #Show start index of match
print(match.end())         #Show end index of match



regex =re.compile('programing')
print(regex.findall('In computer science all programing language osm'))
