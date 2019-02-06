import json
import re

__filename = "./contacts.json"


def search_contact():
    token = input("Enter search string: ")

    infile = open(__filename, "rt")
    data = infile.read()
    infile.close()
    data = json.loads(data)

    outlist = []

    for d in data:
        if re.search(token, d["name"]) is not None:
            outlist.append(d)

    if len(outlist) == 0:
        print("No data found matching the search token: " + token)
    else:
        print("%3s %-20s %-40s %20s" % ("Id", "Name", "Email id", "Phone number"))
        print("-" * 90)
        for d in outlist:
            print("%3d %-20s %-40s %20s" % tuple(d.values()))


def del_contact():
    contact_id = int(input("Enter the id for deletion: "))

    infile = open(__filename, "rt")
    data = infile.read()
    infile.close()
    data = json.loads(data)

    found = False
    for d in data:
        if d["id"] == contact_id:
            found = True
            data.remove(d)
            break

    if found:
        outfile = open(__filename, "wt")
        outfile.write(json.dumps(data))
        outfile.close()
        print("Contact removed from your address book")
    else:
        print("Invalid id!")


def add_new_contact():
    contact = dict()
    contact["id"] = input("Enter id: ")
    contact["name"] = input("Enter name: ")
    contact["email"] = input("Enter email id:" )
    contact["phone"] = input("Enter phone number: ")

    infile = open(__filename, "rt")
    data = infile.read()
    infile.close()
    data = json.loads(data)
    data.append(contact)

    outfile = open(__filename, "wt")
    outfile.write(json.dumps(data))
    outfile.close()

    print("New contact added successfully")


def display_contacts():
    infile = open(__filename, "rt")
    data = infile.read()
    infile.close()
    data = json.loads(data)

    print("%3s %-20s %-40s %20s" % ("Id", "Name", "Email id", "Phone number"))
    print("-"*90)
    for d in data:
        print("%3d %-20s %-40s %20s" % tuple(d.values()))


def menu():
    while True:
        print("""
        MAIN MENU
        ----------------------------
        1. List all contacts
        2. Search contact by name
        3. Add new contact
        4. Delete a contact by id
        5. Exit
        ---------------------------- """)

        choice = input("Enter your choice here: ")

        try:
            choice = int(choice)

            if choice not in range(1, 6):
                print("Invalid choice! Try again")
            elif choice == 5:
                break
            else:
                if choice == 1:
                    display_contacts()
                elif choice == 2:
                    search_contact()
                elif choice == 3:
                    add_new_contact()
                elif choice == 4:
                    del_contact()
        except ValueError as err:
            print("Kindly input a valid integer")
        except FileNotFoundError:
            print("Something wrong with the source file. Kindly inform support team.")

    print("Thank you for using our AddressBook app :-)")


if __name__ == "__main__":
    menu()