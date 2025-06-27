# age = input("enter your age : ")

# if age >= "18":
#     print("you can vote")
# else:
#     print("you can not vote")

num = int(input("enter a num"))

if num % 2 == 0:
    print(f"{num} is even num ")
else:
    print(f"{num} is odd num")


answer = input("1) when was the first use of the word 'quiz'?")
if answer == "1781":
    print("correct!")
else:
    print(f"the answer is '1781' , not '{answer}' ")

answer = input("2) which built-in fuction can get iformation from the user? ")
if answer == "input":
    print("correct!")
else:
    print(f"the answer is 'input' , not {answer!r}")


costprice = int(input("enter the cp: "))

sellingprice = int(input("enter the sp"))

if(sellingprice > costprice):
    print("profit")
    totalprofit = sellingprice - costprice
    print(totalprofit)
else :
    print("no profit")



number = int(input("enter any number: "))
if number > 0:
    if number % 2 == 0:
        print("possitive even number")
    else:
        print("possitive odd number")
else:
    print("not a possitive number")
