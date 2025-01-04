import random
import datetime
# class lambda_fun:
#     def __init__(self,num,x,y):
#         self.num = num
#         self.x = x
#         self.y = y
#
#
#     # def add(self):
#     #     print(res(self.num))
#     # def product(self):
#     #     print(prod(self.x,self.y))
#
#
# obj = lambda_fun(13,4,8)
# res = lambda num:num+15
# prod = lambda x,y:x*y
#
# print(res(24))
# print(prod(12,4))
# # obj.add()
# # obj.product()
# mlt = lambda a:15*a
#
# print(mlt(4))

# def mt(n):
#     return lambda a: a * n
#
#
# rd = int(input("Input the random number of you choice"))
# for _ in range(10):
#     rand = random.choice(range(1, 10))
#     print(f"random number is {rand}")
#     res = mt(rand)
#     print(f" ho ho ho ho {res(rd)}")

# lis = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#
# res = sorted(lis,key=lambda x:x[0])
# print(res)

# dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#
# res = sorted(dict,key= lambda x:x['color'] )
# print(f"sorted list is {res}")

# ls = input("list input karo")
# ls2 = ls.split(",")
# # print(ls2)
# # print(list(x for x in ls2 if int(x)%2 == 0))
# # print(list(x for x in ls2 if int(x)%2!=0))
#
# even = lambda x:x%2 == 0
# evls = []
# oddls = []
# for i in ls2:
#     if even(int(i)):
#         evls.append(i)
#     else:
#         oddls.append(i)
# print(f"the even list is {evls}")
# print(f"the odd list is {oddls}")
# we can also use filter function to extract the values according to lambda function

# even = list(filter(lambda x:int(x)%2==0,ls2))
# print(f"the even list is {even}")
# odd = list(filter(lambda x:int(x)%2!=0,ls2))
# print(f"the odd list is {odd}")

#square and cube of the number

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sq = lambda x:int(x) **2
# cu = lambda x:int(x) **3
# ls2 = []
# ls3 = []
# for i in ls:
#     ls2.append(sq(i))
#     ls3.append(cu(i))
#     # print(f"sq of the number is = {sq(i)}")
#     # print(f"cube of the number is = {cu(i)}")
# print(f"list of square {ls2}")
# print(f"list of cube {ls3}")
# str1 = input("input the string = ")
# first = lambda x: True if x.startswith('p') else False
# # n = input("input the character you want to search")
# print(first('ython'))
# if first(str1) == n:
#     print("True")
# else:
#     print(False)
# mon = lambda x:x.month
# yea = lambda x:x.year
# now = datetime.datetime.now()
# print(f"the date and time is {now}")
# print(f"the month is {mon(now)}")
# date1 = input("Input the data = ")
# dt = lambda x:
# numb = lambd
# import subprocess
#
# # from outcome import capture
#
# result = subprocess.run("python --version",capture_output=True,text=True)
# print(result.stdout)


# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     print(n)
#     return fibo(n-1)+fibo(n-2)
#
# number = int(input("input karo number jo sequence chahiye"))
# ls = [fibo(number)]
# # print(f" ye list hai series ki {ls}")

# 0 1 1 2 3 5 8
# number = int(input("input karo number jo sequence chahiye"))
#
# a,b = 0,1
# i=0
# ls = [a,b]
# while i in range(number-2):
#     c = a+b
#     a=b
#     b=c
#     ls.append(c)
#     i+=1
#
# print(f" the serieds is = {ls}")

# fib = [0,1]
#
# while(len(fib) < number):
#     fib.append(fib[-1]+fib[-2])
# print(f"list of the series is {fib}")
#
# ls = [0,0,0]
# print(f"the reverse of fibonaci series is {fib.reverse()}")
# fib.sort(reverse=True)
# print(f"the series is sorted in desc order {fib}")
# fib.extend(ls)
# print(f"the appended new list is {fib}")
# print(f"the new list appended without method is {fib+ls}")
# fib.insert(2,8888)
# print(f"I'm inserting the number 8888 in the series on the 2nd place {fib}")
# print(f"I'm poping out the number and I'm not sure what it will print and we can also write a index in it {fib.pop()}")
# fib.remove(8888)
# print(f"I'm removing one number from it which I have inserted {fib}")

#try try and except programs
# ls = [2,4,5,6,9]
# try:
#     n = int(input("Input the index you want to acess in list = "))
#     print(ls[n])
#     print(ls[n]/n)
# except IndexError:
#     print("Index out of bound, INdex aapne galat daal diya ")
# except ZeroDivisionError:
#     print("Mamla gabad hai 0 se divide kar diya aapne ")
# except Exception as e:
#     print(e)
# print("ye waali lines exception ke baad ki hai")

#finally keyword -- Mainly it will be more handy when you use the function which is returning
# something but you want to run some line code necassarily like you want to delete some config
# before returning/coming out of functon

# def func():
#     ls = [2,4,5,6,9]
#     try:
#         n = int(input("Input the index you want to acess in list = "))
#         print(ls[n])
#         print(ls[n]/n)
#         return("chal gaya bhayii")
#     except IndexError:
#         return("Index out of bound, INdex aapne galat daal diya ")
#     except ZeroDivisionError:
#         return("Mamla gabad hai 0 se divide kar diya aapne ")
#     except Exception as e:
#         return (e)
#     finally:
#         print("ye waali lines exception ke baad ki hai jo ki finally block mai hai")
#
# print(func())

# a = int(input("Enter the value of the number"))
#
# if(a<9 or a>100):
#     raise ValueError("We were able to do this in the Interview")
# else:
#     print(f"the vale of a {a}")
# _________________________________________________________________________
#python code to implement the short hand if else

# a = 4000
# b = 3303
#
# print("A") if a <400 else  print("something") if a<b else print("bass ho gaya bhai")
# print("9") if a>400 else ""
# c=24 if a<b else 0
# print(c)
# ------------------------------------------------------------------------
# enumerate keyword we can use to print the index of the content and content also

# li = [1,3,4,6,3,2,23]
# for index,values in enumerate(li):
#     print(f"the index of the value is = {index}")
#     print(f"the value on that index is = {values}")

# for Tuple also it will print the index and values
# lis = [(1,2),(2,4),(4,5)]
# for index in lis:
#     i,j = enumerate(index)
#     print(f"The value of i is {i} and value of j is {j}")
# ---------------------------------------------------------------
#  Now the question is that how will you declare the SET
# s = set()
# # lsir = [1,2,3,4,5,3,2,4,6]
# lis = input(" please input the values in a list ")
# s.update(lis)
# print(f" the valuse of sets are {s}")
# ------------------------------------------------------------------------
# The question is  suppose i have 2 list of which 1 I want as keys and others values

# ls = [1,3,4,5,6,7]
# ls2= ['a','v','f','e','t','q']
# i=0
# j=0
# dic = {}
# while ((i in range(len(ls))) and (j in range(len(ls2)))):
#     print(f"the 'i' is {i} and 'j' is {j}")
#     dic.update({ls[i]:ls2[j]})
#     i+=1
#     j+=1
# print(f"the dictionary is = {dic}")

# lets check what could be the other options we can use zip(creates a tuple with the
# corresponding values of the lists ) as an 2nd method
# ls = [1,3,4,5,6,7]
# ls2= ['a','v','f','e','t','q']
# mydict = dict(zip(ls,ls2))
# print(f" the dictionary is {mydict}")
# --------------------------------------------------------------------------------
# The os module in python --very Important
# import os
#
# print(f" the current working direcotry is {os.getcwd()}")
# path = r'C:\Users\saura\PycharmProjects\selenium_new\Tests\delete'
# if not (os.path.exists(path)):
#     os.mkdir(path)
#     os.chdir(path)
#     for i in range(10):
#         os.mkdir(os.path.join(path,f'no{i}'))
#         # os.rmdir(os.path.join(path, f'no{i}'))
#
# else:
#     try:
#         for i in range(10):
#             os.rmdir(os.path.join(path, f'no{i}'))
#     except:
#         print("mamla thoda gadbad hai")
#     os.rmdir(path)
#
# print(f" the current working direcotry  2 is {os.getcwd()}")
# ---------------------------------------------------------------------
# The OS module in python for running a command on shell

# import os
# import subprocess
#
# os.system("python --version")
# # data = subprocess.run("cd ..", capture_output=True, text=True,shell=True)
# data2 = subprocess.run("dir", capture_output=True, text=True,shell=True)
# data3 = subprocess.run("python --version", capture_output=True, text=True,shell=True) #here shell=true not required
# print(f"lo ab output lo print statement ke saath wo upar wala directly run karega console par aur subprocess la ke de dega tumhe = {data2.stdout}")
# print(f"lo ab output lo print statement ke saath wo upar wala directly run karega console par aur subprocess la ke de dega tumhe = {data3.stdout}")
# # print(f"lo ab output lo print statement ke saath wo upar wala directly run karega console par aur subprocess la ke de dega tumhe = {data.stdout}")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# File I/O with os module
# import os
# import shutil
#
# path = r'C:\Users\saura\PycharmProjects\selenium_new\Tests\delete'
#
# if not os.path.exists(path):
#     os.mkdir(path)
# else:
#     shutil.rmtree(path)
#     # os.rmdir(path) this will not remove the directory if it is non empty
#     os.mkdir(path)
# file_path = os.path.join(path,'new_file.txt')
# with open(file_path,'w') as file:
#     file.write("hello this file I have created through python\n")
#     file.write("that too using the os module to create a directory first")
#
# print(f"file exists : {os.path.exists(file_path)}")
# with open(file_path,'r') as file:
#     text = file.read()
# print(f"text of the file is = {text}")
#
# with open(file_path,'a') as file:
#     file.write("\n ye statement maine file ko append mode mai khol ke likha hai")
# lst = ["\nye jo content hai wo list maise append hua hai\n"," ye 2nd string hai list ki\n","aur ye third hai\n"]
# with open(file_path,"a") as file:
#     file.writelines(lst)
# with open(file_path,'r') as file:
#     text = file.read()
# print(f" ye jo read kar rha hu ye appeded content hai = \U0001F60A {text}")
#
# with open(file_path,'r') as file:
#     text = file.readlines()
# print(f" ye jo read kar rha hu ye appeded content hai aur readlines and writeline to write the content use kiya hai = \U0001F60A {text}")
# ------------------------------------------------------------------------------------------------------------------------------------------
# map() ==>
# li = [1,2,3,4,5,6,8]
# li2 = ['abc','cdffer','ewrfcdsacdsa','cdsabtrfsadxzdsaf']
# print(list(map(lambda x:x **3,li)))
# print(list(map(len,li2)))
# ---------------------------------------------------------------------------------------------------------------------
# map and filter function==>
# li = [1,2,3,4,5,6,8]
# # to prin the squares of even digits
# print(list(map(lambda x:x **2,filter(lambda x:x%2 == 0,li))))
# print(list(filter(lambda x:x%2==0,li)))
# ----------------------------------------------------------------------------------
# reduce function
# from functools import reduce
#
# li = [1,2,3,4,5,6,8]
#
# print(f"the sum of the list is = {reduce(lambda x,y: x+y,li)}")
# --------------------------------------------------------------------------------
# How to use if __name__ == '__main__'
# import regularex
#
# print(f"the square of even digit numbers upto 10 are {regularex.square()}")
# so we have not included the if __name__=='__main__' so when I'm running this code
# automatically all  functions are getting run
# now I'm adding the above statement in the code of regularex.py and then I have run this code
# -----------------------------------------------------------------------------------------------------------------
# Experiment with decorators
import functools
from functools import reduce
from itertools import count
from operator import indexOf
from string import ascii_letters, ascii_lowercase
# from symbol import yield_arg

# def log_decorator(func):
#     # @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"Calling function {func.__name__}")
#         result = func(*args,**kwargs)
#         print(f"Function {func.__name__} finished")
#         return result
#     return wrapper
#
# @log_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# @log_decorator
# def add(a, b):
#     return a + b
# @log_decorator
# def dic(d,c):
#     print(d,c)
#
# say_hello("Alice")
# result = add(3, 5)
# print(f"Result of add: {result}")
# dic(1,c=4)
# ---------------------------------------------------------------------------
# getter and setter in class and also name mangling which is basically used to access the private decalered variables in python
# There is no such thing specified by the python but you can specify by yourself everything
# class Abc:
#     def __init__(self):
#         self._value = 56
#         self.__value3 = 24
#
#     @property
#     def value(self):
#         return f" the value you want is coming from getter = {self._value}"
#     @value.setter
#     def value(self,a):
#         self._value = a
#
# obj =Abc()
# print(f" this is the value coming from the function {obj.value}")
# print(f" this value is coming from variable {obj._value} ")
# obj.value = 34
# print(f" This value must be a changed value done through the setter {obj.value}")
# obj._value = 33
# print(f" This value must be a changed value and cahanged by accessing the variable=  {obj.value}")
# # print(f"this is the private variable so should not be accessed {obj.__value3}")
# # Above statement will not work we need name mangling to access as it is so called private or whatever you want to call ,it
# print(f"this is the private variable so should not be accessed {obj._Abc__value3}")
# # The above statement is basically is name mangling and there is not access sepecifier as such in python you can decalre you own convention to practice them
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# This is basically the demonstration of static method of the class
# We can call that method directly , with the class name , with the object as well

# class Bcd:
#     noofEmp = 34    #this is the class variable not a instance variable
#     def __init__(self):
#         self.a = "this is static method program" #
#         Bcd.noofEmp+=1  #class variable
#
#     @staticmethod
#     def stat(a,b):
#         print(f" this is the static method {a+b}")
#         return (a + b)
# obj = Bcd()
# for i in range(25):
#     obj2 = Bcd()
# print(obj.a)
# print(obj.stat(10,10))  #could be called with the object as well
# print(Bcd.stat(23,54))  # directly by Class name as well
# print(f"the number of employees are {obj2.noofEmp}")#calling the variable with obj2 but since it is kind of global so the value will be changed for other object as well
# # print(stat(20,40))
# ------------------------------------------------------------------------------------------------------------------
# print the things or method related to the list,dict etc we can use the following thing
# ls = [1,2,34,5]
# print(f" We can use this - {dir(ls)}") #methods whict list contains
# --------------------------------------------------------------------------------------------------
# If you want to converthe the Instance variable of the class to the dictionary use this
# class Efg:
#     def __init__(self,a,b):
#         self.a =a
#         self.b = b
#         self.version = 1.0
#
# obj = Efg(21,45)
# print(obj.__dict__) # output will be {'a': 21, 'b': 45, 'version': 1.0}
# ------------------------------------------------------------------------
# super() keyword
#method Overriding
# ------------------------------------------------------------------------------
#operator Overloading
# there are __add__ method and this type of methods are dundher methods
# class Overload:
#     def __init__(self,number):
#         self.number = number
#
#     def __add__(self,no2):
#         return(self.number+no2.number)
#
# obj = Overload(23)
# obj1 = Overload(34)
# print(obj+obj1) #it is kind off we are calling __add__ function with obj1 and sending the obj2 along with it

# --------------------------------------------------------------------------------
# Adding the command line utilty in python
# import argparse
#
# parser = argparse.ArgumentParser(description="A simple command-lin utilitiy")
# parser.add_argument('name', type=str,help='your Name')
# args = parser.parse_args()
# print(f"hello, {args.name}!")
# --------------------------------------------------------------------------------------------
# Requests module to try
import  requests
from unicodedata import decimal

# try:
#     headers = {"accept": "image/webp"}
#     output = requests.get('https://httpbin.org/image',headers=headers)
#     print(f"the status code us {output.status_code}")
#     if output.status_code ==200:
#         with open('file.webp',"wb") as file:
#             file.write(output.content)
#
#     # print(f"the data we get in response is = {output.text}")
#     output.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(f'HTTP error occurred: {err}')
# except Exception as err:
#     print(f'Other error occurred {err}')
# else:
#     print('success!')

# post requests

# url = 'https://httpbin.org/post'
# data = {'name': 'abc'}
#
# output = requests.post(url,data)
# print(f"the out pt is {output.json()}")
# print(f"the response code is {output.status_code}")
# -------------------------------------------------------------------------------------------------------------------------------
# Dictionary comprehension
# Create a dictionary of squares of numbers from 1 to 10
# diction = {x:x **2 for x in range(1,11)}
# print(f"this is the example of the dictionary comprehension {diction}")
# ________________________________________________________________________________________
# Mapping words to their reverse in a sentence
# Sample Output
# Hello, how are you?
# {'Hello,': ',olleH', 'how': 'woh', 'are': 'era', 'you?': '?uoy'}

# st = "Hello, how are you?"
# ls = st.split()
# dictio = {word:word[::-1] for word in ls} #word[::-1] this will reverse the string
# print(f"this is the dictionary fromed {dictio}")

# _______________________________________________________________________________________________________
# Mapping numbers to their binary and hexadecimal representations
# Sample Output
# {1: ('1', '1'), 2: ('10', '2'), 3: ('11', '3'), 4: ('100', '4'), 5: ('101', '5'), 6: ('110', '6'), 7: ('111', '7'), 8: ('1000', '8'), 9: ('1001', '9'), 10: ('1010', 'a')}

# def binary(ls):  THis is the logic to convert the decimal into binary
#     ls2= []
#     for i in ls:
#         b=i
#         n = []
#         while b:
#             n.append(b%2)
#             b = b//2
#         a = "".join(str(n))
#         ls2.append(a[::-1].strip("'['']'"))
#     print(ls2)
# def hexd():
#     # to = str(hex(24)).strip("0x")
#     print(f"ye hex hai = {hex(24)[2:]}")

# ls = [2,4,7,2,5]
# print({x:(bin(x)[2:],hex(x)[2:]) for x in ls})
# ___________________________________________________________________________________
# Mapping words to their palindrome status in a sentence
# Sample Output
# madam sees the racecar
# {'madam': True, 'sees': True, 'the': False, 'racecar': True}
# st = "madam sees the racecar"
# ls = st.split()
# ans = {x : True if x == x[::-1] else False for x in ls}
# print(f"the answer is = {ans}")
# ________________________________________________________________________________
# Mapping characters to their position in the alphabet
# Sample Output
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
# alpha = {ascii_lowercase[x]:x+1 for x in range(len(ascii_lowercase))}
# print(f"dictionary with the index of alphabet is = {alpha}") #-----ascii_lowercase gives us all the lowercase alphabet in the form of string
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mapping words to their frequency of containing the letter 'e'
# Sample Output
# Hello, how are you?
# {'Hello,': 1, 'how': 0, 'are': 1, 'you?': 0}
import re
# st = "Helleo, how are you?"
# ls = st.split()
# ans = {x:len(re.findall('e',x)) for x in ls}
# print(f"the ans is = {ans}")

# The 2nd is method which is more concise =>
# st = "Helleo, how are you?"
# ans = {word:word.count('e') for word in st.split()}
# print(f"the answer is = {ans}")
#--------------------------------------------------------------------------------------------
# Distinct words and their length, excluding those with lengths not Fibonacci, in a sentence
# Sample Output
# Hello, how are you?
# {'are': 3, 'how': 3}
# def fibo(a):
#     ser = [0,1]
#     while(len(ser)<=a+1): #here the good logic will be (a<=ser[-1])
#         ser.append(ser[-1]+ser[-2])
#         # a-=1
#     # print(f"the fibonacci series is = {ser}")
#     return ser
#
# st = "Hello, how are you?"
# # 1- split 2- list ayegin 3- hame check karna hai len of word in the list
# ans = {word:len(word) for word in set(st.split()) if len(word) in fibo(len(word))}
# print(f" answer is = {ans}")
#------------------------------------------------------------------------------------------
# Characters and their occurrence count, excluding punctuation, in a sentence
# Sample Output
# Hello, how are you?
# {'w': 1, 'r': 1, 'u': 1, 'o': 3, 'e': 2, 'H': 1, 'l': 2, 'h': 1, ' ': 3, 'y': 1, 'a': 1}
# def chek(ls,st)

# st = "Hello, how are you?"
# # print(f" this is the set = {set(st)}")
# # print(f" the occurence of the word is {st.count('e')}")
# # ls = st.split()
# ans = {word:st.count(word) for word in set(st) if word not in ['!','@','#','$','%','^','&','*','?',',','.']}
# print(f"the answer is {ans}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Distinct words and their length, excluding those with even lengths, in a sentence
# Sample Output
# Hello, how are you?
# {'how': 3, 'are': 3}
# st = "Hello, how are you?"
# lst = st.split()
# ans = {word:len(word) for word in set(lst) if len(word)%2!=0}
# print(f"this is the answer = {ans}")
# -------------------------------------------------------------------------------------------------------------------------------------
#  Distinct words and their length, excluding those with odd lengths, in a sentence
# Sample Output
# Hello, how are you?
# {'Hello,': 6, 'you?': 4}
# st = "Hello, how are you?"
# lst = st.split()
# ans = {word:len(word) for word in set(lst) if len(word)%2 == 0}
# print(f"the answer is = {ans}")
# ----------------------------------------------------------------------------------------------------------------------------------
#  Pairs of distinct elements and their character position sum from two lists
# Sample Output
# ['abc', 'def', 'ghi']
# ['jkl', 'mno', 'pqr']
# {('abc', 'jkl'): 615, ('abc', 'mno'): 624, ('abc', 'pqr'): 633, ('def', 'jkl'): 624, ('def', 'mno'): 633, ('def', 'pqr'): 642, ('ghi', 'jkl'): 633, ('ghi', 'mno'): 642, ('ghi', 'pqr'): 651}
# from functools import reduce
# def sum1(st):
#     ans1=0                                =====>> this is the first method but not kind of dictinary comprehension
#     ans1=[ord(word) for word in st]
#     ans2= reduce(lambda x,y: x+y, ans1)
#     # print(f"the assafsdf is {ans2}")
#     return ans2
#
# # sum1('abc')
# ls = ['abc', 'def', 'ghi']
# ls2 = ['jkl', 'mno', 'pqr']
# ans = {(word1,word2):sum1(word1)+sum1(word2) for word1 in set(ls) for word2 in set(ls2)}
# print(f" need improvement {ans}")

# =======> Below is the method which is kind of more pythonic way/dictionary Comprehension
# ls = ['abc', 'def', 'ghi']
# ls2 = ['jkl', 'mno', 'pqr']
# ans = {(word1,word2):sum([ord(char) for char in word1])+sum([ord(char) for char in word2]) for word1 in set(ls) for word2 in set(ls2)}
# print(f" need improvement {ans}")

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Pairs of distinct elements and their absolute difference from two lists
# Sample Output
# [3, 6, 9]
# [5, 10, 15]
# {(3, 5): 2, (3, 10): 7, (3, 15): 12, (6, 5): 1, (6, 10): 4, (6, 15): 9, (9, 5): 4, (9, 10): 1, (9, 15): 6}

# ls1 =  [3, 6, 9]
# ls2 = [5, 10, 15]
# abs_sum = {(number1,number2):number1+number2 for number1 in set(ls1) for number2 in set(ls2)}
# abs_dif = {(number1,number2):abs(number1-number2) for number1 in set(ls1) for number2 in set(ls2)}
# print(f"the absolute difference  is = {abs_dif}")
# print(f"the absolute sum  is = {abs_sum}")

# --------------------------------------------------------------------------------------------------------
# Numbers and their binary representation from 1 to 10
# Sample Output
# {1: '1', 2: '10', 3: '11', 4: '100', 5: '101', 6: '110', 7: '111', 8: '1000', 9: '1001', 10: '1010'}

# ans = {numb:bin(numb)[2:] for numb in range(10)}
# print(f"the sum is {ans}")

# -----------------------------------------------------------------------------------------------------------------------------
# Mapping lowercase letters to their ASCII values
# Sample Output
# {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

# ans = {word:ord(word) for word in ascii_lowercase}
# print(ans)
# -------------------------------------------------------------------------------------------------------------------------------------
# Create a dictionary of characters and their counts, excluding whitespace characters, from a string
# Sample Output
# hello world
# {'o': 2, 'h': 1, 'r': 1, 'w': 1, 'e': 1, 'l': 3, 'd': 1}
# str = "hello world"
# ans = {word:str.count(word) for word in str if word!=' '}
# print(f" the answer is = {ans}")
# ----------------------------------------------------------------------------------------------------------------------------------------
# Create a dictionary of numbers with their divisors
# Sample Output
# [1, 2, 3, 4, 5]
# {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5]}

# ls = [1, 2, 3, 4, 5]
# ans = {number:[x for x in range(1,number+1) if number%x == 0] for number in ls}
# print(f" the answer is = {ans}")

# ----------------------------------------------------------------------------------------------------------------------------------------------
# Create a dictionary of strings with words in reverse
# Sample Output
# Python is fun
# {0: 'fun', 1: 'is', 2: 'Python'}

# str = "Python is fun"
# ls = str.split()
# ans = {i:ls[-(i+1)] for i in range(len(ls))}   =================> this is 1 way but we can use enumerate method which gives the index and the value
# print(f" the word is = {ans}")
# ============>2nd method
# str = "Python is fun"
# ans = {i:word for i,word in enumerate(str.split()[::-1])}
# print(f"the answer is = {ans}")
# ---------------------------------------------------------------------------------------------------------------------------------------------
# Create a dictionary of numbers with their signs reversed
# Sample Output
# [5, -10, 15, -20, 25]
# {5: -5, -10: 10, 15: -15, -20: 20, 25: -25}

# ls = [5, -10, 15, -20, 25]
# ans = {number:(-1)*number for number in ls }
# print(f"ths answeris {ans}")
# _________________________________________________________________________________________________________________________________________
# Create a dictionary of strings with vowels removed
# Sample Output
# ['apple', 'banana', 'cherry']
# {'apple': 'ppl', 'banana': 'bnn', 'cherry': 'chrry'}
# str = ['apple', 'banana', 'cherry']
# ans = {word:"".join(filter(lambda x : x.lower() not in ['a','e','i','o','u'],word)) for word in str}
# print(f" the answer is = {ans}")
# -----------------------------------------------------------------------------------------------------------------------------------------
# To do is 31------------------------------------------------------




# --------------------------------------------------------------------------------------------------
# ====================Lambda Function===============================================
# Write a Python program to remove None values from a given list using the lambda function.
#
# ls = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# print(list(filter(lambda x:x is not None,ls)))

# ----------------------------------------------------------------------------------------------------------
#  Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.
# Original list with tuples:
# [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# Maximum and minimum values of the said list of tuples:
# (74, 62)
# ls = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# ls2 = list(sorted(ls,key=lambda x:x[1]))
# print((ls2[-1][1],ls2[0][1]))
# to find the max and min you can use the max and min function works like sorted function
# max(itr,key=)
# ------------------------------------------------------------------------------------
# Write a Python program to remove specific words from a given list using lambda.
# Original list:
# ['orange', 'red', 'green', 'blue', 'white', 'black']
# Remove words:
# ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']
# ls = ['orange', 'red', 'green', 'blue', 'white', 'black']
# rmls = ['orange', 'black']
# print(list(filter(lambda x:x not in rmls,ls)))  ===> one way is this
# # print([word for word in ls if word not in rmls]) ===> this is the 2nd method
# -------------------------------------------------------------------------------------------
#  Write a Python program to count the occurrences of items in a given list using lambda.
# Original list:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}
# ls = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# print(list(map(lambda x:(x,ls.count(x)),ls))) ==> map(function,iterable)
# toh hamare case mai ek ek value ls se uthe ke lambda funcion mai jaayega
# aur jo bhi function return hoga wo dictionary form mai jaayega
# ------------------------------------------------------------------------------------------------------
# Write a Python program to sort a given list of strings (numbers) numerically using lambda.
# Original list:
# ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# ['-500', '-12', '0', '4', '7', '12', '45', '100', '200']

# ls = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# print(sorted(ls,key=lambda x : int(x)))
# -----------------------------------------------------------------------------------------------------
# Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
# ls = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# ls2 = [word for word in ls if isinstance(word,str)]
# ls.sort(key=lambda x:(isinstance(x,str), x))
# res = lambda x:(isinstance(x,str), x)
# ls3 = [(False,1),(False,10),(True,"red"),(False,0),(True,"orange")]
# ls3.sort()
# print(f"this is the tuple sorting = {ls3}")
# print(res(ls))
# print(ls)
# -------------------------------------------------------------------------------------------------------------------------
# Write a Python program to find the index position and value of the maximum and minimum values in a given list of numbers using lambda.
# Original list:
# [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
# Index position and value of the maximum value of the said list:
# (5, 89)
# Index position and value of the minimum value of the said list:
# (3, 10.11)
# ls = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
# print(f" Index position and value of the maximum value of the said list: {max((enumerate(ls)), key=lambda x: x[1])}")
# print(f" Index position and value of the minimum value of the said list: {min((enumerate(ls)),key=lambda x:x[1])} ")

# -------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to convert string elements to integers inside a given tuple using lambda.
# Original tuple values:
# (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# New tuple values:
# ((233, 33), (1416, 55), (2345, 34))
# ls = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# print(tuple((int(word[0]),int(word[2])) for word in ls )) ===> Method 1 of doing it
# print(tuple(map(lambda x:(int(x[0]),int (x[2])),ls))) ===>2nd method
# -----------------------------------------------------------------------------------------------------------------
# Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
# Original Tuple:
# ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (30.5, 34.25, 27.0)
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (25.5, -18.0, 3.75)
# In below program  zip and * is also used ==>
# "*" - This is called unpacking operator because it unpacks the iterator for eg - ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3)) this is the tuple of tuples
# now this operator will change it like this (10, 10, 10) (30, 45, 56) (81, 80, 39) (1, 2, 3)  these are bunch of individual tuples which can be used, so what exactly the use of
# unpacking operator we can use the unpacked values individually and apply the operation on it on the above tuple of tuples if we want to apply the zip function we cannot apply it
# as it needs the individual iterators to combine and since it was single tuple of tuples we cannot apply it on that, so when we have unpacked that we got multiple tuples individually
# and we have combine them through the zip to find the avg.
# "zip" => what does zip is doing is it is taking the multiple iterator and combining their 1st values and rsults a tuple example- list = [1,2,3] and list2 = [6,8,9] list(zip(list,list2)
# the result will be [(1,6],(2,8),(3,9)]
# -------------------------answer of the question
# tup = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# avg =map(lambda x:sum(x)/len(x),zip(*tup))
# print(tuple(avg))
# --------------------------------------------------------------------------------------------------------------------------------------------
# Write a Python program to multiply all the numbers in a given list using lambda.
# Original list:
# [4, 3, 2, 2, -1, 18]
# Mmultiply all the numbers of the said list: -864
# Original list:
# [2, 4, 8, 8, 3, 2, 9]
# Mmultiply all the numbers of the said list: 27648

# ls = [2.2, 4.12, 6.6, 8.1, 8.3]
#
# print(reduce(lambda x,y: x*y,ls))

# -------------------------------------------------------------------------------------------------
# Write a Python program to reverse strings in a given list of string values using lambda.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'

# ls = ['Red', 'Green', 'Blue', 'White', 'Black']
# print(list(map(lambda x:x[::-1],ls))) ===>method 1
# # print([word[::-1] for word in ls ])  ====> method 2
# ************very important****************************
# to convert any list aur any iterator into the string we can use ''.join that will be changd into string
# *************************************************************
# --------------------------------------------------------------------------------------------
# Write a Python program to find the nested list elements, which are present in another list using lambda.
# Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# ls2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# print([list(filter(lambda x:x in ls,word))for word in ls2])
# ----------------------------------------------------------------------------------------------------------
# Write a Python program to find the elements of a given list of strings that contain a specific substring using lambda.
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Elements of the said list that contain specific substring:
# ['black']
# Substring to search:
# abc
# Elements of the said list that contain specific substring:
# []
# str1 = ['red', 'black', 'white', 'green', 'orange']
# str2 = "ed"
# print([list(filter(lambda x: str2 in x,str1))]) ==> method1
# print(list(word for word in str1 if str2 in word)) ===> method2

# ----------------------------------------------------------------------------------------------------
# Write a Python program to remove all elements from a given list present in another list using lambda.
# Original lists:
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [2, 4, 6, 8]
# print([list(filter(lambda x:x not in list2 ,list1))])

# ----------------------------------------------------------------------------------------------------
# Write a Python program to sort a list of lists by a given index of the inner list using lambda.
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Sort the said list of lists by a given index ( Index = 0 ) of the inner list
# [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
# Sort the said list of lists by a given index ( Index = 2 ) of the inner list
# [('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]
# ls = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# inde = 1
# ls.sort(key=lambda x:x[2])
# print(ls)

# -------------------------------------------------------------------------------------------------------------------------------
# printing the values of the dictionaries and sorting them with the key and values
# dic = {"abc":1,"cde":2,"efg":7,"ghi":5}
# print(dic.items())
# for i in sorted(dic,key=lambda x:dic[x],reverse=True):
#         print({i:dic[i]})

    # print(i)
# print(sorted(dic,reverse=True))
# for std in dic:
#     print(std)

# -----------------------------------------------------------------------------------------------------------------------------
# str1 = "saurabh@gmail.sau"
# pattern = r"sau"
# # print((re.match(pattern,str1)).group()) #getting an error because it is returning a None as it does not find anything and we are grouping None here
# # print((re.search(pattern,str1)).group()) # om output getting because re.search is looking out the pattern thorughout the string but match is looking for it in the starting only
# # print((re.findall(pattern,str1))) # it will give the list of the occurence of the pattern in the string
# if str1.endswith("com"):
#     print("valid")
# else:
#     print("Invalid ")
