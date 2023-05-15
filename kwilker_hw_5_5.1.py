import string



vc_dict = {}
def vs_counter(file):
    
    vowels = 0
    constonants = 0
    read = file.read()
    read = read.upper().replace(' ','')

    for e in read:
        if e.isalpha() == True:
            vc_dict[e.strip()] = read.count(e)
            continue
            
        else:
            continue


    for e in vc_dict.keys():
        if e == 'A':
            vowels = vowels + vc_dict[e]

        elif e == 'E':
            vowels = vowels + vc_dict[e]

        elif e == 'I':
            vowels = vowels + vc_dict[e]

        elif e == "O":
            vowels = vowels + vc_dict[e]

        elif e == "U":
            vowels = vowels + vc_dict[e]

        else:
            constonants = vowels + vc_dict[e]

    print("The constants and vowels:", vc_dict, "\n")

    return constonants, vowels
     

while True:
    try:
        user_input= input("Please Enter a textfile(without the ',txt'):")
        file = open(user_input + ".txt", 'r')


    except FileNotFoundError as e:
         print("""Sorry! No file was found (If you typed '.txt'
at the end of it, retype the file name without it) \n""")
         
         continue


        

    count_const, count_vowel = vs_counter(file)
    print("We are examining the text file:",user_input)
    print("Total # of vowels in the the textfile:", count_vowel)
    print("Total # of constonants in the textfile:", count_const)

    
    break
    






