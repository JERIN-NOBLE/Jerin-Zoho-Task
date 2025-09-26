tasks = []
while True:
    print("\nZoho Task Manager (Jerin)")
    print("1.Add  2.View  3.Done  4.Delete  5.Exit")
    c = input("Choice: ")
    if c == "1":
        tasks.append({"title": input("Task: "), "done": False})
    elif c == "2":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['title']} [{'Done' if t['done'] else 'Pending'}]")
    elif c == "3":
        i = int(input("Task no: ")) - 1
        tasks[i]["done"] = True
    elif c == "4":
        i = int(input("Task no: ")) - 1
        tasks.pop(i)
    elif c == "5":
        print("Goodbye Jerin! Zoho Task Manager closed.")
        break 
