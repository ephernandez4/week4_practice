##################################### String Methods#################################

#uppercase methog in python
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper()) #prints sentence in uppercase

sentence2 = "ESPN IS THE BEST SPORTS NETWORK"
print(sentence2.lower()) #prints sentence in lowercase
print(sentence.find("communications")) #prints the index of the word communications
#uppercase the word communication
print(sentence.replace("communications", "COMMUNICATIONS")) #prints communications in uppercase
#use slicing method
print(sentence[25:36].upper()) #prints communication in uppercase

print(sentence.replace("communications", "COMMUNICATIONS"))
#upper method
print(sentence.replace ("communications", "communications".upper()))

# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper()) 
#prints sentence in uppercase
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]
word_list={"Simple", " is", " better", " than" " complex."}
print(word_list)
# String Methods Practice #3
# Replace in the following sentence:
new_sentence ="If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
print(new_sentence.replace("hard", "easy"))
print(new_sentence.replace("bad", "good"))
# "bad" --> "good"
# and display the sentence with both words modified.
modified_sentence =new_sentence.replace("hard", "easy").replace("bad", "good")
#################################string properties################################

#join method
word_list={"Simple", " is", " better", " than" " complex."}
print(word_list)
joined_sentence=" ".join(word_list)
print(joined_sentence)
new_word_list = ["apple", "banana", "mango", "cherry", "watermelon"]
joined_sentence2 =" 🍎🍌🍋🍒🍉".join(new_word_list) #window semicolon
print(joined_sentence2)

#split method
sentence4="I am a python programmer"
print(sentence4.split())#splits the sentence into a list of words
# by default this method splits the sentence by commas 
print(sentence4.split(",")) #splits sentence into a list of words using seperator
#this prints out as ["I am a programmer"]

print(sentence4.split("a")) #splits the sentence into a list of words using seperators
#takes out the a
print(sentence4.split("p")) 

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
result="Repitition" * 15
print(result)

#find the first paragraph in the declaration of idependence
first_paragraph ="We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable rights, that among these are life, liberty, and the pursuit of happiness. That, to secure these rights, governments are instituted among men, deriving their just powers from the consent of the governed. That, whenever any form of government becomes destructive of these ends, it is the right of the people to alter or to abolish it, and to institute new government, laying its foundation on such principles, and organizing its powers in such form, as to them shall seem most likely to effect their safety and happiness."
#place it in a variable called "first_paragraph"
#replace the word "people" with "citizens" in the paragraph
print(first_paragraph.replace("people", "citizens").replace(" ", ",").replace(",","🥪"))
#print the first paragraph with the word people replaced with citizens
#remove all spaces, replace commas with emojis

# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
richsentence=print("Whitecaps on the bay. A broken signboard banging. In the April wind. — Richard Wright, collected in Haiku: This Other World, 1998")
richsentence = False # this is a boolean data type
print(richsentence)
# — Richard Wright, collected in Haiku: This Other World, 1998

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
words="electroencephalographist"
print(len(words))