num = 10
num_float = float(num)
print("Integer to float:", num_float) # Output: 10.0

#Float to integer
num2 = 20
num_int = int(num2)
print("Float to integer :", num_int) # Output:20

#String to integrer (if the string contains a number)
num_str = "15"
num_from_str = int(num_str)
print("String to integer:", num_from_str + 15)

# Integer to string
num3 = 100
num_str3 = str(num3)
print("Integer to string:", num_str3 + "100") 

str1 = "hi"
str2 = "world"
combined = str1 + " " + str2
print("Concentrated string:", combined)

repeated = str1 * 3
print("Repeated string:", repeated)

slice_str = combined[0:5]
print("Sliced string:", slice_str)

upper_str = str1.upper()
print("Upper case string:", upper_str)

lower_str = str1.lower()
print("Lower case string:", lower_str)

print("Length of combined string:", len(combined))

str1 = "will"
str2 = " i am"
combined = str1 + " " + str2
print("Concentrated string:", combined)

repeated = str1 * 3
print("Repeated string:", repeated)

slice_str = combined[0:5]
print("Sliced string:", slice_str)

upper_str = str1.upper()
print("Upper case string:", upper_str)

lower_str = str1.lower()
print("Lower case string:", lower_str)

print("Length of combined string:", len(combined))