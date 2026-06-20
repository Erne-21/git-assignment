todos = ["Buy groceries", "Finish homework", "Walk the dog"]


def show_todos():
    print("\n--- My To-Do List ---")
    if not todos:
        print("(empty)")
    for i, item in enumerate(todos, start=1):
        print(f"{i}. {item}")


def add_todo(item):
    todos.append(item)
    print(f"Added: {item}")


def menu():
    while True:
        print("\n1) View  2) Add  3) Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_todos()
        elif choice == "2":
            item = input("New to-do: ")
            add_todo(item)
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()