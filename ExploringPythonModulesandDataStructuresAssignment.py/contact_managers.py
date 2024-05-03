
def add_contact(contacts, name, number):
    contacts.append({"name": name, "number": number})
    print(contacts)

def delete_contact(contacts, name):
    for  contact in contacts:
        contact = name
        print('1')
        remove = contacts.pop({contact})
        print('2')
        print(remove)


                 

def view_contacts(contacts):
    print(contacts)

