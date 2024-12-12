import cmd
import os
from lib import *


class shell(cmd.Cmd):
    intro = 'Welcome to the shell commands - type help or ? for commands.\n'
    prompt = '> '

    def __init__(self):
        super().__init__()
        self.data = []
        self.header = []

    def do_exit(self, line):
        """Exit the Shell"""
        return True

    def do_test(self, line):
        """Do some test for test the shell"""
        print(line)

    def do_add(self, line):
        """Load multiple CSV files and merge data."""
        csv_files = [i for i in os.listdir('.') if i.endswith('.csv')]

        if not csv_files:
            print("Pas de fichier CSV trouvé !")
            return

        for i, file in enumerate(csv_files, 1):
            print(f"{i}. {file}")

        try:
            choices = input("Entrez les numéros des fichiers CSV à lire (séparés par des virgules) : ")
            selected_indices = [int(x.strip()) for x in choices.split(',') if x.strip().isdigit()]

            if not selected_indices:
                print("Aucun fichier sélectionné.")
                return

            selected_files = [csv_files[i - 1] for i in selected_indices if 1 <= i <= len(csv_files)]

            if not selected_files:
                print("Choix invalide. Veuillez réessayer.")
                return

            # Dictionnaire pour stocker les produits avec leurs quantités et prix cumulés
            product_dict = {}

            for file in selected_files:
                header, data = load_csv_files(file)
                for row in data:
                    product_name = row[0]
                    quantity = row[1]
                    price = row[2]

                    if product_name in product_dict:
                        # Additionner les quantités et les prix
                        product_dict[product_name][1] += quantity  # Ajouter la quantité
                        product_dict[product_name][2] += price  # Ajouter le prix
                    else:
                        # Ajouter le produit au dictionnaire
                        product_dict[product_name] = row.copy()  # Utiliser copy pour éviter les références
                        product_dict[product_name][1] = quantity  # Quantité
                        product_dict[product_name][2] = price  # Prix

            # Convertir le dictionnaire en liste
            self.data = list(product_dict.values())

            # Si c'est la première fois que l'on charge des données, on définit l'en-tête
            if not self.header:
                self.header = header

            print(f"Fichiers {', '.join(selected_files)} chargés avec succès.")
        except ValueError:
            print("Veuillez entrer des numéros valides.")

    def do_view(self, line):
        """Affiche les données actuelles"""
        if not self.data:
            print("Aucune donnée à afficher.")
            return
        print(self.header)
        for i in self.data:
            print(i)

    def do_unload(self, line):
        """Unload a CSV file."""
        if not self.data:
            print("Aucune donnée à décharger.")
            return
        filename = input("Entrez le nom du fichier pour sauvegarder les données: ")
        unload_data(self.header, self.data, filename)

    def do_sort(self, line):
        """Trie les données selon une colonne spécifiée. Usage: sort <column_name> [reverse]"""
        if not self.data:
            print("Aucune donnée à trier.")
            return
        args = line.split()
        if len(args) < 1:
            print("Veuillez spécifier le nom de la colonne à trier.")
            return
        column = args[0]
        reverse = len(args) > 1 and args[1].lower() == 'reverse'
        try:
            self.data = sort_data(self.data, self.header, column, reverse)
            print(
                f"Données triées par la colonne '{column}' {'en ordre décroissant' if reverse else 'en ordre croissant'}.")
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    shell().cmdloop()