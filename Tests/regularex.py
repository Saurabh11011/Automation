# str1 = "Krishna 67 68 69"
# str2,*str3 = str1.split()
# print(f" the str2 is {str2} and str3 is {str3}")
# str1 = "cat loves cat"
# if str1 == str1[::-1]:
#     print("palindrome")
# else:
#     print("wohhoo")
from operator import indexOf

# lst = []
# list comprehenstion
# 1- print(list(number for number in range(1000) if number%7 == 0))
# 2 - print(list(number for number in range(1000) if '3' in str(number)))
#3- count the number of spaces in given string --
# str1 = input("Input the string = ")
# count = list(counter for counter in str1 if counter == " ")
# print(len(count))
#4 - print the consonants
# str1 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# str2 = "aeiou"
# consonants = list(con for con in str1 if con not in str2 and con!=' ')
# print(consonants)
# 5 - print the value of the list in the form of tuple and also the index of that
# lst = ["hi", 4, 8.99, "apple", ("t,b","n")]
# tup = tuple((value,lst[value]) for value in range(len(lst)))
# print((tuple2 for tuple2 in tup))
# 6-using enumerate print the value of the list in the form of tuple and also the index of that
# lst = ["hi", 4, 8.99, "apple", ("t,b","n")]
# tup = (value for value in enumerate(lst))
# print(list(tup))
#7-Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
# my_set = set()
# for common1 in list_a:
#     for common2 in list_b:
#         if common1 == common2:
#             my_set.add(common1)
# print([di for di in list_a if di in list_b]) ==> one more method to print the common numbers in both the list
#
# print(my_set)
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# diff technique of the above question -- common = (x for x in list_a for y in list_b if x == y)
# print(list(common))
#8 -- extract the number from the sentence
# str1 = "In 1984 there were 13 instances of a protest with over 1000 people attending"
# print(list(x for x in str1 if x.isdigit()))
# 9 --- print even if the number is even and odd if the number is odd in range of 20
# print(["even" if n%2 == 0 else "odd" for n in range(20)])
# 9 -Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
# list_a = [1,2,3,4,5,6,7,8,9]
# list_b = [2,7,1,12]
# print(tuple((x,y) for x in list_a for y in list_b if x == y))
#10--Find all of the words in a string that are less than 4 letters
# str1 = "cat donkey buffalo dog cow"
# str2 = str1.split()
# print([word for word in str2 if len(word)<4])
# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# print(set(x for x in range(1,1000)  for y in range(2,9) if (x%y) == 0))
# nums = [1,2,3,4]
# nums.append(3)
# print(f"the list is = {nums}")
# nums.insert(0,3)
# print(f"the list is = {nums}")
# nums.remove(3)
# print(f"the list is = {nums}")
# print(nums.count(3))
# nums2 = [2,5,3,9]
# print(nums.extend(nums2))
# print(nums.sort())
# print(nums)
# str1 = input("what is the string = ")
# print(str1 == str1[::-1])

# class range:
#     def __init__(self,animal):
#         self.animal = animal
#
#     def sound(self,select):
#         return(self.animal[select])
#
# dict = {"dog":"bark","cat":"meow"}
# obj = range(dict)
# print(obj.sound("dog"))
# -------------------------------------------------------------------------------
# Tries if __name__ == '__main__' with lambda.py
# def square():
#     print({x:x **2 for x in range(10) if x%2 == 0})
# def dict_comp():
#     keys = {'a','b','c','d'}
#     values = {1,2,3,4}
#
#     # ans = {x:y for x in keys for y in values}
#     ans = {x:y for (x,y) in zip(keys,values)}
#     print(ans)
# def add_value():
#     d = {"3": "a"}
#     d = d | {"4":"b"}
#     print(d)
#
# if __name__ == '__main__':
#     add_value()
#     square()
#     dict_comp()
#     print(" All the functions are running directly that's why ")
# else:
#     print(" The functions are executed by importing the module  ")


# square()
# dict_comp()
# awk '/manager/ {print}' employee.txt
# awk '{print $1$2}' employee.txt
# sed '/s/linux/unix/' employee.txt
# sed '3 /s/linux/unix/g' employee.txt

# --------------------------------------------------------------------
