def likes(names):
    
    other = len(names) - 2
    print(len(names))
    
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1]+ " and "+ names[2] + " like this"
    elif len(names) >= 4:
        return names[0] + ", " + names[1]+ " and " + str(other) + " others like this"
    
    


print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
print(likes(["jayson", "hello", "jacku", "blibk"]))
