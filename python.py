# my_num = 3
# print(my_num)
# my_var = "5"
# print(type(my_var))
# my_int = int(my_var)
# print(type(my_int))
# my_int = float (my_var)
# print(type(my_int))

# a = 5
# b = 7
# c = -1

# d = (-b + (b**2 - 4*a*c)**0.5)// 2*a
# print(d)

# num = -b + (b**2 - 4*a*c)**0.5
# den = 2*a

# print(num/den)

# from re import S


# Pi = 3.142
# R = 5
# Vol = 4/3*Pi*5**3
# print(Vol)

# #2
# # b = 24.95
# # p = b*0.40
# # s = 3
# # bs = 0.75
# # scf = p+S
# # print(scf)
# # print(p)

# b = 24.95
# discount = 0.6
# ship_1 = 3
# ship_2 = 0.75
# num_of_books = 60

# total_book_price = b*discount*num_of_books

# total_checkout_price = total_book_price+ship_1+(ship_2*59)

# print(total_checkout_price)


# # start_hour = 6:52
# # Distance_1 = 1
# # Time_1 = 8.15
# # Distance_2 = 3
# # Time_2 = 7.12*Distance_2
# # print(Time_2)
# # Distance_3 = 1
# # Time_3 = 8.15


# # start_time = 6*3600 + (52*60)
# # easy_time = ((8*60) +15)*2
# # tempo_time = ((7*60) +12)*3

# # run_time = easy_time + tempo_time

# # end_time = start_time + run_time
# # end_time_hr = end_time//3600
# # end_time_min = (end_time%3600)//60
# # end_time_sec = (end_time%3600)%60

# # print(f"{end_time_hr}:{end_time_min}:{end_time_sec}am")

# y = "Hello World!"
# print(y)


# new_string = "This is a string."

# new_doc_string = '''This is a nice string and i

# can move to the next 

# # line and work
 
# #  Thanks'''

# # print(new_doc_string)

# # print(new_doc_string)

# string1 = "This is a string"
# string2 = "I love this string,"
# string3 = 1456

# # print(string1+ "" +string2)

# # print(string1, string2)

# # print(string1 [1])

# # print(string3[2])

# print(string1[2:6])
# print(string1[2:6:2])

# name=""

#  print("my name is {name}")

# name = "benita"
# print(f"my name is {name}")

# name = input ("Enter your name:")
# print(f"my name is {name}")

# print(f"""Hello, {name}.

# Your order is ready

# for pick up

# Cheers, Village Lantern.""")

# 
# from tkinter import E


# print( "The man said, \"You do what you have to do, so you can do what you want to do.\"")

# print ("This is the boy's dog. \nHis name is Jack!")


from cgi import print_arguments
from ctypes import Structure
from dataclasses import replace
from ntpath import join
from posixpath import split
from tkinter import E
from tracemalloc import stop
from turtle import title
from unittest import result


# name = "Emmanuel"
# name.count("E")
# print (name.count(E))

# name = input("Enter your name: \n::>>")
# print(name.title())

# name = input("Enter your name: \n::>>")
# print(name.split())

# name = input("Enter your name: \n::>>")
# print(name.split())

# name = input("Enter your name: \n::>>")
# a= (name.split())
# print(a)
# print(a[0])

# a = ["david" , "adeleke"]

# print("".join(a).title())


# sequence_string= "hello my name is precious. \nI school at univelcity, \n thank you"
# word_from_user = input( "Enter word of your choice:")
# number_of_word_found_in_sequence = sequence_string.count(word_from_user)
# new_sequence_string = sequence_string.replace(word_from_user, word_from_user.upper())


# print(number_of_word_found_in_sequence)

# 
# sequence_string= "hello precious, \n welcome to univelcity \n your class begins now"
# users_word= input("Enter a word of your choice:")
# word_count_for_user= sequence_string.count(users_word)

# print (F""" {word_count_for_user} results found """)

# users_word_highlight = sequence_string.replace(users_word, users_word.upper())

# print(users_word_highlight)

# text = """An alternative is designed development, in which high-level insight into the problem can 
# make the programming much easier. In this case, the insight is that a Time object is really
# a three-digit number in base 60"""

# search_for = input("").lower()
# print(f"{text.lower().count(search_for)} result(S) found ")

# print(text.lower().replace(search_for, search_for.upper()))

# Assignment 1

# x = int (input ("Enter a number: ") )
# y = int (input ("Enter a number: ") )
# z = int (input ("Enter a number: ") )

# total_number = x + y + z
# number_count = 3
# average_number = total_number/number_count
# print(average_number)


# # #Assignment 2
# users_word = input ("Enter your reply: ")
# search_for = input ("")

# first_word = users_word[0].upper
# users_word_split = users_word.split()


# output_word = users_word.replace(search_for, search_for.upper())

# print(output_word)

# print(search_for)

# Assignment3
# users_string= """I hope your had fun today in clas"""
# word_search= input("Enter a word of your choice:")

# word_count_for_user= users_string.count(word_search)

# print (F""" {word_count_for_user} results found """)

#Practice
# first_name= "Precious"
# Last_name= "Amadi"

# print(first_name+Last_name)

# print(first_name*3)

#Assignment2 Correction

# print("Enter a sentence below: ")
# # users_word = input ("Enter your sentence: ")
# answer = input(':>').split()
# answer[0] = answer[0].upper()

# print(f'Solution:\n{ " ".join(answer)}')


#Function
# def test_function() : 
#     print(4*2+2)

# test_function()

# def fun2 (n:int):
    
#     print(n**2)
#     return(fun2)

# fun2(4)

# print(fun2(4) ) 


# def fun3 (a,b,c):
#     print(a,b,c)

# fun3(1,2,3)
# fun3 (b=1, c=3, a=2)
# fun3 (1, b=3, c=2)

# def fun2 (n:int):
#     global result

#     result = n**2

#     return(result)

# fun2(4)

# print(result)

# print(fun2(4) ) 

# ClassworkWeek2
# def mean_function(n: int):
#     print(mean_number)
    
#     return(mean_function)

# mean_number = [1,2,3,4]
# number_lenght= len(mean_number)

# mean_count= sum(mean_number)
# mean_function= mean_count/number_lenght

# print(mean_function)

# print(number_lenght)


# def users_numbers (a,b,c,d):
     
#      users_number = int (input ("Enter your numbers: ") )
#      print(users_number)

#Classworktest2
# def mean_function(n: int):
#     print(mean_number)
    
#     return(mean_function)

# mean_number = input ("Enter your numbers: " :> ).split(",")
# number_lenght= len(mean_number)

# mean_count= sum(mean_number)
# mean_function= mean_count/number_lenght

# print(mean_function)

# print(number_lenght)

#desmondclasscorrection

# def mean (arr):
#     mean_value = sum(arr)/len(arr)
#     return round (mean_value, 2)

# print("Calculate the mean")
# print("Enter your number seperated by a comma: ")
# vals = input(" :> ").split(',')

# print (vals)
# mapped = list(map(int,vals))

# print(mean(mapped))

# print ('x')
# if 4>5:
#     print(7)

#     print(4)

# score = int (input("Enter your exam score: \n:>"))

# if score >= 100:

# if score >= 90:
#     print ('A')
# elif score >=80:
#     print("B")
# elif score >=70:
#     print("C")
# elif score>=60:
#     print("D")
# elif score >= 50:
#     print("E")
# elif score >= 40:
#     print("F")

# else: 
#     print("Comrade you no try")

# else:
#     print("Na harvard fit you")

#lambda
# my_str = "this is a lovely string"
# a = list(map(lambda f:f.upper(), my_str))
# print("".join(a))

import random

# a = [1,2,3,4,5,6,7]
# random.shuffle(a)
# print(a)

# a = [1,2,3,4,5,6,7]
# # random.shuffle
# b = random.sample(a,3)
# print(b)

# print("Guess the computer's choice to win the prize.")
# a = [1,2,3,4,5,6,7]
# print("Select a number from", a)
# # random.shuffle
# com_choice = random.choice(a)
# user = int(input("Your choice "))
# if user == com_choice:
#     print("You win")
# else: 
#     if user > com_choice:
#         print("Too High")
#     else:
#         print("Too Low")
#     print("You lose")

# print ("Play Rock Paper Scissors, Guess to win")

# a = ['R','P','S']

# print ("Pick a letter from", a)

# com_pick= random.choice(a)
# # random.shuffle(a)
# user_pick = input('Your choice:').lower()


# if user_pick == com_pick:
#     print('You draw')
# elif user_pick == a[0] and com_pick == a[1]:
#     print ("You loose")
# elif user_pick == a[1] and com_pick == a[0]:
#     print ('You win!')
# elif user_pick == a[1] and com_pick == a[2]:
#     print ('You lose!')
# elif user_pick == a[2] and com_pick == a[1]:
#     print ('You win!')
# elif user_pick == a[2] and com_pick == a[0]:
#     print ('You lose!')

# elif user_pick == 1 and com_pick== 0:
#     print ("You win")


# Desmondclassowrkcorrection


# a = ['R','P','S']

# print ("Pick a letter from", a)

# com_pick= random.choice(a)
# # random.shuffle(a)
# user_pick = input('Your choice:').lower()

# if user_pick == a[0] and com_pick == [2]:
#     print("You win!")
#     print("Computer choose", com_pick)
# elif user_pick == a[2] and com_pick == [1]:
#     print("You win!")
#     print("Computer choose", com_pick)
# elif user_pick == a[1] and com_pick == [0]:
#     print("You win!")
#     print("Computer choose", com_pick)
# elif user_pick == com_pick:
#     print("It's a tie")
# else: 
#     print("You lose")
#     print("Computer choose", com_pick)

#Loop is a way of going over a block of code as long as the condition is met.
#For loop goes over a block of code for either a period of time or for a range
#Range is a function that gives an number within two points.
#breakstatement instructs the loop to break the loop
#skipstatement instructs the loop to skip and continue the condition.

# for i in range(10):
#     if i ==5:
#         break
#     print(i)

# for i in range(10):
#     if i ==5:
#         continue
#     print(i)
# print(b)

# write a for loop to print all the odd numbers between 90 and 120

# for a in range(90,120):
#     if a % 2 == 1: 
#         print(a)
    
# #print all the multiples of 5 and 3

# print("")

# array = [1,2,3,4,15,22,21,33,50,55,72,66,95]

# for n in array:
#     if n % 5 ==0 or n % 3 ==0:
#         print(n)

#Write a function that takes in an integer and returns true or false if that number is a prime number.

# def is_prime(n):
#     i = 2

#     if n in (1,3):
#         return True
#     elif n == 2:
#         return False

#     while i <= n//2:
#         if n%i != 0:
#             return True
#         else:
#             return False
#         i+=1

# for x in range(1, 5):
#     print(x, '=', is_prime(x))

#Assignment
# num = int(input("Please enter a number to check if its prime : "))

# def primeNumber():
#     if (num <= 1):
#         return False

#     for i in range(2,num):
#         if(num % i == 0):
#             return False

#     return True

# if (primeNumber() == True):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# for i in range(10, 50, 5):
#     print(i)

# Import random

# a = ['R','P','S']
# trial = 3
# score = 0


# print ("Pick a letter from", a)

# com_pick= random.choice(a)
# # random.shuffle(a)
# user_pick = input('Your choice:').lower()

# if user_pick == a[0] and com_pick == [2]:
#     print("You win!")
#     print("Computer choose", com_pick)
#     trial +=2

# elif user_pick == a[2] and com_pick == [1]:
#     print("You win!")
#     print("Computer choose", com_pick)
#     trial +=2

# elif user_pick == a[1] and com_pick == [0]:
#     print("You win!")
#     print("Computer choose", com_pick)
#     trial +=2

# elif user_pick == com_pick:
#     print("It's a tie")
#     trial +=1
# else: 
#     print("You lose")
#     print("Computer choose", com_pick)
#     trial -=1

# Data Structure

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]

# a [2:5]

# b[3] = 82
# a[3] = 50

# print(b)
# print(a)


# a = [1,2,3,4,5,6,7]
# a [2:5]

# for x in a:
#     print(x)

# List comprehension

# a = [x**2 for x in range(10)]
# # a = [1,2,3,4,5,6,7,8,9]

# print(a)

# m = 0.728
# p = [1,2,4,7,8,9,10]

# c = [(i-m)**2 for i in p]

# print (c)
# sum(c)
# print (sum(c))

# In a range 


# a = [1,2,4,7,8,9,10]

# def oddnumber():
#     if ( a % 2 == 0 in range (10)):
#         replace(a, '0')

# print (a)  


num = int(input("Please enter a number to check if its prime : "))
    
primenum = [a for a in range (98,176)]
         
         if a <=1 and a % a == 0
return False

if primenum (num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



# def primeNumber(n):
#     if (n <= 1):
#         return False

#     for i in range(98,175):
#         if(n % i == 0):
#             return False

#     return True

# if primeNumber(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")