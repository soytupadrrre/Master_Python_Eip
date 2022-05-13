import tkinter as tk
from app.iris import RestIris

class ResumeApp:
    def __init__(self, master=None):
        # build ui
        self.resume_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.resume_view.title("Victor Luque - Tkinter - Resumen")
        self.resume_header = tk.Label(self.resume_view)
        self.resume_header.configure(
            font="{Calibri} 16 {}", justify="center", text="Resumen Datos Iris Dataset"
        )
        self.resume_header.grid(column="0", padx="10", pady="10", row="0")
        self.text2 = tk.Text(self.resume_view)
        self.text2.configure(height="7", padx="10", pady="10", setgrid="true")
        self.text2.configure(state="normal", width="50")
        _text_ = """El resumen de los datos consta de:

- El número de elementos que tiene cada columna
- La media de los campos numéricos
- La desviacion de los campos numéricos
- El mínimo y máximo de los campos numéricos
- El 25%, 50% y 75% de los campos nméricos"""
        self.text2.insert("0.0", _text_)
        self.text2.grid(column="0", row="1")
        self.__tkvar = tk.StringVar(value="Opciones")
        __values = [
            "total",
            "media",
            "desviación",
            "minimo",
            "25",
            "50",
            "75",
            "máximo",
        ]
        self.resume_options = tk.OptionMenu(
            self.resume_view,
            self.__tkvar,
            "Opciones",
            *__values,
            command=self.resume_options_command
        )
        self.resume_options.grid(column="0", row="2")
        self.frame2 = tk.Frame(self.resume_view)
        self.entry_res_spl = tk.Entry(self.frame2)
        self.sepal_length_resume = tk.StringVar(value="0")
        self.entry_res_spl.configure(
            takefocus=True, textvariable=self.sepal_length_resume, validate="none"
        )
        _text_ = """0"""
        self.entry_res_spl.delete("0", "end")
        self.entry_res_spl.insert("0", _text_)
        self.entry_res_spl.grid(column="1", row="1")
        self.resume_label_2 = tk.Label(self.frame2)
        self.resume_label_2.configure(text="Sepal Width:")
        self.resume_label_2.grid(column="0", row="2")
        self.entry_res_spw = tk.Entry(self.frame2)
        self.sepal_width_resume = tk.StringVar(value="0")
        self.entry_res_spw.configure(textvariable=self.sepal_width_resume)
        _text_ = """0"""
        self.entry_res_spw.delete("0", "end")
        self.entry_res_spw.insert("0", _text_)
        self.entry_res_spw.grid(column="1", row="2")
        self.resume_label_3 = tk.Label(self.frame2)
        self.resume_label_3.configure(text="Petal Length:")
        self.resume_label_3.grid(column="0", row="3")
        self.entry_res_ptl = tk.Entry(self.frame2)
        self.petal_length_resume = tk.StringVar(value="0")
        self.entry_res_ptl.configure(textvariable=self.petal_length_resume)
        _text_ = """0"""
        self.entry_res_ptl.delete("0", "end")
        self.entry_res_ptl.insert("0", _text_)
        self.entry_res_ptl.grid(column="1", row="3")
        self.resume_label_4 = tk.Label(self.frame2)
        self.resume_label_4.configure(text="Petal Length:")
        self.resume_label_4.grid(column="0", row="4")
        self.entry_res_ptw = tk.Entry(self.frame2)
        self.petal_width_resume = tk.StringVar(value="0")
        self.entry_res_ptw.configure(textvariable=self.petal_width_resume)
        _text_ = """0"""
        self.entry_res_ptw.delete("0", "end")
        self.entry_res_ptw.insert("0", _text_)
        self.entry_res_ptw.grid(column="1", row="4")
        self.resume_label_1 = tk.Label(self.frame2)
        self.resume_label_1.configure(
            compound="top", relief="flat", text="Sepal Length:"
        )
        self.resume_label_1.grid(column="0", row="1")
        self.frame2.configure(height="200", width="200")
        self.frame2.grid(column="0", row="4")
        self.frame2.rowconfigure("0", pad="10")
        self.frame2.rowconfigure("all", pad="10")
        self.frame2.columnconfigure("0", pad="10")
        self.frame2.columnconfigure("all", pad="10")
        self.label_resume_options = tk.Label(self.resume_view)
        self.resume_option_title = tk.StringVar(value="Totales")
        self.label_resume_options.configure(
            anchor="center", font="{Calibri} 14 {}", justify="center", pady="10"
        )
        self.label_resume_options.configure(
            takefocus=False, text="Opciones"
        )
        self.label_resume_options.grid(column="0", row="3", sticky="ew")
        self.resume_view.configure(height="200", width="200")
        self.__get_resume_data()

        # Main widget
        self.mainwindow = self.resume_view

    def run(self):
        self.mainwindow.mainloop()

    def __clear_all(self):
        self.entry_res_ptl.delete("0", "end")
        self.entry_res_ptw.delete("0", "end")
        self.entry_res_spl.delete("0", "end")
        self.entry_res_spw.delete("0", "end")

    def resume_options_command(self, option):
        self.label_resume_options.update()
        self.__clear_all()
        if option == "total":
            self.label_resume_options.configure(takefocus=False, text="Totales")
            self.entry_res_spl.insert("0",self.count["sepal_length"])
            self.entry_res_spw.insert("0",self.count["sepal_width"])
            self.entry_res_ptl.insert("0",self.count["petal_length"])
            self.entry_res_ptw.insert("0",self.count["petal_width"])
        elif option == "media":
            self.label_resume_options.configure(takefocus=False, text="Media")
            self.entry_res_spl.insert("0",self.mean["sepal_length"])
            self.entry_res_spw.insert("0",self.mean["sepal_width"])
            self.entry_res_ptl.insert("0",self.mean["petal_length"])
            self.entry_res_ptw.insert("0",self.mean["petal_width"])

        elif option == "desviación":
            self.label_resume_options.configure(takefocus=False, text="Desviación")
            self.entry_res_spl.insert("0",self.std["sepal_length"])
            self.entry_res_spw.insert("0",self.std["sepal_width"])
            self.entry_res_ptl.insert("0",self.std["petal_length"])
            self.entry_res_ptw.insert("0",self.std["petal_width"])

        elif option == "minimo":
            self.label_resume_options.configure(takefocus=False, text="Mínimo")
            self.entry_res_spl.insert("0",self.min["sepal_length"])
            self.entry_res_spw.insert("0",self.min["sepal_width"])
            self.entry_res_ptl.insert("0",self.min["petal_length"])
            self.entry_res_ptw.insert("0",self.min["petal_width"])

        elif option == "máximo":
            self.label_resume_options.configure(takefocus=False, text="Máximo")
            self.entry_res_spl.insert("0",self.max["sepal_length"])
            self.entry_res_spw.insert("0",self.max["sepal_width"])
            self.entry_res_ptl.insert("0",self.max["petal_length"])
            self.entry_res_ptw.insert("0",self.max["petal_width"])

        elif option == "25":
            self.label_resume_options.configure(takefocus=False, text="25%")
            self.entry_res_spl.insert("0",self.percentile25["sepal_length"])
            self.entry_res_spw.insert("0",self.percentile25["sepal_width"])
            self.entry_res_ptl.insert("0",self.percentile25["petal_length"])
            self.entry_res_ptw.insert("0",self.percentile25["petal_width"])

        elif option == "50":
            self.label_resume_options.configure(takefocus=False, text="50%")
            self.entry_res_spl.insert("0",self.percentile50["sepal_length"])
            self.entry_res_spw.insert("0",self.percentile50["sepal_width"])
            self.entry_res_ptl.insert("0",self.percentile50["petal_length"])
            self.entry_res_ptw.insert("0",self.percentile50["petal_width"])

        elif option == "75":
            self.label_resume_options.configure(takefocus=False, text="75%")
            self.entry_res_spl.insert("0",self.percentile75["sepal_length"])
            self.entry_res_spw.insert("0",self.percentile75["sepal_width"])
            self.entry_res_ptl.insert("0",self.percentile75["petal_length"])
            self.entry_res_ptw.insert("0",self.percentile75["petal_width"])

        else:
            self.label_resume_options.configure(takefocus=False, text="Opciones")
            self.__clear_all()

    def __get_resume_data(self):
        rest = RestIris()
        resume = rest.get_resume()
        self.count = resume["count"]
        self.mean = resume["mean"]
        self.std = resume["std"]
        self.min = resume["min"]
        self.max = resume["max"]
        self.percentile25 = resume["25%"]
        self.percentile50 = resume["50%"]
        self.percentile75 = resume["75%"]
        


if __name__ == "__main__":
    app = ResumeApp()
    app.run()

