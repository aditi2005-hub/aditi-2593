# write a program to detect double spaces in a string
#replace the double spaces from problem with single spaces
#wap to format the following letter using escape sequence characters
letter = "dear  Students, This python course is going well. Thanks"
print(letter.find("  "))
replaced = letter.replace("  "," ")
print(replaced)
letter = "Dear Students,\n\t\tThis python course is going well.\nThanks!"
print(letter)