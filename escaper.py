def escaping(string):
    characters = ('_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!')
    print("".join(["\\" + char if char in characters else char for char in string]))


string = """

Українські групи в фб:
https://www.facebook.com/groups/Ukrainians.in.Ireland
https://www.facebook.com/groups/787279257984036 
https://www.facebook.com/groups/151187490507560 

"""


escaping(string)