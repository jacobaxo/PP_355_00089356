import random 

number_of_dials = int(input("Each lock has how many dials: "))

how_many_to_list = int(input("How many combinations would you like: "))

get_number = print(random.uniform(100, number_of_dials))



#this code was suppose to pick a number in the right range but it does not do it correctly so i deleted it
if number_of_dials == 3:
    print(random.randrange(0,999))
if number_of_dials == 4:
    print(random.randrange(0,9999))
if number_of_dials == 5:
    print(random.randrange(0,99999))
if number_of_dials == 6:
    print(random.randrange(0,999999))
if number_of_dials == 7:
    print(random.randrange(0,9999999))
if number_of_dials == 8:
    print(random.randrange(0,99999999))
if number_of_dials == 9:
    print(random.randrange(0,999999999))

#this does not work



print("-------------------------------------------")

print(f"Number ")