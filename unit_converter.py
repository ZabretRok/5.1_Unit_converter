print ("Hello! I am your unit converter. My speciality is to convert kilometers into miles. ")

while True:
    kilometers = float(input("Please, enter number of kilometers, to convert them into miles! "))
    miles = round( kilometers * 0.6213, 4)
    print (f"{kilometers} kilometer(s) is {miles} mile(s). ")

    answer = input("Do you want to do another conversion? (Y/N) ")
    if answer.lower() != "y" :
        print ("Ok, see you soon! ")
        break

