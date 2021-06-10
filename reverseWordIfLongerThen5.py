

def isLonger(string):
    count = 0
    for letter in string:
        count = count + 1
        

    if count >= 5:
        return True
    
    return False

def spin_words(sentence):
    count = int(0)
    sentence = sentence.split()
    for word in sentence:
        if isLonger(word):
            listW = list(word)
            listW.reverse()
            print(listW)
            print(count)
            sentence[count] = "".join(list(listW))
        count = count + 1

    string = " "
    print(string.join(sentence))
            
    return string


print(spin_words("more one more snruter or dedulcni"))






