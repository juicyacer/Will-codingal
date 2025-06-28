print("select your ride")
print("1. bike")
print("2. car")

choice = int(input("enter your choice"))

if( choice == 1 ):
    print(" what type of bike? " )
    print("1.scooty\n")
    print("2.scooter\n")

    choice2 = int(input("enter your choice2: "))
    if choice2 == 1:
        print("youhave selected scooty")
    else:
        print("you have selected scooter")

elif( choice == 2 ):
    print( "what type of car?" )
    print("1.sedan")
    print("2.xuv")

    choice3 = int(input("enter your choice3: "))
    if choice3 == 1:
            print("you have selected sedan")
    else:
            print("you have selected xuv")

else:
    print("wrong choice")


medical_cause = input("did you have a medical cause Y or N: ")

atten = int(input("enter the attendance of the student: "))

if medical_cause == 'Y':
     print(" you are allowed")
else:
     if atten>=75:
        print ("allowed")
     else:
        print ("not allowed")
        