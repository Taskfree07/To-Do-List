import tkinter as tk

class ToDoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do List")

        #create widgets
        self.task_entry = tk.Entry(self.window, width=30)
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.task_list = tk.Listbox(self.window)
        self.delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)

        #place widgets
        self.task_entry.grid(row=0, column=0)
        self.add_button.grid(row=0, column=1)
        self.task_list.grid(row=1, column=0, columnspan=2)
        self.delete_button.grid(row=2, column=1)

        #Bind events
        self.task_list.bind("<Double-1>", self.delete_task)

        self.window.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self, event=None):
        selected_index = self.task_list.cureselection()
        if selected_index:
            self.task_list.delete(selected_index[0])

if __name__ == "__main__":
    app = ToDoListApp()
                    
