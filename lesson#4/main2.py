print("Enter Marks Obtained in 4 subjects out of 100: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
computerscience = int(input("computerscience :"))

sum = math + english + science + computerscience
perc = (sum/400)*100

print(f"you gat {sum}/400 with {perc} %")
