string = input("please input your own word : ")

char = input("please input your own character : ")
count = 0

i = 0
while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("the total number of times ", char, " has occured = " , count)


