contacts = {}
while True:
    choice = input("Enter choice Add/List/Remove/Exit ::").lower()
    if(choice == "add"):
        names = input("Enter Name:")
        phonenums = input("Enter Phone number:")
        contacts[names] = phonenums
    elif(choice == "list"):
        for key,value in contacts.items():
            print(key,value)
    elif(choice == "remove"):
        name = input("Enter Name to remove:")
        phone = input("Enter Phone number to remove:")
        if name in contacts and contacts[name]==phone:
            contacts.pop(name)
            print(f"{name} reomved")
        else:
            print(f"{name} is not found or {phone} doesn't match")
    elif(choice == "exit"):
        break

