import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

class AllDataApp:
    def __init__(self, master=None):
        # build ui
        self.all_data_view = tk.Tk() if master is None else tk.Toplevel(master)
        self.all_data_view.title("Victor Luque - Tkinter - All Data")
        self.all_data_header = tk.Label(self.all_data_view)
        self.all_data_header.configure(
            font="{Calibri} 16 {}",
            justify="center",
            text="Datos dentro de Iris Dataset",
        )
        self.all_data_header.grid(column="0", padx="10", pady="10", row="0")
        self.treeview5 = ttk.Treeview(self.all_data_view, selectmode="browse")
        self.treeview5.grid(column="0", row="1")
        self.treeview5["columns"] = ("ID", "Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species")
        self.treeview5.column("#0", width=0, minwidth=0, stretch=tk.NO)
        self.treeview5.column("ID", width="50", stretch="no")
        self.treeview5.column("Sepal Length", width="125", stretch="no")
        self.treeview5.column("Sepal Width", width="125", stretch="no")
        self.treeview5.column("Petal Length", width="125", stretch="no")
        self.treeview5.column("Petal Width", width="125", stretch="no")
        self.treeview5.column("Species", width="125", stretch="no")
        self.treeview5.heading("#0", text="ID")
        self.treeview5.heading("ID", text="ID")
        self.treeview5.heading("Sepal Length", text="Sepal Length (cm)")
        self.treeview5.heading("Sepal Width", text="Sepal Width (cm)")
        self.treeview5.heading("Petal Length", text="Petal Length (cm)")
        self.treeview5.heading("Petal Width", text="Petal Width (cm)")
        self.treeview5.heading("Species", text="Species")
        # Insert data from dataframe as tuple
        df = self.__read_csv()
        records = df.to_records(index=False)
        for record in records:
            id, sl, sw, pl, pw, species = record
            self.treeview5.insert("", "end", values=(id, sl, sw, pl, pw, species))
        self.verscrlbar = ttk.Scrollbar(self.all_data_view, orient="vertical", command=self.treeview5.yview)
        self.verscrlbar.grid(column="1", row="1", sticky="ns")
        self.treeview5.configure(yscrollcommand=self.verscrlbar.set)
        self.all_data_view.configure(height="200", width="200")

        # Main widget
        self.mainwindow = self.all_data_view

    def run(self):
        self.mainwindow.mainloop()

    def __read_csv(self):
        df = pd.read_csv("data/iris.csv")
        return df


if __name__ == "__main__":
    app = AllDataApp()
    app.run()
