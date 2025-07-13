# take a secret word as input (withot spaces),
# then encode the word using a custom cypher
# replace all the vowels with *
# reverse the entire SyntaxWarningthen shift each letter 2 places ahead in the alphabet (wrap around if needed , eg. y=a, b=z)
# print the resulting encoded word


L1 = [1, 8, 7, 2, 15,20]

# L1.sort()
# print(L1)

# L1.reverse()
# print(L1)

# L1.append(21)
# print(L1)

# L1.insert(4,26)
# print(L1)

# L1.pop()
# print(L1)

#L1.pop(2) ----------remove index
# print(L1)


# L1.remove(7)----------remove value
# print(L1)

#wap to store seven fruits in a list entered by the user
#wap to accept marks of 6 students and dispaly them in a sorted manner
#wap to sum a list with 4 numbers.

# fruits=[]
# for i in range (1,7):
#   i<=7
#   a =input('enter a fruit: ')
#   fruits.append(a)
# a+=a

#print('list of fruits:' ,fruits)

# marks = []
# for i in range (1,7):

#   a = input('enter your marks:')
#   marks.append(a)
#   marks.sort()
# print(marks)

numbers= []
for i in range(4):
  num = int(input('enter a number:'))
  numbers.append(num)

total = sum(numbers)
print('the total is:', total)