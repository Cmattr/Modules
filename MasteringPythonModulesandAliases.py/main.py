import text_utils

string = str(input("please input a string: "))

menu = ""
while menu != 4:
    print(f"\nPlease select a function for {string}")
    menu = input('''    1. print string in upper case
    2. Print string in lower case
    3. Reverse string
    4. quit
    Make a selection by number: ''')

    if menu == '1':
        text_utils.capitalizing_string(string)
    elif menu == '2':
        text_utils.lower_string(string)
    elif menu == '3':
        text_utils.reverse_string(string)
    else:
        break
    
        