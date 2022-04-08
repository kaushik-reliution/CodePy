# sets method practice
elmnt={"Pruthvi","Agni","Vayu","Akash","Air","Shunya"}
pos={"Jagrut","Shushupta","Turi","Shunya","Agni"}
print("Set display",elmnt)
print("Set Display2",pos)
elmnt.add("Shunya")
print("After add new value",elmnt)
# diff=elmnt.difference(pos)
# print("Diffrence",diff)
# elmnt.difference_update(pos)
# print(elmnt)
pos.discard("Agni")#remove specific item
match=elmnt.intersection(pos)
print("After intersection",match)
smtrc=elmnt.symmetric_difference(pos)
print("A-B(symmetric)",smtrc)
unin=elmnt.union(pos)
print("A U B",unin)


