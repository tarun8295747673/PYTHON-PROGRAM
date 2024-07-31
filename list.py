#in list we can store multiple types of value like (int. ,float, string, etc.)

marks = [97.5, 22.5, 78.32, 55.42, 42.3]
print(type(marks),"\n",marks)
print(len(marks))
print(marks[1])
print(marks[2])

# list are immutable

list = ["tarun",21, 12, 2003, "KUMAR"]
list[0]="TARUN" # this will change the zero index "tarun" value to "TARUN"
print(list)

# slicing is also possible in list
# [starting index : ending index]