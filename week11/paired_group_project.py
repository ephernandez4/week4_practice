

# #problem 1
while True:
    grade=int(input('Enter a grade :'))               #ASK USER FOR A GRADE NUMBER                                      #while loop 
    if grade >= 90 and grade<= 100:                 #CHOOSE A RANGE TO CHOOSE WHAT IS PRINTED OUT
         print("excellent ")
    elif grade >= 70 and grade <= 89:                #if 70-89 print GOOD
         print('good')

    elif grade >= 50 and grade <= 69:                #if 50-69 print PASS
         print('pass')
     
    elif grade < 50 and grade > 0:                                   #if <50 print fail 
         print('fail')
    elif grade <0:
        print("you entered a negitve number. goodbye")
        break
grade =int(input('enter a list of student scores '))

#problem 2

number=int(input('Enter a number:')) # ask a user for a number 

for number in range(1,21):  # range 
    if number %2 ==0 and number >=10: # condtion 
        print('special even')        # result of condtion
    else:
        print('special odd')          #result of condtion 











        