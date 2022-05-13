import tkinter as tk
from app import RestIris


class DeleteIdApp:
    def __init__(self, master=None):
        # build ui
        self.delete_id_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.delete_id_view.title("Victor Luque - Tkinter - Delete by Id")
        self.label42 = tk.Label(self.delete_id_view)
        self.label42.configure(font="{Calibri} 16 {}", text="Eliminar en Iris Dataset")
        self.label42.grid(column="0", padx="10", pady="10", row="0")
        self.frame24 = tk.Frame(self.delete_id_view)
        self.label43 = tk.Label(self.frame24)
        self.label43.configure(text="ID:")
        self.label43.grid(column="0", row="0")
        self.entry_d_id = tk.Entry(self.frame24)
        _text_ = """0"""
        self.entry_d_id.delete("0", "end")
        self.entry_d_id.insert("0", _text_)
        self.entry_d_id.grid(column="1", row="0")
        self.frame24.configure(height="200", width="200")
        self.frame24.grid(column="0", row="1")
        self.frame24.rowconfigure("all", pad="15")
        self.frame24.columnconfigure("all", pad="20")
        self.frame25 = tk.Frame(self.delete_id_view)
        self.button15 = tk.Button(self.frame25)
        self.button15.configure(text="Limpiar")
        self.button15.grid(column="0", row="0")
        self.button15.configure(command=self.clear_data)
        self.button16 = tk.Button(self.frame25)
        self.button16.configure(text="Enviar")
        self.button16.grid(column="1", row="0")
        self.button16.configure(command=self.send_data)
        self.frame25.configure(height="200", width="200")
        self.frame25.grid(column="0", row="2")
        self.frame25.rowconfigure("all", pad="15")
        self.frame25.columnconfigure("all", pad="30")
        self.delete_id_view.configure(height="200", width="200")

        # Main widget
        self.mainwindow = self.delete_id_view

    def run(self):
        self.mainwindow.mainloop()

    def clear_data(self):
        self.entry_d_id.delete("0", "end")

    def send_data(self):
        delete_data = {
            "id": int(self.entry_d_id.get())
        }
        rest_iris = RestIris()
        rest_iris.delete_by_id(delete_data)
        self.clear_data()


if __name__ == "__main__":
    app = DeleteIdApp()
    app.run()
