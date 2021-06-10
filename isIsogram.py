
 
def is_isogram(string):
    arr = []
    string = string.lower()
    print(arr)
    for i in string:
        if i != arr:
            if i in arr:
                return False
            arr.append(i)
            print(arr)
    return True




print(is_isogram("helo"))









# def is_isogram(string):
#     string = string.lower()
#     for char in string:
#         if string.count(char) > 1:
#             return False
#     return True




