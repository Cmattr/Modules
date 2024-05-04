
def add_contact(contacts, name, number, email):
    new_contact = {
           "phone": number,
           "email": email}
    contacts[name] = new_contact
    print(f"\n new contact for {name} added\n ")

def delete_contact(contacts, name):
    contacts.pop(name)
    print (f"\n{name} has been removed from your contacts\n")


                 

def view_contacts(contacts):
    for key, value in contacts.items():
        print(f"\n contact: {key, value} \n")

