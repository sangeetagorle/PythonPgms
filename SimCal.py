#WAP to build a Simple Calculator


'''a=int(input("Enter a value of a"))
b=int(input("Enter a value of b"))
choice=int(input("Enter your Choice 1--Addition  2--Substraction  3--Multiplication  4--Division"))
if choice==1:
    print("Addition of two numbers is",(a+b))
elif choice==2:
    print("Substraction of two numbers is",(a-b))
elif choice==3:
    print("Multiplication of two numbers is",(a*b))
elif choice==4:
    print("Division of two numbers is",(a/b))
else:
    print("Invalid Choice")'''
#WAPP TO TAKE LIST AS USER INPUT AND PRINT LIST
'''lst1=[]
n=int(input("Enter the size of list1"))
for i in range(0,n):
    ele=int(input())
    lst1.append(ele)
print(lst1)'''
#WAPP TO PRINT TABLES OF A GIVEN NUMBER USING STATICMETHOD
'''class Demo:
    n=int(input("Enter the number to find its table"))
    @staticmethod
    def tables(n):
        for i in range(1,11):
            print(n*i)           
Demo.tables(Demo.n)'''
#WAPP TO PRING COUNT IN EACH WORD OF A GIVEN STRING
'''str=input("Enter the string");
str1=str.split(' ')
for i in str1:
    print(f"{i} {len(i)}")'''

lst=list(eval(input("enter values")))
for i in lst:
    print(lst)




