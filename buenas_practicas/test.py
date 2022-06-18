import unittest
import app
from pathlib import Path
import pandas as pd
# Create unittest for app.py
class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file = Path("buenas_practicas/finanzas2020.csv")

    def test_read_file_return_dataframe(self):
        """
        Comprueba que la función read_file devuelva un dataframe
        """
        self.assertIsInstance(app.read_file(self.test_file), pd.DataFrame)

    def test_file_not_found(self):
        """
        Comprueba que la función read_file lanza una excepción si el archivo no existe
        """
        with self.assertRaises(FileNotFoundError):
            app.read_file(Path("buenas_practicas/finanzas2021.csv"))

    def test_check_columns_in_dataframe(self):
        """
        Comprueba que la función check_columns no lanza ningun error de tipo 
        AssertionError y devuelve True en caso de que el dataframe tenga 
        las columnas correctas
        """
        df = app.read_file(self.test_file)
        # Drop last colum
        df_test_col_num = df.drop(df.columns[-1], axis=1)
        self.assertRaises(AssertionError, app.check_columns, df_test_col_num)
        # Lowercase all colums
        df_test_col_names = df.copy()
        df_test_col_names.columns = df_test_col_names.columns.str.lower()
        self.assertRaises(AssertionError, app.check_columns, df_test_col_names)
        self.assertEqual(app.check_columns(df), True)

    def test_parsed_dataframe(self):
        """
        Comprueba que la función parse_dataframe devuelva un dataframe con 12 filas y 2 columnas
        """
        df = app.read_file(self.test_file)
        parsed = app.get_df_year(app.parse_dataframe(df))
        colnames = ["Ahorros", "Gastos"]
        indexnames = ['Enero', 'Febrero', 'Marzo', 
                'Abril', 'Mayo', 'Junio', 
                'Julio', 'Agosto', 'Septiembre', 
                'Octubre', 'Noviembre', 'Diciembre']
        self.assertEqual(parsed.shape, (12, 2))
        self.assertEqual(parsed.columns.tolist(), colnames)
        self.assertEqual(parsed.index.tolist(), indexnames)

    def test_most_spent_month(self):
        """
        Comprueba que la función most_spent_month devuelve el mes con mayor gasto
        """
        df = app.parse_dataframe(app.read_file(self.test_file))
        parsed = app.get_df_year(df)
        month, value = app.most_spent_month(parsed)
        self.assertEqual(month, 'Abril')
        self.assertEqual(value, 34133.0)

    def test_most_saving_month(self):
        """
        Comprueba que la función most_saving_month devuelve el mes con mayor ahorro
        """
        df = app.parse_dataframe(app.read_file(self.test_file))
        parsed = app.get_df_year(df)
        month, value = app.most_saving_month(parsed)
        self.assertEqual(month, 'Enero')
        self.assertEqual(value, 29685.0)

    def test_avg_spent_year(self):
        """
        Comprueba que la función avg_spent_year devuelve el promedio de gastos del año
        """
        df = app.parse_dataframe(app.read_file(self.test_file))
        parsed = app.get_df_year(df)
        avg = app.avg_spent(parsed)
        self.assertEqual(round(avg, 2), 24732.58)
        