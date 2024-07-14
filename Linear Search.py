values = [5,7,3,2,1,8,0]
found = False
search = int(input("What value are you looking for?"))
length = len(values)
for i in range(length):
    if values[i] == search:
        found =True
        print("found item at", i)
        break
if found == False:
    print("Item is not in list")
        