"""
Kenyon Wilkerson
Class: 521 - Fall 1
Date: 10/21/21
Homework Problem: #2.1
Summary: Print a calculation and manipulate the output so that
it repeats itself 3 times and add the 3 outputs together
then divide the two"""


user_input = int(input("Enter a number from 1 to 9")) 

calculation = int((((user_input * 2) + 10 )/ 2) - user_input)

print(calculation) #Prints first calculation
                   
calc_string = str(user_input)

 


calc_string3 = calc_string * 3

print(calc_string3) #prints the input 3 times


p = 0
for e in calc_string3:
    e = int(e)
    p = e + p



calc_string3 = int(calc_string3)

calculation_2 = (calc_string3 / p) 

calculation2_int = int(calculation_2)

print(calculation2_int)




    
