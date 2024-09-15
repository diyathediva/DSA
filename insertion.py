data = ['t','b','a','c','e','o','q',]

length = len(data)

for i in range(length-1):
    currentitem = data[i]
    position = i - 1
    while position>= 0 and currentitem<data[position]:
        data[position +1] = data[position]
        position = position -1
    data[position +1] = currentitem
    print(data)   
    