#Emily Wawrzyniak, Yao Hua He, Itzel Garza, Emily Hernandez
#1. ask for peice of text 
userText = input(" Enter any text you please:")
#2. ask for 3 letter
firstLetter =input(" Enter the first letter : ")
secondLetter = input('Now enter the second letter: ')
thirdLetter =input('Finally, enter the last letter')

letterValue = [firstLetter, secondLetter, thirdLetter]
#3. convert string to lowercase
userText.lower()
letters= [firstLetter.lower(), secondLetter.lower(), thirdLetter.lower()]

#4. Convert string to list 
listofWords = userText.split()

#5. print out word count (how many objects are in list 
wordCount= len(listofWords)
print(f"The word count is {wordCount} words")

#6. invert list of words
backwardsList =list(reversed(listofWords))

#7. join list using spaces 
print(" ".join(backwardsList))
      
#8. create boolean asking of "python" is in list of words 
pythonIncluded= ('python')

if pythonIncluded in listofWords:
    print('"Python" is found in your text')

#9. Make list into bigger list using ech letter
listofLetters =list(userText.lower())

#10. Find first and last letter of the list 
firstL = [listofLetters[0]]
lastL = [listofLetters[-1]]
print (f'The first letter of the list is  {firstL},  and the last letter is {lastL}')
#11. Print how many times the letter is found in the text 
total1Letter= listofLetters.count(firstLetter)
total2Letter= listofLetters.count(secondLetter)
total3Letter= listofLetters.count(thirdLetter)



choseLetters = { "inputs": { firstLetter: str(total1Letter), secondLetter: str(total2Letter), thirdLetter: str(total3Letter), } } 
# Printing the occurrences of each letter for letter, 
for letter, count in choseLetters["inputs"].items(): 
    print(f'There are {count} occurrences of the letter "{letter}" in the text.')