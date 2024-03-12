str1='hello'
# string indexing
print(str1[0])
print(str1[-1])

# string slicing
print(str1[0:4])
print(str1[:3])

# membership operator
print('hel' in str1)

# raw string 
str2='hello \n how are you?'
str3=r'hello \n how are you?'
print(str2)
print(str3)

str4='hello'
print(str4.center(50, '*'))
print(str4.count('l'))


s1='h'
print(s1.isdigit())