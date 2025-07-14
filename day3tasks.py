# 1. Take a number from the user and print whether it's even or odd.
# num = int(input("give a number"))

# if num % 2 == 0:
#   print("the number is even.")
# else:
#   print("the number is odd")

 # 2. Write a program to count the number of vowels in a given string.
# str = input("write a text: ")
# str_r = str.replace(" ","")
# vowels = "AEIOUaeiou"

# vowels_found = [char for char in str if char in vowels]

# print("the found vowels are:", vowels_found)
# 3. Ask the user to input a sentence and print the number of words in it.
# sen= input("write a sentence: ")
# sen= sen.split()
# numb_of_words=len(sen)
# print('the number of words are ', numb_of_words)

# 4. Take a number from the user and print its multiplication table from 1 to 10 using a function.
# def mul(number):
#   for i in range(11):
#     print(f"{number} * {i} = {number * i}")
# num= int(input("which number's multiplication do you want?: "))
   
# mul(num)  
# 5. Write a program to accept 5 numbers from the user, store them in a list, and print the maximum and minimum values.
# numbers = []
# for i in range(5):
#   num = int(input(f"enter number {i+1} :"))
#   numbers.append(num)
# print(numbers)
# max_number= max(numbers)
# min_number = min(numbers)
# print(f"the max numb is {max_number} and the min numb is {min_number}")
# print(f"the average number is  {sum(numbers) / len(numbers)}")
#Accept a string and check whether it is a palindrome or not (same forward and backward).
# def palindrome_checker(str):
#   str= input("write a text")
#   str= str.lower()
#   str= str.replace(" ","")
#   if str == str[::-1]:
#     print("its a palindrome")
#   else:
#     print("not a palindrome")

# palindrome_checker(str)

#Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break)
# import random
# secret_numb = random.randint(1,10)

# while True:
#   guess=int(input("guess a number from 1 to 10 : "))
#   if guess==secret_numb:
#     print("congrats you guessed it right")
#     break
#   else:
#     print("oops, guess again")
# Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.

  
