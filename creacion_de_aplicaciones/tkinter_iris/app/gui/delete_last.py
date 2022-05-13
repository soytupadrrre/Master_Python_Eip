import tkinter as tk
from app import RestIris

class DeleteLastApp:
    def __init__(self, master=None):
        # build ui
        self.delete_last_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.delete_last_view.title("Victor Luque - Tkinter - Delete Last")
        self.label41 = tk.Label(self.delete_last_view)
        self.label41.configure(
            font="{Calibri} 16 {}", text="Eliminar última fila en Iris Dataset"
        )
        self.label41.grid(column="0", padx="10", pady="10", row="0")
        self.button14 = tk.Button(self.delete_last_view)
        self.button14.configure(default="normal", text="Eliminar")
        self.button14.grid(column="0", pady="10", row="1")
        self.button14.configure(command=self.send_data)
        self.delete_last_view.configure(height="200", width="200")

        # Main widget
        self.mainwindow = self.delete_last_view

    def run(self):
        self.mainwindow.mainloop()

    def send_data(self):
        RestIris().delete_last_row()


if __name__ == "__main__":
    app = DeleteLastApp()
    app.run()

