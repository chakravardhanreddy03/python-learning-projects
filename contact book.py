contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    name = input("Enter name to search: ")

    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True

    if not found:
        print("Contact not found.")
    print()


def update_contact():
    name = input("Enter name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            new_phone = input("Enter new phone number: ")
            contact["phone"] = new_phone
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


def menu():
    while True:
        print("===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()