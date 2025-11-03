contacts = {}
while True:
    print("\n1.add a new contact")
    print("2.view contact")
    print("3.delete a contact")
    print("4.exit")
    choice = input("choose any one: ")
    print("----")
    if choice == 1:
        name = input("enter a name: ")
        number = int(input("enter number: "))
        contacts[name] = number
        contacts.update()
        print("----")
    elif choice == 2:
        if len(contacts) == 0:
            print("no contacts to view")
            print("----")
        else:
            print(f"{name}:{number}")
    elif choice == 3:
        if len(contacts) == 0:
            print("no contact to delete")
            print("-----")
        else:
            delete = input("enter a name to delete: ")
            if name in contacts:
                contacts.pop()
                print("----")
    elif choice == 4:
        print("closing...closed")
        break
    else:
        print("invalid")