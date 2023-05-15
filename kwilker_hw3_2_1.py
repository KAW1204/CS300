import math

START = 2
END = 130
even_count = 0
odd_count = 0
cube_count = 0
square_count = 0
square_list = []
cube_list = []

print("Printing numbers from ", START, "to", END)
for e in range(START, END+1):
    if (e % 2 == 0):
        even_count+= 1
        

    else:
        odd_count+= 1
        

    if (e ** 3 < END):
        cube_list.append(e ** 3)
        cube_count += 1

    if(e ** 2 < END):
         square_list.append(e ** 2)
         square_count += 1

print("Odd (",odd_count,"):",START+1, "...", END-1)
print("Even (",even_count,"):",START, "...", END)
print("Square (",square_count,")",square_list)
print("Cube (",cube_count,")",cube_list)
    
