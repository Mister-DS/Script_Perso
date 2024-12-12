import unittest
import os
import csv
import tempfile
from lib import (
    load_csv_files,
    equality_check,
    merge_csv_data,
    unload_data,
    sort_data
)

# réaliser et corriger part claude : https://claude.ai/chat/4f797d83-6013-4cca-a5c3-a0384ed3b3b1


class TestCSVUtils(unittest.TestCase):
    def setUp(self):
        # Créer des fichiers temporaires pour les tests
        self.test_csv_content = [
            ['Product', 'Quantity', 'Price', 'Category'],
            ['Laptop', '10', '1000', 'Electronics'],
            ['Phone', '5', '500', 'Electronics'],
            ['Laptop', '15', '1200', 'Electronics']
        ]

        # Créer un fichier CSV temporaire
        self.temp_csv = tempfile.mktemp(suffix='.csv')
        with open(self.temp_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.test_csv_content)

    def tearDown(self):
        # Nettoyer le fichier temporaire
        if os.path.exists(self.temp_csv):
            os.remove(self.temp_csv)

    def test_load_csv_files(self):
        # Test du chargement des fichiers CSV
        header, data = load_csv_files(self.temp_csv)

        # Vérifier l'en-tête
        self.assertEqual(header, ['Product', 'Quantity', 'Price', 'Category'])

        # Vérifier les données
        expected_data = [
            ['Laptop', 10, 1000, 'Electronics'],
            ['Phone', 5, 500, 'Electronics'],
            ['Laptop', 15, 1200, 'Electronics']
        ]
        self.assertEqual(data, expected_data)

    def test_equality_check(self):
        # Test de la fonction de vérification d'égalité des en-têtes
        header1 = ['A', 'B', 'C']
        header2 = ['A', 'B', 'C']
        header3 = ['A', 'B', 'D']

        self.assertTrue(equality_check(header1, header2))
        self.assertFalse(equality_check(header1, header3))

    def test_merge_csv_data(self):
        # Test de la fonction de fusion des données
        input_data = [
            ['Laptop', 10, 1000, 'Electronics'],
            ['Phone', 5, 500, 'Electronics'],
            ['Laptop', 15, 1200, 'Electronics']
        ]

        merged = merge_csv_data(input_data)

        # Vérifier que les données sont correctement fusionnées
        expected_merged = [
            ['Laptop', 25, 1000, 'Electronics'],
            ['Phone', 5, 500, 'Electronics']
        ]
        self.assertEqual(merged, expected_merged)

    def test_unload_data(self):
        # Test de la sauvegarde des données
        header = ['Product', 'Quantity', 'Price', 'Category']
        data = [
            ['Laptop', 25, 2200, 'Electronics'],
            ['Phone', 5, 500, 'Electronics']
        ]

        # Fichier de sortie temporaire
        output_csv = tempfile.mktemp(suffix='.csv')

        try:
            # Sauvegarder les données
            unload_data(header, data, output_csv)

            # Vérifier que le fichier a été créé
            self.assertTrue(os.path.exists(output_csv))

            # Vérifier le contenu du fichier
            with open(output_csv, 'r', newline='') as f:
                reader = csv.reader(f)
                loaded_data = list(reader)

            expected_content = [
                ['Product', 'Quantity', 'Price', 'Category'],
                ['Laptop', '25', '2200', 'Electronics'],
                ['Phone', '5', '500', 'Electronics']
            ]
            self.assertEqual(loaded_data, expected_content)

        finally:
            # Nettoyer le fichier de sortie
            if os.path.exists(output_csv):
                os.remove(output_csv)

    def test_unload_data_empty_list(self):
        # Test de la levée d'exception pour une liste vide
        header = ['Product', 'Quantity', 'Price', 'Category']
        output_csv = tempfile.mktemp(suffix='.csv')

        with self.assertRaises(ValueError):
            unload_data(header, [], output_csv)

    def test_sort_data(self):
        # Test du tri des données
        header = ['Product', 'Quantity', 'Price', 'Category']
        data = [
            ['Laptop', 25, 2200, 'Electronics'],
            ['Phone', 5, 500, 'Electronics'],
            ['Tablet', 15, 1000, 'Electronics']
        ]

        # Tri par défaut (croissant)
        sorted_data = sort_data(data, header, 'Quantity')
        expected_sorted = [
            ['Phone', 5, 500, 'Electronics'],
            ['Tablet', 15, 1000, 'Electronics'],
            ['Laptop', 25, 2200, 'Electronics']
        ]
        self.assertEqual(sorted_data, expected_sorted)

        # Tri décroissant
        sorted_data_desc = sort_data(data, header, 'Quantity', reverse=True)
        expected_sorted_desc = [
            ['Laptop', 25, 2200, 'Electronics'],
            ['Tablet', 15, 1000, 'Electronics'],
            ['Phone', 5, 500, 'Electronics']
        ]
        self.assertEqual(sorted_data_desc, expected_sorted_desc)

    def test_sort_data_invalid_column(self):
        # Test de la levée d'exception pour une colonne invalide
        header = ['Product', 'Quantity', 'Price', 'Category']
        data = [
            ['Laptop', 25, 2200, 'Electronics'],
            ['Phone', 5, 500, 'Electronics']
        ]

        with self.assertRaises(ValueError):
            sort_data(data, header, 'InvalidColumn')


if __name__ == '__main__':
    unittest.main()