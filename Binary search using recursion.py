values = [2,5,4,7,6,5,8,1,9,0]
values.sort()
print(values)
finalval = int(input("What value are you looking for?"))
low = 0
high = len(values) -1
def binarysearch(values, finalval,low,high):
    if high >= low:
        mid = (high + low) // 2
        if values[mid] == finalval:
            return mid
        elif values[mid] > finalval:
            return binarysearch(values,finalval,low,mid-1)
        elif values[mid] < finalval:
            return binarysearch(values,finalval,mid+1,high)

    else:
        print("value not found")
print(binarysearch(values,finalval,low,high))