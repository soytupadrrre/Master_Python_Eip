import tkinter as tk
try:
    from .petal_plot import PetalPlotApp
    from .sepal_plot import SepalPlotApp
except: 
    from petal_plot import PetalPlotApp
    from sepal_plot import SepalPlotApp

class FlowerApp:
    def __init__(self, master=None):
        # build ui
        self.length_plot_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.label16 = tk.Label(self.length_plot_view)
        self.label16.configure(
            font="{Calibri} 16 {}",
            text="Gráficos del Sépalo y del Pétalo",
        )
        self.label16.grid(column="0", padx="10", pady="10", row="0")
        self.frame8 = tk.Frame(self.length_plot_view)
        self.sepal_length_plot_btn = tk.Button(self.frame8)
        self.sepal_length_plot_btn.configure(text="Ver Sepal Plot")
        self.sepal_length_plot_btn.grid(column="0", row="0")
        self.sepal_length_plot_btn.configure(command=self.show_sepal_length_plot)
        self.petal_length_plot_btn = tk.Button(self.frame8)
        self.petal_length_plot_btn.configure(text="Ver Petal Plot")
        self.petal_length_plot_btn.grid(column="1", row="0")
        self.petal_length_plot_btn.configure(command=self.show_petal_length_plot)
        self.frame8.configure(height="200", width="200")
        self.frame8.grid(column="0", row="1")
        self.frame8.rowconfigure("all", pad="20")
        self.frame8.columnconfigure("all", pad="20")
        self.length_plot_view.configure(height="200", width="200")
        self.length_plot_view.title("Victor Luque - Tkinter - Flower")

        # Main widget
        self.mainwindow = self.length_plot_view

    def run(self):
        self.mainwindow.mainloop()

    def show_sepal_length_plot(self):
        app_sepal = SepalPlotApp()
        app_sepal.run()

    def show_petal_length_plot(self):
        app_petal = PetalPlotApp()
        app_petal.run()


if __name__ == "__main__":
    app = FlowerApp()
    app.run()

