# I will use a Javascript Object notation (JSON) file to store my contacts.
import json

#Then create a function to load my contacts from my file
my_contacts = []

#Adding my contacts by prompting the user to enter an imports and then saves it 

def add_contact():
    contact_name = input("Enter your name: ")
    contact_number = int(input("Enter your phone number: "))
    contact_email_adress = input("Enter your email adress: ")
    contact_age = input("Enter your age: ")
    contact_location = input("Enter your location: ")

# Match contacts to  name, phone number, and email address and store them in dictionary
    contact = {
            "contact_name": contact_name,
            "contact_number": contact_number,
            "contact_email": contact_email_adress,
            "contact_age": contact_age,
            "contact_location": contact_location}
    my_contactscontact.append(my_contacts)
    print(f"Your Contact info has been successfully save: ")

# def view_contacts():
#     if my_contacts:

# def main():
#     print("starting application")
#     add_contact()
# if __name__  == "__main__":
#     main()

# Implement input validation (e.g., ensuring a valid email address format).
# Use functions to modularize the different actions (add, delete, view contacts).
#1 Create a program that allows the user to add, update, view, and delete contacts.


