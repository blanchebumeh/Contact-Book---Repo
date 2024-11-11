import json

# Initialize an empty list to store contacts
my_contacts = []

# Function to add a contact
def add_contact():
    contact_name = input("Enter your name: ")
    contact_number = input("Enter your phone number: ")
    contact_email = input("Enter your email address: ")
    contact_age = input("Enter your age: ")
    contact_location = input("Enter your location: ")

    # Create a dictionary for the contact
    contact = {
        "name": contact_name,
        "number": contact_number,
        "email": contact_email,
        "age": contact_age,
        "location": contact_location
    }

    # Add the contact to the list
    my_contacts.append(contact)
    print("Your contact info has been successfully added.")

# Function to update a contact
def update_contact(contact_name):
    for contact in my_contacts:
        if contact["name"] == contact_name:
            contact["number"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email address: ")
            contact["age"] = input("Enter new age: ")
            contact["location"] = input("Enter new location: ")
            print(f"Contact {contact_name} updated.")
            return
    print(f"Contact {contact_name} not found.")

# Function to save contacts to a JSON file
def save_contacts_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(my_contacts, file, indent=4)
    print("Contacts have been saved to the file.")

# Function to load contacts from a JSON file
def load_contacts_from_file(filename):
    global my_contacts
    try:
        with open(filename, 'r') as file:
            my_contacts = json.load(file)
        print("Contacts have been loaded from the file.")
    except FileNotFoundError:
        print("File not found. Starting with an empty contact book.")

# Function to display all contacts
def display_contacts():
    if my_contacts:
        for contact in my_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['number']}, Email: {contact['email']}, Age: {contact['age']}, Location: {contact['location']}")
    else:
        print("No contacts found.")

# Function to delete a contact
def delete_contact(contact_name):
    global my_contacts
    my_contacts = [contact for contact in my_contacts if contact["name"] != contact_name]
    print(f"Contact {contact_name} deleted.")













