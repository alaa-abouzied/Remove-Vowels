str1 = input("Please Enter Your Own String : ")
vowels = ['a', 'e', 'o', 'i', 'u']
space = ""
for i in str1:
    if i in vowels:
        str1 = str1.replace(i, space)

print(str1)
