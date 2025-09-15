#Build a Contact Book to store, view, update, and delete contact names and numbers.


contact_list = []
def add_contacts():
    cname = input("Enter the name: ")
    cnum = input("Enter the number: ")
    data = {
        "Name": cname,
        "Number": cnum
    }
    contact_list.append(data)
    print("Contact added!**")
    
def view_contact():
    print("\nYour Contacts:")
    if not contact_list:
        print("No contacts yet!")
    else:
        for i in range(len(contact_list)):
            print(f"{i+1}. {contact_list[i]['Name']} - {contact_list[i]['Number']}")
            
def update_contact():
    name = input("Enter the name you want to update: ")
    for i in range(len(contact_list)):
        if contact_list[i]["Name"].lower() == name.lower():
            new_num = input("Enter the new number: ")
            contact_list[i]["Number"] = new_num
            print("Contact updated!")
            return
    print("Contact not found!")
def delete_contact():
    name = input("Enter the name you want to delete: ")
    for i in range(len(contact_list)):
        if contact_list[i]["Name"].lower() == name.lower():
            contact_list.pop(i)
            print("Contact deleted!")
            return
    print("Contact not found!")
def contactBook():
    while True:
        print("\nContact Book")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")        
        choice = int(input("Enter your choice: "))        
        if choice == 1:
            add_contacts()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            print("Exiting Contact Book. All Done!")
            break
        else:
            print("Invalid choice! Try again.")
contactBook()
