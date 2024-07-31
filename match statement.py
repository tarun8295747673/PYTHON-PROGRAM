day = int(input("enter the number :"))
match day:
    case 1:
        print("the day in monday")
    case 2:
        print("the day is tuesday")
    case 3:
        print("the day is wednesday")
    case 4:
        print("the day is thursday")
    case 5:
        print("the day is friday")
    case 6:
        print("the day is saturday")
    case 7:
        print("the day is sunday")
    case _:
        print("holiday")
