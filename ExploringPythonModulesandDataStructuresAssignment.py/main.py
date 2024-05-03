import contact_managers
contacts = []

main_menu = ""
while main_menu != 'quit':

    main_menu = input('''Menu
    1. add
    2. delete
    3. view
    4. quit
    Please select an option: ''')


    if main_menu == 'add':
        name = input('Please enter a name: ')
        number = input('Please enter a phone number: ')
        contact_managers.add_contact(contacts, name, number)
    elif main_menu == 'delete':
        name = input("please enter the name of the contact you wish to delete: ")
        contact_managers.delete_contact(contacts, name)
    elif main_menu == 'view':
        contact_managers.view_contacts(contacts)