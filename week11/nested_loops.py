# nested loops = A loop within another loop (outer,inner)
#               outer loop :
#                   inner loop:

rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
symbol=input("Enter a symbol to use: ")

for x in range(rows): #repeats 3 times
    for x in range(columns): #1 is inclusive while 10 is exclusive
         print(symbol, end="") # puts numbers in one line
    print()

