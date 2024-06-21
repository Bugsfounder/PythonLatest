dict = {}
frndName1 = input("Enter Your Name:")
frndLanguage1 = input("Enter Your Language:")
frndName2 = input("Enter Your Name:")
frndLanguage2 = input("Enter Your Language:")
frndName3 = input("Enter Your Name:")
frndLanguage3 = input("Enter Your Language:")
frndName4 = input("Enter Your Name:")
frndLanguage4 = input("Enter Your Language:")

dict.update(
    {
        frndName1: frndLanguage1,
        frndName2: frndLanguage2,
        frndName3: frndLanguage3,
        frndName4: frndLanguage4,
    }
)
print(dict)

# 7. If the names of 2 friends are same; what will happen to the program in problem
# 6?
# if the name of two friends are same then the second name's value is updated the first same name's value.

# 8. If languages of two friends are same; what will happen to the program in problem
# 6?
#  Nothing, it works perfectly it insert language with the respective name.
