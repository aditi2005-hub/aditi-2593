sentence = input("enter a sentence")

words = sentence.split()
word_count = len(words)

character= sentence.replace(" ",'')
character_count= len(character)



print(" the word count is ", word_count )
print("the character count is ",character_count)