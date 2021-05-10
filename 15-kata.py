def lessthan(a,b):
    if a < b:
        print(str(a) + " is less than " + str(b))
    elif b < a:
        print(str(b) + " is less than " + str(a))
    else:
        print(str(a) + " and " + str(b) + " are equals")

lessthan(5,8)
lessthan(10,4)
lessthan(20,20)
