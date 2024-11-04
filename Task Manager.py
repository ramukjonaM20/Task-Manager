# Import the tkinter library for creating GUI applications
import tkinter as tk
from tkinter import messagebox
# Import the TaskManager class (assumed to be in a separate module 'task_manager.py') which handles task logic
from task_manager import TaskManager

# Define a class for the Task Manager application
class TaskManagerApp:
    # Initialize the TaskManagerApp with the root window
    def __init__(self, root):
        # Create an instance of the TaskManager for task management
        self.manager = TaskManager()
        # Store the root Tkinter window
        self.root = root
        # Set the title of the root window
        self.root.title("To-Do List Application")
        # Call the method to create all the widgets for the GUI
        self.create_widgets()

    # Method to create and display all widgets for the To-Do List application
    def create_widgets(self):
        # Create a Listbox to display the list of tasks
        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.pack(pady=10)

        # Create an entry box for the user to add or edit tasks
        self.add_entry = tk.Entry(self.root, width=40)
        self.add_entry.pack(pady=5)

        # Create a frame to organize buttons horizontally
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Button to add a new task to the list
        add_button = tk.Button(button_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=0, padx=5) # Position the button within the frame with padding

        # Button to edit the selected task in the list
        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task)
        edit_button.grid(row=0, column=1, padx=5)

        # Button to delete the selected task from the list
        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=0, column=2, padx=5)

        # Button to mark the selected task as complete
        complete_button = tk.Button(button_frame, text="Mark Complete", command=self.mark_task_complete)
        complete_button.grid(row=0, column=3, padx=5)

        # Load and display the tasks from the TaskManager
        self.load_tasks()

    # Method to load and display tasks in the Listbox
    def load_tasks(self):
        # Clear all items in the Listbox to refresh it
        self.task_listbox.delete(0, tk.END)
        # Iterate over tasks in the TaskManager
        for task in self.manager.tasks:
            # Display a checkmark (✓) for completed tasks and a cross (✗) for incomplete tasks
            status = "✓" if task['completed'] else "✗"
            # Insert each task into the Listbox with its status and description
            self.task_listbox.insert(tk.END, f"[{status}] {task['description']}")

    # Method to add a new task to the list
    def add_task(self):
        # Get the description of the task from the entry box
        description = self.add_entry.get()
        # If the entry is not empty, proceed with adding the task
        if description:
            # Add the task to the TaskManager
            self.manager.add_task(description)
            # Reload and display tasks in the Listbox
            self.load_tasks()
            # Clear the entry box after adding the task
            self.add_entry.delete(0, tk.END)

    # Method to edit the selected task
    def edit_task(self):
        try:
            # Get the index of the selected task in the Listbox
            index = self.task_listbox.curselection()[0]
            # Get the new description from the entry box
            new_description = self.add_entry.get()
            # If the entry is not empty, proceed with editing the task
            if new_description:
                # Edit the task in the TaskManager
                self.manager.edit_task(index, new_description)
                # Reload and display tasks in the Listbox
                self.load_tasks()
                # Clear the entry box after editing the task
                self.add_entry.delete(0, tk.END)
        except IndexError:
            # Show a warning if no task is selected to edit
            messagebox.showwarning("Edit Task", "Please select a task to edit.")

    # Method to delete the selected task
    def delete_task(self):
        try:
            # Get the index of the selected task in the Listbox
            index = self.task_listbox.curselection()[0]
            # Delete the task from the TaskManager
            self.manager.delete_task(index)
            # Reload and display tasks in the Listbox
            self.load_tasks()
        except IndexError:
            # Show a warning if no task is selected to delete
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    # Method to mark the selected task as complete
    def mark_task_complete(self):
        try:
            # Get the index of the selected task in the Listbox
            index = self.task_listbox.curselection()[0]
            # Mark the task as complete in the TaskManager
            self.manager.mark_task_complete(index)
            # Reload and display tasks in the Listbox
            self.load_tasks()
        except IndexError:
            # Show a warning if no task is selected to mark complete
            messagebox.showwarning("Mark Complete", "Please select a task to mark complete.")


# Main block to run the application
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Create an instance of TaskManagerApp with the root window
    app = TaskManagerApp(root)
    # Start the Tkinter main event loop
    root.mainloop()
