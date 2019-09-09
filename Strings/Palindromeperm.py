def palindrome(string):
    dict = {}
    string = string.lower()
    for char in string:
        if char == " ":
            pass
        elif char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    values = dict.values()
    middle = False
    for value in values:
        if value % 2 == 1:
            if not middle:
                middle = True
            else:
                return False
    return True


print(palindrome("racerac"))
