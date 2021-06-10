


def list(number):
    count = int(0)
    for i in number:
        if type(i) == str:
            print(i + "is a string")
            print("and the count = " + str(count) )
            del number[count]
        count = count + 1
    return number




print(list(["hellloooooo",1,"yo", 50, "jijijij"]))