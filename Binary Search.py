values = [2,5,4,7,6,5,8,1,9,0]

values.sort()
print(values)
found =False
finalval = int(input("What value are you looking for?"))
low = 0
high = len(values) -1
while low <= high:
    mid = (low + high)//2
    print(mid,values[mid])
    if values[mid] == finalval:
        found =True
        print("Item was found at" ,mid)
        break
    elif finalval < values[mid]:
        high = mid -1
    elif finalval> values[mid]:
        low = mid +1
if found == False:
    print("item not found")        

