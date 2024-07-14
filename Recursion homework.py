
number = int(input("what si the number"))
def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number-1)
print(fact(number))