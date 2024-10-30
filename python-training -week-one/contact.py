#I will use a Javascript Object notation (JSON) file to store my contacts.
import json

#Then create a function to load my contacts from my file
my_contacts = []

# Save the contacts to a file (e.g., a text file) and load them when the program starts.

def save_contact():
    contact_name = input("Enter your name: ")
    contact_phone_number = input("Enter your phone number: ")
    contact_email_adress = input("Enter your email adress: ")
    contact_age = input("Enter your age: ")
    contact_location = input("Enter your location: ")

#2 Each contact should have a name, phone number, and email address.
#3 Use lists or dictionaries to store contacts.

    contact = {
            "contact_name": contact_name,
            "contact_phone_number": contact_phone_number,
            "contact_email": contact_email_adress,
            "contact_age": contact_age,
            "contact_location": contact_location
        }
    contact.append(my_contacts)
    print(f"Your Contact info has been successfully save: ")

def main():
    print("starting application")
    save_contact()

if __name__  == "__main__":
    main()

# Implement input validation (e.g., ensuring a valid email address format).
# Use functions to modularize the different actions (add, delete, view contacts).
#1 Create a program that allows the user to add, update, view, and delete contacts.


