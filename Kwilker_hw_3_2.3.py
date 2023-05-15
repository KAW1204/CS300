correct_input = False

while (correct_input == False):
    user_input = input("Please enter an 3 digit integer in ascending order")
    if (user_input.isdigit() == False ):
        print("This is not an integer please reeneter")
        continue

    user_input = user_input.replace(".","")
    input_count = len(user_input)
    
    if (input_count <= 3):
        
         for e in range(1,len(user_input)):
             
                 
        
            if (user_input[e] > user_input[e-1]):

                 if (e == input_count-1):
                     
                    correct_input = True
                    print("This is the correct input")
                    break
             
            elif(user_input[e] == user_input[e-1]):
                print("Your number contains a duplication")
                break
            
            
            elif(user_input[e] < user_input[e-1]):
                print("Your number is not in ascending order")
                break



    else:
        print("Error: You did not enter a 3-digit number")
        
   

   
    
        
        
    
        
    

    
