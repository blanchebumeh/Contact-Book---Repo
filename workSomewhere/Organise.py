# I will use a Javascript Object notation (JSON) file to store my contacts.

import json
#Then will go ahead and initialize an empty list to store my contacts
 
my_contacts = []

#function to Add my contacts by prompting the user to enter an input.

def add_contact():
    contact_name = input("Enter your name: ")
    contact_number = int(input("Enter your phone number: "))
    contact_email_address = input("Enter your email adress: ")
    contact_age = input("Enter your age: ")
    contact_location = input("Enter your location: ")

# create a dictionary and Match contacts to name,phone number, and email address.
    contacts = {
            "contact_name": contact_name,
            "contact_number": contact_number,
            "contact_email": contact_email_address,
            "contact_age": contact_age,
            "contact_location": contact_location} #Add contacts to my list 
    my_contacts.append(contacts)
    print(f"Your Contact info has been successfully added: ")

# Function to save my contacts to JSON file

def save_contacts_to_file(contact.json):
    with open(filename, 'w') as file:
        json.dump(my_contacts, file, indent=4)
    print("Contacts have been saved to the file.")
















