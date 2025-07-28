tasks = []

def handle_task():
    while True:
        choice = input("Add/View/Delete/Exit > ").strip().lower()
        if choice == "add":
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == "view":
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t}")
        elif choice == "delete":
            idx = int(input("Index to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
        elif choice == "exit":
            break
        else:
            print("Invalid choice.")
