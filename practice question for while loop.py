# practice question for "while loop"
# 1. print number from 1 to 100

num1 = 1
while num1 <= 100:
    print(num1)
    num1 += 1

# 2. print number from 100 to 1

num2 = 100
while num2 >= 1:
    print(num2)
    num2 -= 1

#print a multiplication table of number n.

num3 = 1
while num3 <= 10:
    print(num3 * 3)
    num3 +=1


# print the element of the following list using a loop
lis = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(lis):
    print(lis[idx])
    idx += 1

# search a number x in this tuple using loop
t = (1,4,9,16,25,36,49,64,81,100)
x = 81
i = 0
while i < len(t):
    if(t[i] == x):
        print("found")
    else:
        print("not found")

    i+=1
