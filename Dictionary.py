# Create a dictionary and take input from the user and return meaning of the entered word from dictionary.

dmean={"N":"1","NO":"2","Num":"4","Nums":"3"}
print(dmean.get("N"))
print("Before remove",dmean)
dmean.pop("Nums")
print("After removed specific value",dmean)
dict=dmean.setdefault("Numb","1")
print("insert new key",dmean)
dmean.popitem()
print("delete last inserted key item",dmean)
dvalue=dmean.values()
print(dvalue)
dmean["NO"]=4 #when changes in dictionary values displayes as per updated values
print("After change value of NO Key",dmean)
