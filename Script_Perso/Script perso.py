import os
import csv
from collections import defaultdict


def load_csv_files(path: str) -> list:
    """
    Charge tous les fichiers CSV d'un dossier donné.
    Args:
        path (str): Chemin du dossier contenant les fichiers CSV.
    Returns:
        list: Liste des données des fichiers CSV, chaque élément est un dictionnaire.
    """
    csv_data = []
    for file_name in os.listdir(path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(path, file_name)
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                csv_data.extend(list(reader))
    return csv_data


def merge_csv_data(data: list) -> list:
    """
    Fusionne les données des fichiers CSV en gérant les doublons.
    Args:
        data (list): Liste des données chargées à partir des fichiers CSV.
    Returns:
        list: Liste consolidée des données avec mise à jour des quantités.
    """
    consolidated_data = {}

    for row in data:
        product_name = row['product_name']
        quantity = int(row['quantity'])
        price = float(row['price'])

        # Affichage pour débogage
        print(f"Traitement du produit: {product_name}, quantité: {quantity}, prix: {price}")

        if product_name in consolidated_data:
            # Ajouter la quantité sans toucher au prix
            consolidated_data[product_name]['quantity'] += quantity
            print(f"Produit trouvé, nouvelle quantité pour {product_name}: {consolidated_data[product_name]['quantity']}")
        else:
            # Ajouter un nouveau produit avec son prix et sa quantité uniquement si le produit n'a pas encore de prix
            consolidated_data[product_name] = {'quantity': quantity, 'price': price}
            print(f"Ajout du produit {product_name} avec prix {price} et quantité {quantity}")

    # Convertir en liste de dictionnaires
    return [
        {
            'product_name': name,
            'quantity': details['quantity'],
            'price': details['price'],
            'total_value': details['quantity'] * details['price']
        }
        for name, details in consolidated_data.items()
    ]






def save_consolidated_data(data: list, output_path: str) -> None:
    """
    Sauvegarde les données consolidées dans un fichier CSV.
    Args:
        data (list): Liste des données consolidées.
        output_path (str): Chemin de sortie du fichier CSV consolidé.
    """
    with open(output_path, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['product_name', 'quantity', 'price', 'total_value']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    # Exemple d'utilisation
    input_path = "data/input"  # Répertoire contenant les fichiers CSV
    output_file = "data/consolidated_inventory.csv"

    # Chargement des fichiers CSV
    csv_data = load_csv_files(input_path)

    # Fusion des données
    consolidated_data = merge_csv_data(csv_data)

    # Sauvegarde dans un fichier consolidé
    save_consolidated_data(consolidated_data, output_file)

    print(f"Données consolidées sauvegardées dans {output_file}")
