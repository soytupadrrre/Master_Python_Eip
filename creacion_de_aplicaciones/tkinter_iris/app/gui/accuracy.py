import tkinter as tk
import tkinter.ttk as ttk
from app.iris import RestIris

class AccuracyApp:
    def __init__(self, master=None):
        # build ui
        self.accuracy_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.accuracy_view.title("Victor Luque - Tkinter - Accuracy")
        self.label9 = tk.Label(self.accuracy_view)
        self.label9.configure(
            font="{Calibri} 16 {}", text="Precisión Algoritmos Machine Learning"
        )
        self.label9.grid(column="0", padx="10", pady="10", row="0")
        self.text3 = tk.Text(self.accuracy_view)
        self.text3.configure(height="3", insertunfocussed="none", padx="10", pady="10")
        self.text3.configure(state="disabled", takefocus=False, undo="true", width="50")
        self.text3.configure(wrap="word")
        _text_ = """En esta sección se muestra la precisión de los algoritmos DecisionTree y RandomForest sobre Iris Dataset"""
        self.text3.configure(state="normal")
        self.text3.insert("0.0", _text_)
        self.text3.configure(state="disabled")
        self.text3.grid(column="0", row="1", sticky="ew")
        self.frame6 = tk.Frame(self.accuracy_view)
        self.frame4 = tk.Frame(self.frame6)
        self.label10 = tk.Label(self.frame4)
        self.label10.configure(
            compound="top", font="{Calibri} 14 {}", justify="center", relief="flat"
        )
        self.label10.configure(text="Decission Tree Classifier\nAccuracy")
        self.label10.grid(column="0", row="0")
        self.entry_dtc = tk.Entry(self.frame4)
        self.dtc_accuracy = tk.StringVar(value="0")
        self.entry_dtc.configure(textvariable=self.dtc_accuracy)
        _text_ = """0"""
        self.entry_dtc.delete("0", "end")
        self.entry_dtc.insert("0", _text_)
        self.entry_dtc.grid(column="0", row="1", sticky="n")
        self.frame4.configure(height="10", width="10")
        self.frame4.grid(column="0", row="0")
        self.frame4.rowconfigure("all", pad="20")
        self.frame5 = tk.Frame(self.frame6)
        self.label11 = tk.Label(self.frame5)
        self.label11.configure(
            font="{Calibri} 14 {}", text="Random Tree Classifier\nAccuracy"
        )
        self.label11.grid(column="0", row="0")
        self.entry_rtf = tk.Entry(self.frame5)
        self.rtf_accuracy = tk.StringVar(value="0")
        self.entry_rtf.configure(textvariable=self.rtf_accuracy)
        _text_ = """0"""
        self.entry_rtf.delete("0", "end")
        self.entry_rtf.insert("0", _text_)
        self.entry_rtf.grid(column="0", row="1", sticky="n")
        self.frame5.configure(height="10", width="10")
        self.frame5.grid(column="2", row="0", sticky="n")
        self.frame5.rowconfigure("all", pad="20")
        self.separator2 = ttk.Separator(self.frame6)
        self.separator2.configure(orient="vertical")
        self.separator2.grid(column="1", ipady="40", padx="10", row="0")
        self.frame6.configure(height="10", width="10")
        self.frame6.grid(column="0", row="2", sticky="n")
        self.accuracy_view.configure(height="200", width="200")
        self.__get_accuracy()

        # Main widget
        self.mainwindow = self.accuracy_view

    def run(self):
        self.mainwindow.mainloop()

    def __get_accuracy(self):
        rest = RestIris()
        dtc, rfc = rest.get_accuracy()["algorithms"]
        self.entry_dtc.delete("0", "end")
        self.entry_rtf.delete("0", "end")
        self.entry_dtc.insert("0",dtc["results"]["accuracy"])
        self.entry_rtf.insert("0", rfc["results"]["accuracy"])


if __name__ == "__main__":
    app = AccuracyApp()
    app.run()

