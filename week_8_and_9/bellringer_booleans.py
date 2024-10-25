# 1 
favLang = input("What is your favorite programming language?")
if favLang == 'python': 
    print('You love python!')
else:
    print('Diffrent choice')

# 2 
grade = int(input('What grade is being innputted?'))
if grade >= 90:
    print('the grade is a an A')
elif grade >= 80 and grade < 90:
    print('he grade is a b')
elif grade >= 70 and grade < 80:
    print ('the grade is a c')
elif grade >= 60 and grade < 70:
    print('the grade is a d')
else:
    print ('the grade is a f')


# 3 
user="Admin"
logged_in= True

if user == "Admin" and logged_in :
    print("Welcome admin!")

else :
    print("Log in")

# 4

list1= [1, 2, 3, 4]
list2= [1, 2, 3, 4]

if list1 == list2:
    print ('The lists have the same value')
else: 
    print('the have diffrent values')

if list1 is list2:
    print ('They have the same object in memory ')
else: 
    print('they have diffrent objects in memory ')

#EMILY HERNANDEZ


