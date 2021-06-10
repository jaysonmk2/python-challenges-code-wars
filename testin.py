def square_digits(num):
    
    num = str(num)
    string = ""
    print(num)
    for n in num:
        num=int(n)**2
        print(num)
        string = string + str(num)
    
    print(string)
    return num
    

print(square_digits(431111))