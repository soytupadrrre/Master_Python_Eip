import tkinter as tk
from app import RestIris

class InsertApp:
    def __init__(self, master=None):
        # build ui
        self.insert_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.insert_view.title("Victor Luque - Tkinter - Insert")
        self.frame7 = tk.Frame(self.insert_view)
        self.entry_spl = tk.Entry(self.frame7)
        self.sepal_length_resume = tk.StringVar(value="0")
        self.entry_spl.configure(
            takefocus=True, textvariable=self.sepal_length_resume, validate="none"
        )
        _text_ = """0"""
        self.entry_spl.delete("0", "end")
        self.entry_spl.insert("0", _text_)
        self.entry_spl.grid(column="1", row="1")
        self.label12 = tk.Label(self.frame7)
        self.label12.configure(text="Sepal Width:")
        self.label12.grid(column="2", row="1")
        self.entry_spw = tk.Entry(self.frame7)
        self.sepal_width_resume = tk.StringVar(value="0")
        self.entry_spw.configure(textvariable=self.sepal_width_resume)
        _text_ = """0"""
        self.entry_spw.delete("0", "end")
        self.entry_spw.insert("0", _text_)
        self.entry_spw.grid(column="3", row="1")
        self.label13 = tk.Label(self.frame7)
        self.label13.configure(text="Petal Length:")
        self.label13.grid(column="0", row="2")
        self.entry_ptl = tk.Entry(self.frame7)
        self.petal_length_resume = tk.StringVar(value="0")
        self.entry_ptl.configure(textvariable=self.petal_length_resume)
        _text_ = """0"""
        self.entry_ptl.delete("0", "end")
        self.entry_ptl.insert("0", _text_)
        self.entry_ptl.grid(column="1", row="2")
        self.label14 = tk.Label(self.frame7)
        self.label14.configure(text="Petal Width:")
        self.label14.grid(column="2", row="2")
        self.entry_ptw = tk.Entry(self.frame7)
        self.petal_width_resume = tk.StringVar(value="0")
        self.entry_ptw.configure(textvariable=self.petal_width_resume)
        _text_ = """0"""
        self.entry_ptw.delete("0", "end")
        self.entry_ptw.insert("0", _text_)
        self.entry_ptw.grid(column="3", row="2")
        self.label15 = tk.Label(self.frame7)
        self.label15.configure(compound="top", relief="flat", text="Sepal Length:")
        self.label15.grid(column="0", row="1")
        self.frame7.configure(height="200", width="200")
        self.frame7.grid(column="0", padx="10", row="1")
        self.frame7.rowconfigure("all", pad="10")
        self.frame7.columnconfigure("all", pad="10")
        self.label18 = tk.Label(self.insert_view)
        self.label18.configure(
            font="{Calibri} 16 {}", text="Insertar datos en Iris Dataset"
        )
        self.label18.grid(column="0", padx="10", pady="10", row="0")
        self.frame10 = tk.Frame(self.insert_view)
        self.label19 = tk.Label(self.frame10)
        self.label19.configure(text="Species:")
        self.label19.grid(column="0", row="0")
        self.entry_species = tk.Entry(self.frame10)
        self.species_resume = tk.StringVar(value="example")
        self.entry_species.configure(textvariable=self.species_resume)
        self.entry_species.grid(column="1", row="0")
        self.label44 = tk.Label(self.frame10)
        self.label44.configure(text="ID:")
        self.label44.grid(column="0", row="1")
        self.entry_id = tk.Entry(self.frame10)
        self.row_id = tk.StringVar(value="0")
        self.entry_id.configure(textvariable=self.row_id)
        _text_ = """0"""
        self.entry_id.delete("0", "end")
        self.entry_id.insert("0", _text_)
        self.entry_id.grid(column="1", row="1")
        self.frame10.configure(height="200", width="200")
        self.frame10.grid(column="0", row="2")
        self.frame10.rowconfigure("all", pad="20")
        self.frame10.columnconfigure("all", pad="20")
        self.frame11 = tk.Frame(self.insert_view)
        self.insert_clear_btn = tk.Button(self.frame11)
        self.insert_clear_btn.configure(text="Limpiar")
        self.insert_clear_btn.grid(column="0", row="0")
        self.insert_clear_btn.configure(command=self.clear_data)
        self.insert_post_btn = tk.Button(self.frame11)
        self.insert_post_btn.configure(text="Enviar")
        self.insert_post_btn.grid(column="1", row="0")
        self.insert_post_btn.configure(command=self.send_data)
        self.frame11.configure(height="200", width="200")
        self.frame11.grid(column="0", row="3")
        self.frame11.rowconfigure("all", pad="15")
        self.frame11.columnconfigure("all", pad="30")
        self.insert_view.configure(height="200", width="200")

        # Main widget
        self.mainwindow = self.insert_view

    def run(self):
        self.mainwindow.mainloop()

    def clear_data(self):
        self.entry_spl.delete("0", "end")
        self.entry_spw.delete("0", "end")
        self.entry_ptl.delete("0", "end")
        self.entry_ptw.delete("0", "end")
        self.entry_species.delete("0", "end")
        self.entry_id.delete("0", "end")

    def send_data(self):
        post_data = {
            "sepal_length": float(self.entry_spl.get()),
            "sepal_width": float(self.entry_spw.get()),
            "petal_length": float(self.entry_ptl.get()),
            "petal_width": float(self.entry_ptw.get()),
            "species": self.entry_species.get(),
        }
        rest_iris = RestIris()
        
        new_data = rest_iris.post_data(post_data)
        self.clear_data()
        self.entry_spl.insert("0", new_data["sepal_length"])
        self.entry_spw.insert("0", new_data["sepal_width"])
        self.entry_ptl.insert("0", new_data["petal_length"])
        self.entry_ptw.insert("0", new_data["petal_width"])
        self.entry_species.insert("0", new_data["species"])
        self.entry_id.insert("0", new_data["id"])


if __name__ == "__main__":
    app = InsertApp()
    app.run()

