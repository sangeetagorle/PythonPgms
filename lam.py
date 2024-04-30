'''ref=lambda a,b:a+b
print(ref(10,20))'''

'''ref=lambda a,b: b if a<b else  a
print(ref(10,30))'''

from funtools import *
lst1=[1,2,3,4]
prod=reduce(lambda a,b:a*b,lst1)
print(prod)

'''lst1=[1,2,3,4]
even=list(filter(lambda a:a%2==0,lst1))
print(even)'''

'''lst1=[1,2,3,4]
sqrt=list(map(lambda a:a**2,lst1))
print(sqrt)'''
