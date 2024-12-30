import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title('File Explorer')
        self.root.geometry("500x600")
        self.root.config(background="white")

        # Create a File Explorer label
        self.label_file_explorer = tk.Label(self.root, 
                                            text="File Explorer using Tkinter",
                                            width=100, height=4, 
                                            fg="blue", bg="white")
        self.label_file_explorer.grid(column=1, row=1)

        # Create a button to browse files
        self.button_explore = tk.Button(self.root, 
                                         text="Browse Files",
                                         command=self.browse_files)
        self.button_explore.grid(column=1, row=2)

        # Create a button to browse directories
        self.button_browse_dir = tk.Button(self.root, 
                                            text="Browse Directory",
                                            command=self.browse_directory)
        self.button_browse_dir.grid(column=1, row=3)

        # Create a button to open the selected file
        self.button_open_file = tk.Button(self.root, 
                                           text="Open File",
                                           command=self.open_file)
        self.button_open_file.grid(column=1, row=4)

        # Create a button to exit the application
        self.button_exit = tk.Button(self.root, 
                                      text="Exit",
                                      command=self.root.destroy)
        self.button_exit.grid(column=1, row=5)

        # Create a label to display the selected file
        self.label_selected_file = tk.Label(self.root, 
                                            text="", 
                                            width=100, height=4, 
                                            fg="black", bg="white")
        self.label_selected_file.grid(column=1, row=6)

        # Initialize the selected file path
        self.selected_file_path = ""

    def browse_files(self):
        self.selected_file_path = filedialog.askopenfilename(initialdir="/",
                                                            title="Select a File",
                                                            filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        self.label_selected_file.config(text="File Opened: " + self.selected_file_path)

    def browse_directory(self):
        self.selected_file_path = filedialog.askdirectory(initialdir="/",
                                                          title="Select a Directory")
        self.label_selected_file.config(text="Directory Selected: " + self.selected_file_path)
        
    def open_file(self):
        if self.selected_file_path:
            try:
                if self.selected_file_path.endswith(".txt"):
                    with open(self.selected_file_path, 'r') as file:
                        file_content = file.read()
                        messagebox.showinfo("File Content", file_content)
                else:
                    messagebox.showerror("Error", "Only text files are supported.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a file first.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    file_explorer = FileExplorer(root)
    file_explorer.run()