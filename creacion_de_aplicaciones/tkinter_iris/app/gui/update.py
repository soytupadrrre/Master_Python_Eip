import tkinter as tk
from app import RestIris

class UpdateIdApp:
    def __init__(self, master=None):
        # build ui
        self.update_id_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.update_id_view.title("Victor Luque - Tkinter - Update Id")
        self.label34 = tk.Label(self.update_id_view)
        self.label34.configure(
            font="{Calibri} 16 {}", text="Actualizar en Iris Dataset"
        )
        self.label34.grid(column="0", padx="10", pady="10", row="0")
        self.frame20 = tk.Frame(self.update_id_view)
        self.label35 = tk.Label(self.frame20)
        self.label35.configure(text="ID:")
        self.label35.grid(column="0", row="0")
        self.entry_u_id = tk.Entry(self.frame20)
        self.id_field_value = tk.StringVar(value="0")
        self.entry_u_id.configure(
            font="TkDefaultFont", textvariable=self.id_field_value
        )
        _text_ = """0"""
        self.entry_u_id.delete("0", "end")
        self.entry_u_id.insert("0", _text_)
        self.entry_u_id.grid(column="1", row="0")
        self.frame20.configure(height="200", width="200")
        self.frame20.grid(column="0", row="1")
        self.frame20.rowconfigure("all", pad="15")
        self.frame20.columnconfigure("all", pad="20")
        self.frame21 = tk.Frame(self.update_id_view)
        self.entry_u_spl = tk.Entry(self.frame21)
        self.sepal_length_resume = tk.StringVar(value="0")
        self.entry_u_spl.configure(
            takefocus=True, textvariable=self.sepal_length_resume, validate="none"
        )
        _text_ = """0"""
        self.entry_u_spl.delete("0", "end")
        self.entry_u_spl.insert("0", _text_)
        self.entry_u_spl.grid(column="1", row="1")
        self.label36 = tk.Label(self.frame21)
        self.label36.configure(text="Sepal Width:")
        self.label36.grid(column="2", row="1")
        self.entry_u_spw = tk.Entry(self.frame21)
        self.sepal_width_resume = tk.StringVar(value="0")
        self.entry_u_spw.configure(textvariable=self.sepal_width_resume)
        _text_ = """0"""
        self.entry_u_spw.delete("0", "end")
        self.entry_u_spw.insert("0", _text_)
        self.entry_u_spw.grid(column="3", row="1")
        self.label37 = tk.Label(self.frame21)
        self.label37.configure(text="Petal Length:")
        self.label37.grid(column="0", row="2")
        self.entry_u_ptl = tk.Entry(self.frame21)
        self.petal_length_resume = tk.StringVar(value="0")
        self.entry_u_ptl.configure(textvariable=self.petal_length_resume)
        _text_ = """0"""
        self.entry_u_ptl.delete("0", "end")
        self.entry_u_ptl.insert("0", _text_)
        self.entry_u_ptl.grid(column="1", row="2")
        self.label38 = tk.Label(self.frame21)
        self.label38.configure(text="Petal Width:")
        self.label38.grid(column="2", row="2")
        self.entry_u_ptw = tk.Entry(self.frame21)
        self.petal_width_resume = tk.StringVar(value="0")
        self.entry_u_ptw.configure(textvariable=self.petal_width_resume)
        _text_ = """0"""
        self.entry_u_ptw.delete("0", "end")
        self.entry_u_ptw.insert("0", _text_)
        self.entry_u_ptw.grid(column="3", row="2")
        self.label39 = tk.Label(self.frame21)
        self.label39.configure(compound="top", relief="flat", text="Sepal Length:")
        self.label39.grid(column="0", row="1")
        self.frame21.configure(height="200", width="200")
        self.frame21.grid(column="0", row="2")
        self.frame21.rowconfigure("all", pad="10")
        self.frame21.columnconfigure("all", pad="10")
        self.frame22 = tk.Frame(self.update_id_view)
        self.label40 = tk.Label(self.frame22)
        self.label40.configure(text="Species:")
        self.label40.grid(column="0", row="0")
        self.entry_u_species = tk.Entry(self.frame22)
        self.species_resume = tk.StringVar(value="example")
        self.entry_u_species.configure(textvariable=self.species_resume)
        _text_ = """example"""
        self.entry_u_species.delete("0", "end")
        self.entry_u_species.insert("0", _text_)
        self.entry_u_species.grid(column="1", row="0")
        self.frame22.configure(height="200", width="200")
        self.frame22.grid(column="0", row="3")
        self.frame22.rowconfigure("all", pad="20")
        self.frame22.columnconfigure("all", pad="20")
        self.frame23 = tk.Frame(self.update_id_view)
        self.button12 = tk.Button(self.frame23)
        self.button12.configure(text="Limpiar")
        self.button12.grid(column="0", row="0")
        self.button12.configure(command=self.clear_data)
        self.button13 = tk.Button(self.frame23)
        self.button13.configure(text="Enviar")
        self.button13.grid(column="1", row="0")
        self.button13.configure(command=self.send_data)
        self.frame23.configure(height="200", width="200")
        self.frame23.grid(column="0", row="4")
        self.frame23.rowconfigure("all", pad="15")
        self.frame23.columnconfigure("all", pad="30")
        self.update_id_view.configure(height="200", width="200")

        # Main widget
        self.mainwindow = self.update_id_view

    def run(self):
        self.mainwindow.mainloop()

    def clear_data(self):
        self.entry_u_ptl.delete("0", "end")
        self.entry_u_ptw.delete("0", "end")
        self.entry_u_spl.delete("0", "end")
        self.entry_u_spw.delete("0", "end")
        self.entry_u_species.delete("0", "end")
        self.entry_u_id.delete("0", "end")

    def send_data(self):
        put_data = {
            "sepal_length": float(self.entry_u_spl.get()),
            "sepal_width": float(self.entry_u_spw.get()),
            "petal_length": float(self.entry_u_ptl.get()),
            "petal_width": float(self.entry_u_ptw.get()),
            "species": self.entry_u_species.get(),
            "id": int(self.entry_u_id.get()),
        }
        rest_iris = RestIris()
        new_data = rest_iris.put_by_id(put_data)
        self.clear_data()
        self.entry_u_ptl.insert("0", new_data["petal_length"])
        self.entry_u_ptw.insert("0", new_data["petal_width"])
        self.entry_u_spl.insert("0", new_data["sepal_length"])
        self.entry_u_spw.insert("0", new_data["sepal_width"])
        self.entry_u_species.insert("0", new_data["species"])
        self.entry_u_id.insert("0", new_data["id"])


if __name__ == "__main__":
    app = UpdateIdApp()
    app.run()

