import tkinter as tk
from app import RestIris

class UpdateLastApp:
    def __init__(self, master=None):
        # build ui
        self.update_last_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.update_last_view.title("Victor Luque - Tkinter - Update Last")
        self.frame17 = tk.Frame(self.update_last_view)
        self.entry_ul_spl = tk.Entry(self.frame17)
        self.sepal_length_resume = tk.StringVar(value="0")
        self.entry_ul_spl.configure(
            takefocus=True, textvariable=self.sepal_length_resume, validate="none"
        )
        _text_ = """0"""
        self.entry_ul_spl.delete("0", "end")
        self.entry_ul_spl.insert("0", _text_)
        self.entry_ul_spl.grid(column="1", row="1")
        self.label28 = tk.Label(self.frame17)
        self.label28.configure(text="Sepal Width:")
        self.label28.grid(column="2", row="1")
        self.entry_ul_spw = tk.Entry(self.frame17)
        self.sepal_width_resume = tk.StringVar(value="0")
        self.entry_ul_spw.configure(textvariable=self.sepal_width_resume)
        _text_ = """0"""
        self.entry_ul_spw.delete("0", "end")
        self.entry_ul_spw.insert("0", _text_)
        self.entry_ul_spw.grid(column="3", row="1")
        self.label29 = tk.Label(self.frame17)
        self.label29.configure(text="Petal Length:")
        self.label29.grid(column="0", row="2")
        self.entry_ul_ptl = tk.Entry(self.frame17)
        self.petal_length_resume = tk.StringVar(value="0")
        self.entry_ul_ptl.configure(textvariable=self.petal_length_resume)
        _text_ = """0"""
        self.entry_ul_ptl.delete("0", "end")
        self.entry_ul_ptl.insert("0", _text_)
        self.entry_ul_ptl.grid(column="1", row="2")
        self.label30 = tk.Label(self.frame17)
        self.label30.configure(text="Petal Width")
        self.label30.grid(column="2", row="2")
        self.entry_ul_ptw = tk.Entry(self.frame17)
        self.petal_width_resume = tk.StringVar(value="0")
        self.entry_ul_ptw.configure(textvariable=self.petal_width_resume)
        _text_ = """0"""
        self.entry_ul_ptw.delete("0", "end")
        self.entry_ul_ptw.insert("0", _text_)
        self.entry_ul_ptw.grid(column="3", row="2")
        self.label31 = tk.Label(self.frame17)
        self.label31.configure(compound="top", relief="flat", text="Sepal Length:")
        self.label31.grid(column="0", row="1")
        self.frame17.configure(height="200", width="200")
        self.frame17.grid(column="0", row="1")
        self.frame17.rowconfigure("all", pad="10")
        self.frame17.columnconfigure("all", pad="10")
        self.label32 = tk.Label(self.update_last_view)
        self.label32.configure(
            font="{Calibri} 16 {}", text="Actualizar última fila en Iris Dataset"
        )
        self.label32.grid(column="0", padx="10", pady="10", row="0")
        self.frame18 = tk.Frame(self.update_last_view)
        self.label33 = tk.Label(self.frame18)
        self.label33.configure(text="Species:")
        self.label33.grid(column="0", row="0")
        self.entry23 = tk.Entry(self.frame18)
        self.entry_species = tk.StringVar(value="example")
        self.entry23.configure(state="normal", textvariable=self.entry_species)
        _text_ = """example"""
        self.entry23.delete("0", "end")
        self.entry23.insert("0", _text_)
        self.entry23.grid(column="1", row="0")
        self.frame18.configure(height="200", width="200")
        self.frame18.grid(column="0", row="2")
        self.frame18.rowconfigure("all", pad="20")
        self.frame18.columnconfigure("all", pad="20")
        self.frame19 = tk.Frame(self.update_last_view)
        self.button10 = tk.Button(self.frame19)
        self.button10.configure(text="Limpiar")
        self.button10.grid(column="0", row="0")
        self.button10.configure(command=self.clear_data)
        self.button11 = tk.Button(self.frame19)
        self.button11.configure(text="Enviar")
        self.button11.grid(column="1", row="0")
        self.button11.configure(command=self.send_data)
        self.frame19.configure(height="200", width="200")
        self.frame19.grid(column="0", row="3")
        self.frame19.rowconfigure("all", pad="15")
        self.frame19.columnconfigure("all", pad="30")
        self.update_last_view.configure(height="200", width="200")

        # Main widget
        self.mainwindow = self.update_last_view

    def run(self):
        self.mainwindow.mainloop()

    def clear_data(self):
        self.entry_ul_ptl.delete("0", "end")
        self.entry_ul_ptw.delete("0", "end")
        self.entry_ul_spl.delete("0", "end")
        self.entry_ul_spw.delete("0", "end")
        self.entry23.delete("0", "end")

    def send_data(self):
        put_data = {
            "sepal_length": float(self.entry_ul_spl.get()),
            "sepal_width": float(self.entry_ul_spw.get()),
            "petal_length": float(self.entry_ul_ptl.get()),
            "petal_width": float(self.entry_ul_ptw.get()),
            "species": self.entry_species.get(),
        }
        rest_iris = RestIris()
        new_data = rest_iris.put_last_row(put_data)
        self.clear_data()
        self.entry_ul_ptl.insert("0", new_data["petal_length"])
        self.entry_ul_ptw.insert("0", new_data["petal_width"])
        self.entry_ul_spl.insert("0", new_data["sepal_length"])
        self.entry_ul_spw.insert("0", new_data["sepal_width"])
        self.entry23.insert("0", new_data["species"])



if __name__ == "__main__":
    app = UpdateLastApp()
    app.run()

