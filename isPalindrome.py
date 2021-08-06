from typing import List


strings ="racecar"


liststr = list()
for letter in strings:
    liststr += letter


liststr.reverse()

joined = "".join(liststr)



if joined == strings:
    print("is palindrome")
else:
    print("is not palindrome")




