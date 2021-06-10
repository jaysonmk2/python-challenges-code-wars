def high_and_low(numbers):
    string =""
    mapse=list() 
    numbers = numbers.split()
    for number in numbers:
        mapse.append(int(number))

    string = str(max(mapse))  + " " +  str(min(mapse))
    print(string)
    return string



high_and_low("2375 982 583 1477 2789 1553 1186 1306 2676 414 2870 -163 811 70 2677 2476 324 2519 1477 2687 -137 2602")