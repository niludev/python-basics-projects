# practical Programming Practises
# Extracting Alpha Bravo message using string manipulation and hash tables.

#MAYDAY!

string = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"
elements = string.split(" ")
# print(elements)

def print_string_from_list (s):
    print(''.join(s))

dictionary = {
    "Zero": "0",
    "One": "1",
    "Three": "3",
    "Four": "4",
    "Seven": "7",
    "Dash": "-"
}


passWort = []
for elem in elements:
    print(dictionary.get(elem, elem[0]), end="")

    """ if elem in dictionary:
        passWort.append(dictionary[elem])
    else:
        c = elem[0]
        passWort.append(c) """

""" print(passWort)
print_string_from_list (passWort) """

print()