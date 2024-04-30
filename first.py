'''1.WAPP TO COUNT THE NUMBER OF TIMES CHARCTERS OCCURS IN A GIVEN STRING

METHOD-1
s=input("Enter the String")
ch=input("Enter a character to find count")
count=0;
for i in s:
    if(i==ch):
        count+=1
print(count)

METHOD-2
print(s.count(ch))

METHOD-3
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(str(dict))

2.WAPP TO REPLACE ALL VOWELS WITH *

s=input("Enter the String")
rep=input("Enter the symbol")
vowels=['a','e','i','o','u','A','E','I','O','U']
str=''
for i in s:
    if i in vowels:
        str=str+rep
    else:
        str=str+i

print(str)

3. WAPP TO REVERSE THE STRING

s=input("Enter the String")
s1=''
for i in s:
    s1=i+s1
print("Original String"+s)
print("Reversed String"+s1)

4.WAPP TO COUNT THE NUMBER OF VOWELS IN A GIVEN STRING

s=input("Enter the String")
vowels=['a','e','i','o','u','A','E','I','O','U']
vcount=0
ccount=0
for i in s:
    if i in vowels:
        vcount+=1
    else:
        ccount+=1
print("vowel count"+vcount)
print("consonant count"ccount)

5.WAPP TO PRINT THE LONGEST WORD IN A GIVEN STRING

s=input("Enter the String")
longest=max(s.split(),key=len)
print(longest)'''

'''WRITE A COMMON LETTTERS BETWEEN TWO STRINGS
s1=input("Enter a String")
s2=input("Enter a another string")

s1=set(s1)
s2=set(s2)
print(s1)
print(s2)
lst=s1 & s2
print(lst)'''


'''WRITE A PROGRAM TO COUNT THE COUNT OF REPEATED WORDS
str=input("Enter the String")
spli=str.split(' ')
print(spli)
dict={}
for i in spli:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)'''


'''lst1=['Naina','kimi','shimi']
lst2=[123,456,789]
result=dict(zip(keys,values))
print(result)'''

'''class Demo:
    def __init__(self):
        self.x=10
    def disp(self):
        print("inside disp")
d1=Demo()
print(d1)
print(object)'''


'''count=int(input("Enter a size of list"))
lst=[]
for i in range(count):
    ele=int(input("enter a element"))
    lst.append(ele)
print(lst)
evenList=[]
for i in lst:
    if i%2==0:
        evenList.append(i)
print(evenList)'''

#WAPP TP PRINT THE ADDITION 0F EACH ELEMENT IN LIST
'''from operator import add
L=list(eval(input("Enter the elements of string seperated by comma")))
print(L)
M=list(eval(input("Enter the elements of string seperated by comma")))
print(M)
N=[]
N=list(map(add,L,M))'''

#ORRRRRRRRRRRR
'''L=list(eval(input("Enter the elements of string seperated by comma")))
print(L)
M=list(eval(input("Enter the elements of string seperated by comma")))
print(M)
N=[]
for i in range(len(L)):
    N.append(L[i]+M[i])
print(N)'''


'''L=list(eval(input("Enter the elements of string seperated by comma")))
even=[i for i in L if i%2==0]
print(even)'''


f1=open("Demo1.txt",'r')
print(f1.read())









