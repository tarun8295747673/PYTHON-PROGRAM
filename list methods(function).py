# list = [1,2,3]
# list.append(4) # adds one element at the end  [1,2,3,4]
# list.sort() #sort in ascending order  [1,2,3]
# list.sort(reverse=True) # sort in descending order [3,2,1]
# list.reverse() # reverse list  [3,2,1]
# list.insert(idx,el) # insert element at index


list = [2,4,3,2,5,6]
list.append(9)
print(list)

list1 = [2,4,3,2,5,6]
list1.sort()
print(list1)

list2 = [2,4,3,2,5,6]
list2.sort(reverse=True)
print(list2)

list3 = [2,4,3,2,5,6]
list3.reverse()
print(list3)

list4 = [2,4,3,2,5,6]
list4.insert(2,7)
print(list4)