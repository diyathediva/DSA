values= [2,6,4,7,3,5,1,8,9,10]

length = len(values)

for y in range(length-1):
    swapped =False
    print("pass",y+1)
    for i in range(length-1):
        if values[i]<values[i+1]:
            temp = values[i]
            values[i] =values[i+1]  #in python you can swap variables by doing: a,b =b,a
            values[i+1] =temp
            swapped =True
        print(values)
    if swapped == False:
        break