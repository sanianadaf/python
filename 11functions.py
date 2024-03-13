import functools 
def hello():
    name = input("enter name : ")
    print(f'hello {name}')
    
# hello()

def hello1(n, t):
    print(f'hello {n}. good {t}')

name = input("enter your name : ")
time = input("enter the time : ")
# hello1(name,time)
# hello1(time=time, name=name)

def hello2(n, t='morning'):
    print(f'hello {n}. good {t}.')

hello2(name)
hello2(name, time)


# lambda function

def double(x):
    return x * 2
# print(double(5))

dbl = lambda x: x * 2
print(dbl(23))

max = lambda a, b: a if a >b else b
print(max(34, 56))

# map function

num_list = [1,2,3,4,5,6,7,8,9]

def sqr(x):
    return x ** 2
for i in num_list:
    print(sqr(i))

sqr_num_list = map(sqr, num_list)
print(sqr_num_list)

# filter function

def even_num(x):
    if x % 2 == 0:
        return x
even_list = filter(even_num, num_list)
print(even_list)

def sum(a,b):
    return a+b
list_sum = functools.reduce(sum, num_list)
print(list_sum)