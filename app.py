TODO_FILE = "todos.txt"


def load_todos():
    try:
        with open(TODO_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return ["Buy groceries", "Finish homework", "Walk the dog"]


def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(todos))


def show_todos(todos):
    print("\n--- My To-Do List ---")
    if not todos:
        print("(empty)")
    for i, item in enumerate(todos, start=1):
        print(f"{i}. {item}")


def add_todo(todos, item):
    todos.append(item)
    print(f"Added: {item}")


def remove_todo(todos, index):
    try:
        removed = todos.pop(index - 1)
        print(f"Removed: {removed}")
    except IndexError:
        print("Invalid item number.")


def menu():
    todos = load_todos()
    while True:
        print("\n1) View  2) Add  3) Remove  4) Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            item = input("New to-do: ")
            add_todo(todos, item)
        elif choice == "3":
            show_todos(todos)
            try:
                idx = int(input("Number to remove: "))
                remove_todo(todos, idx)
            except ValueError:
                print("Please enter a number.")
        elif choice == "4":
            save_todos(todos)
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()