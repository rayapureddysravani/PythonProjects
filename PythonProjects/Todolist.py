tasks = []

while True:
    choice = input("Choose Add/View/Remove/Exit:").lower()
    if(choice == "add"):
        tasks.append(input("Enter Task:"))
    elif(choice == "view"):
        for i,task in enumerate(tasks,1):
            print(f"{i}. {task}")
    elif(choice == "remove"):
        index = int(input("Enter a task number to remove::")) -1
        if 0 <= index < len(tasks):
            tasks.pop(index)
    elif(choice == "exit"):
        break