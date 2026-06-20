"""Simple To-Do List - v1
   A static to-do list that just displays a few items.
   """

   todos = ["Buy groceries", "Finish homework", "Walk the dog"]


   def show_todos():
       print("\n--- My To-Do List ---")
       for i, item in enumerate(todos, start=1):
           print(f"{i}. {item}")


   if __name__ == "__main__":
       show_todos()