#while loops = execute come code WHILE some condition remains true

#while loops and for loops
#are forms of iteration
#iteration is the process of 
#repeating or looping through
#a set of steps or instructions
#to iterate it the verb
#form of iteration
#be careful of infinite loops
#they will crash your program
#and you will have to restart
#infinite loops are loops that never end

############################################# WHILE LOOPS #######################################################

# name = input("Enter your name: ") #while loop

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

###############################################

# while name == "":
#     print("You did not enter your name") #infinite loop

################################################
# age=int(input("Enter your Age : "))

# while age < 0:
#     print("Age can't be negative")
#     age=int(input("Enter you Age: "))

# print(f"You are {age} years old")

###############################################

# food=input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food=input("Enter another food you like (q to quit): ")

# print("bye!")

################################################

# num=int(input("Enter a number between 1-10: "))

# while num < 1 or num > 10 :
#     print(f"{num} is not valid")
#     num=int(input("Enter a number between 1-10: "))

# print(f"Your number is {num}")

################################################ FOR LOOPS ###########################################################
#for loops =  execute a block of code a fixed number of times
#               You can iterate over a range, string, sequence, etc.

# for x in range(1, 11): #last number is exclusive
#     print(x) #a lift of items

# for x in reversed(range(1, 11)): #reversed numbers
#     print(x)


# print("HAPPY NEW YEARS!!!")

# for x in reversed(range(1, 11, 2)): #count by 2s
#     print(x)


# credit_card="1234-5678-1234-5678"

# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13 or x == 15:
#         continue #skips over the number (ex: 13))
#     else:
#         print(x)

# for x in range(1, 21):
#      if x == 13:
#           break #ends at 13
#      else:
#           print(x)

############################################# CHALLENGES ###############################################
horror_movies=["The Exorcist", "The Shining", "The Conjuring", "The Ring"]
# loop through the list of horror movies
# if the name is "The Shining" print "The Shining"
# otherwise, print "The Shining was not found!" and print
# out the other names using a loop


for movies in horror_movies:
     if movies == "The Shining":
         print("The Shining is found!")
         print(movies)
     else:
         print("The Shining is not found.")
         print(movies)


#2 create a list of your favorite horror movie chracters 
# loop through the list of chracters
# if the name is "Freddy Krueger", skip over it
# otherwise, print out the name of the chracter
        
horror_movie_chracters=["Scream", "Freddy Krueger", "It Clown", "Megan"]

for chracters in horror_movie_chracters :
        if chracters == "Freddy Krueger":
            continue
        else:
            print(chracters)

#3 create a list of yout favorite horror movie monsters
# loop through the list of names
# if the name is for example "swamp thing", replace it with another name
            
horror_movie_monsters=["swamp thing", 'other mother','killer klowns','chucky','dracula','myers']

for monster in horror_movie_monsters :
    if monster== 'swamp monster':
         horror_movie_monsters[0]= "Pennywise"
         print(horror_movie_monsters)
    else:
        print (monster)
