import unittest
import bpp1
from pathlib import Path
import pandas as pd
# Create unittest for bpp1.py
class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file = Path("buenas_practicas/finanzas2020.csv")

    def test_read_file_return_dataframe(self):
        """
        # Test 1: La lectura del fichero devuelve un Dataframe
        Este test comprueba que al invocar a la función read_file 
        si el fichero es correcto nos devuelve una instancia de 
        un Dataframe de la librería pandas.
        """
        self.assertIsInstance(bpp1.read_file(self.test_file), pd.DataFrame)

    def test_file_not_found(self):
        """
        Test 2: El fichero no existe
        Este test comprueba que en caso de que el fichero no exista, 
        salte una excepción de tipo FileNotFoundError. 
        """
        with self.assertRaises(FileNotFoundError):
            bpp1.read_file(Path("buenas_practicas/finanzas2021.csv"))

    def test_check_columns_in_dataframe(self):
        """
        Test 3:  Comprobar columnas
        Este test controla que el número de columnas sea 12 y 
        los nombres de las columnas sean los especificados en 
        la función check_columns. 

        En caso de que no sean validos los datos, debe de saltar 
        un error de tipo AssertionError en caso de que todo sea 
        correcto, check_columns debe devolver “True”
        """
        df = bpp1.read_file(self.test_file)
        # Drop last colum
        df_test_col_num = df.drop(df.columns[-1], axis=1)
        self.assertRaises(AssertionError, bpp1.check_columns, df_test_col_num)
        # Lowercase all colums
        df_test_col_names = df.copy()
        df_test_col_names.columns = df_test_col_names.columns.str.lower()
        self.assertRaises(AssertionError, bpp1.check_columns, df_test_col_names)
        self.assertEqual(bpp1.check_columns(df), True)

    def test_parsed_dataframe(self):
        """
        Test 4: Dataframe Formateado
        Este test controla que para realizar las operaciones 
        sea necesario tener un dataframe de 12 filas y 2 columnas. 
        Las filas son los nombres de los meses y las columnas son 
        una para gastos y otra para ahorros.
        """
        df = bpp1.read_file(self.test_file)
        parsed = bpp1.get_df_year(bpp1.parse_dataframe(df))
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
        Test 5: Mes con mayor gasto
        Este test controla que, de acuerdo a los datos de 
        la actividad anterior, el mes con mayor gasto sea 
        abril con un gasto total de 34.133,0 €
        """
        df = bpp1.parse_dataframe(bpp1.read_file(self.test_file))
        parsed = bpp1.get_df_year(df)
        month, value = bpp1.most_spent_month(parsed)
        self.assertEqual(month, 'Abril')
        self.assertEqual(value, 34133.0)

    def test_most_saving_month(self):
        """
        Test 6: Mes con mayor ahorro
        Este test controla que el mes con mayor ahorro 
        sea enero con un total de ahorro de 29.685,0 €
        """
        df = bpp1.parse_dataframe(bpp1.read_file(self.test_file))
        parsed = bpp1.get_df_year(df)
        month, value = bpp1.most_saving_month(parsed)
        self.assertEqual(month, 'Enero')
        self.assertEqual(value, 29685.0)

    def test_avg_spent_year(self):
        """
        Test 7: Media de gastos al año
        Este test controla que la media de gastos anuales
        sea de 24.732,58 €
        """
        df = bpp1.parse_dataframe(bpp1.read_file(self.test_file))
        parsed = bpp1.get_df_year(df)
        avg = bpp1.avg_spent(parsed)
        self.assertEqual(round(avg, 2), 24732.58)
        