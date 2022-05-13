import tkinter as tk
from app import RestIris

class PredictApp:
    def __init__(self, master=None):
        # build ui
        self.predict_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.predict_view.title("Victor Luque - Tkinter - Predict")
        self.label20 = tk.Label(self.predict_view)
        self.label20.configure(
            font="{Calibri} 16 {}",
            justify="center",
            text="Predecir datos en Iris Dataset",
        )
        self.label20.grid(column="0", padx="10", pady="10", row="0")
        self.frame12 = tk.Frame(self.predict_view)
        self.label21 = tk.Label(self.frame12)
        self.label21.configure(text="Classifier:\n(DecissionTree | RandomForest)")
        self.label21.grid(column="0", row="0")
        self.entry_classifier = tk.Entry(self.frame12)
        _text_ = """DecissionTree"""
        self.entry_classifier.delete("0", "end")
        self.entry_classifier.insert("0", _text_)
        self.entry_classifier.grid(column="1", row="0")
        self.label27 = tk.Label(self.frame12)
        self.label27.configure(text="ID:")
        self.label27.grid(column="0", row="1")
        self.entry_id = tk.Entry(self.frame12)
        self.predicted_result = tk.StringVar(value="0")
        self.entry_id.configure(textvariable=self.predicted_result)
        _text_ = """0"""
        self.entry_id.delete("0", "end")
        self.entry_id.insert("0", _text_)
        self.entry_id.grid(column="1", row="1")
        self.frame12.configure(height="200", width="200")
        self.frame12.grid(column="0", row="2")
        self.frame12.rowconfigure("all", pad="15")
        self.frame12.columnconfigure("all", pad="15")
        self.frame13 = tk.Frame(self.predict_view)
        self.button8 = tk.Button(self.frame13)
        self.button8.configure(text="Limpiar")
        self.button8.grid(column="0", row="0")
        self.button8.configure(command=self.clear_data)
        self.button9 = tk.Button(self.frame13)
        self.button9.configure(text="Enviar")
        self.button9.grid(column="1", row="0")
        self.button9.configure(command=self.send_data)
        self.frame13.configure(height="200", width="200")
        self.frame13.grid(column="0", row="4")
        self.frame13.rowconfigure("all", pad="15")
        self.frame13.columnconfigure("all", pad="30")
        self.frame14 = tk.Frame(self.predict_view)
        self.entry_spl = tk.Entry(self.frame14)
        self.sepal_length_resume = tk.StringVar(value="0")
        self.entry_spl.configure(
            takefocus=True, textvariable=self.sepal_length_resume, validate="none"
        )
        _text_ = """0"""
        self.entry_spl.delete("0", "end")
        self.entry_spl.insert("0", _text_)
        self.entry_spl.grid(column="1", row="1")
        self.label22 = tk.Label(self.frame14)
        self.label22.configure(text="Sepal Width:")
        self.label22.grid(column="2", row="1")
        self.entry_spw = tk.Entry(self.frame14)
        self.sepal_width_resume = tk.StringVar(value="0")
        self.entry_spw.configure(textvariable=self.sepal_width_resume)
        _text_ = """0"""
        self.entry_spw.delete("0", "end")
        self.entry_spw.insert("0", _text_)
        self.entry_spw.grid(column="3", row="1")
        self.label23 = tk.Label(self.frame14)
        self.label23.configure(text="Petal Length:")
        self.label23.grid(column="0", row="2")
        self.entry_ptl = tk.Entry(self.frame14)
        self.petal_length_resume = tk.StringVar(value="0")
        self.entry_ptl.configure(textvariable=self.petal_length_resume)
        _text_ = """0"""
        self.entry_ptl.delete("0", "end")
        self.entry_ptl.insert("0", _text_)
        self.entry_ptl.grid(column="1", row="2")
        self.label24 = tk.Label(self.frame14)
        self.label24.configure(text="Petal Width:")
        self.label24.grid(column="2", row="2")
        self.entry_ptw = tk.Entry(self.frame14)
        self.petal_width_resume = tk.StringVar(value="0")
        self.entry_ptw.configure(textvariable=self.petal_width_resume)
        _text_ = """0"""
        self.entry_ptw.delete("0", "end")
        self.entry_ptw.insert("0", _text_)
        self.entry_ptw.grid(column="3", row="2")
        self.label25 = tk.Label(self.frame14)
        self.label25.configure(compound="top", relief="flat", text="Sepal Length:")
        self.label25.grid(column="0", row="1")
        self.frame14.configure(height="200", width="200")
        self.frame14.grid(column="0", padx="10", row="1")
        self.frame14.rowconfigure("all", pad="10")
        self.frame14.columnconfigure("all", pad="10")
        self.predict_view.configure(height="0", width="0")

        # Main widget
        self.mainwindow = self.predict_view

    def run(self):
        self.mainwindow.mainloop()

    def clear_data(self):
        self.entry_classifier.delete("0", "end")
        self.entry_spl.delete("0", "end")
        self.entry_spw.delete("0", "end")
        self.entry_ptl.delete("0", "end")
        self.entry_ptw.delete("0", "end")
        self.entry_id.delete("0", "end")

    def send_data(self):
        post_data = {
            "sepal_length": float(self.entry_spl.get()),
            "sepal_width": float(self.entry_spw.get()),
            "petal_length": float(self.entry_ptl.get()),
            "petal_width": float(self.entry_ptw.get()),
            "classifier": self.entry_classifier.get(),
        }
        # run rest
        rest_iris = RestIris()
        new_data = rest_iris.post_predict(post_data)
        self.clear_data()
        self.entry_classifier.insert("0", new_data["predicted_species"])
        self.entry_spl.insert("0", new_data["sepal_length"])
        self.entry_spw.insert("0", new_data["sepal_width"])
        self.entry_ptl.insert("0", new_data["petal_length"])
        self.entry_ptw.insert("0", new_data["petal_width"])
        self.entry_id.insert("0", new_data["id"])



        #self.clear_data()


if __name__ == "__main__":
    app = PredictApp()
    app.run()

