


def decendingOrder(num):
    
    list = []

    #adding a loop so i can go through the number
    #also making the num a string because python will not loop through int
    for i in str(num):

        #adding each value i loop through to a list
        list.append(int(i))
        
    print(list)

    #we added the values into a list so that we can use the sort and reverse methods

    #sort it to go from smallest number to biggest
    list.sort()
    print("this is the sorted list" + str(list))

    #then we simply just reverse the ordered list 
    list.reverse()
    print("this is the output list" + str(list))



    decendingString = str()

    # here we go through another loop that converts all the values of the list into a string
    for j in list:

        #here we concatinate the current value of the loop with the string variable we declared above
        decendingString = decendingString + str(j)

    print(decendingString)

    return decendingString



decending = decendingOrder("15")

print("result is ")
print(decending)