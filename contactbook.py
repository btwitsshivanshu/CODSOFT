contacts = []

def add_contact(name, phone, email, address):
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact(search_term):
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if not results:
        print("No contacts found.")
    else:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(name, new_phone=None, new_email=None, new_address=None):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print(f"Contact {name} updated.")
            return
    print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} deleted.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone number (or press enter to skip): ")
            email = input("Enter new email (or press enter to skip): ")
            address = input("Enter new address (or press enter to skip): ")
            update_contact(name, phone or None, email or None, address or None)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
