#WAP to check a person es eligible for driving license or not 
age = int(input("enter your's age :"))
if(age >= 18):
    print("you are eligible to apply for driving license")
else:
    print("not eligible")


#next program

age = 24
if (age < 18):
    print("you are minor")
elif (age>= 18 and age <50):
    print("you are an adult")
else:
    print("you are an senior")