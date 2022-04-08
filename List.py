list1=["kartik","krunal","rushi","Ram","Vansh","krunal"]
list2=(1,4,5,9)
list1.append("Jogi")
print("Append method",list1)
list1.remove("kartik")
# list1.clear()
print("After remove Method",list1)
# list1.extend(list2)
# print("After Extend Method",list1) #add another list to the last
list1.pop(2) #remove value from specific position
print("After Pop Method",list1)
list1.reverse()
print("After reverese",list1)
count1=list1.count("krunal")
print("Count Method", count1)


