# print the element of the following list using a loop
num = [1,4,9,16,25,36,49,64,81,100]
for li in num:
    print(li)



#search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

y = (1,4,9,16,25,36,49,64,81,100)
x = 36
idx = 0
for el in y:
    if(el==x):
        print("x found")
        idx+=1
    else:
        print("not found")

# print the table of 4 using for loop
idx = 0
for x in range(0,41,4):
    print("4*",idx,"=",x)
    idx +=1


# print no. from 100 to 1

for x in range(100,1,-1):
    
    print(x)
   