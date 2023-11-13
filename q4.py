class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Address Book is empty.")
        else:
            print("Contacts in the Address Book:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"Contact {index}:")
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print()

# Creating an AddressBook instance
address_book = AddressBook()

# Adding contacts to the address book
contact1 = Contact("Alice", "1234567890", "alice@email.com")
contact2 = Contact("Bob", "9876543210", "bob@email.com")
contact3 = Contact("Charlie", "4561237890", "charlie@email.com")

address_book.add_contact(contact1)
address_book.add_contact(contact2)
address_book.add_contact(contact3)

# Displaying the contacts in the address book
address_book.display_contacts()
