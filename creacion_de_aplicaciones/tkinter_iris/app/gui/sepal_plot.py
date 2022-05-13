import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
import pandas as pd

class SepalPlotApp:
    def __init__(self, master=None):
        # build ui
        self.sepal_length_plot_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.sepal_length_plot_view.title("Victor Luque - Tkinter - Sepal Plot")
        self.sepal_length_plot_header = tk.Label(self.sepal_length_plot_view)
        self.sepal_length_plot_header.configure(
            font="{Calibri} 16 {}", justify="center", text="Sepal Plot"
        )
        self.sepal_length_plot_header.pack(padx="10", pady="10", side="top")
        self.figure = Figure(figsize=(6, 4))
        self.df = pd.read_csv("data/iris.csv")
        # Create color column based on species
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Sepal")
        self.ax.set_xlabel("Sepal Length")
        self.ax.set_ylabel("Sepal Width")
        # Create scatter where self.df["species"] == "setosa"
        self.ax.scatter(
            self.df[self.df["species"] == "setosa"]["sepal_length"],
            self.df[self.df["species"] == "setosa"]["sepal_width"],
            color="blue",
            label="setosa"
        )
        # Create scatter where self.df["species"] == "versicolor"
        self.ax.scatter(
            self.df[self.df["species"] == "versicolor"]["sepal_length"],
            self.df[self.df["species"] == "versicolor"]["sepal_width"],
            color="green",
            label="versicolor"
        )
        # Create scatter where self.df["species"] == "virginica"
        self.ax.scatter(
            self.df[self.df["species"] == "virginica"]["sepal_length"],
            self.df[self.df["species"] == "virginica"]["sepal_width"],
            color="red",
            label="virginica"
        )
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.figure, self.sepal_length_plot_view)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.sepal_length_plot_view)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack()

        self.mainwindow = self.sepal_length_plot_view

    def run(self):
        self.mainwindow.mainloop()
        
if __name__ == "__main__":
    app = SepalPlotApp()
    app.run()
