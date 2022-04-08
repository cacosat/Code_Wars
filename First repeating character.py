#Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

#For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

#As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

#If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.


def first_non_repeating_letter(string):
    string1 = string.lower()
    if string1 == "":
        return ""
    else:
        dictionary = {x:0 for x in string1}
        for char in string1:
            if char in dictionary:
                dictionary[char] += 1
        if 1 not in list(dictionary.values()):
            return ""
        else:
            char = list(dictionary.keys())[list(dictionary.values()).index(1)]
            if char not in string:
                return char.upper()
            else:
                return char


print(first_non_repeating_letter("streSS"))
print("hoola".count("o"))