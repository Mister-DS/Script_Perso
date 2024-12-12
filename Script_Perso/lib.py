import csv

def load_csv_files(filename: str, delimiter: str = ',') -> tuple[list[str], list[list]]:
    """
    Charge les données d'un fichier CSV.
    Args:
        filename (str): Chemin du fichier CSV.
    Returns:
        tuple: Une tuple contenant l'en-tête (list) et les données (list de listes).
    """
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        temp = []
        for row in reader:
            temp.append(row)
        header = temp.pop(0)  # En-tête est la première ligne
        data = []
        for i in temp:
            data.append([i[0], int(i[1]), int(i[2]), i[3]])  # Conversion des colonnes appropriées
        return (header, data)

def equality_check(header1: list[str], header2: list[str]) -> bool:
    """
    Vérifie si deux en-têtes de colonnes sont identiques.

    Args:
        header1 (list[str]): Premier en-tête à comparer.
        header2 (list[str]): Deuxième en-tête à comparer.

    Returns:
        bool: True si les en-têtes sont identiques, False sinon.
    """
    return header1 == header2


def merge_csv_data(data: list) -> list:
    merged_data = {}
    for row in data:
        product_name = row[0]
        if product_name in merged_data:
            merged_data[product_name][1] += row[1]  # Ajout des quantités
        else:
            merged_data[product_name] = row
    return list(merged_data.values())


def unload_data(header: list[str], data: list[list], filename: str) -> None:
    """
    Sauvegarde les données consolidées dans un fichier CSV.

    Args:
        header (list[str]): Liste des noms de colonnes.
        data (list[list]): Liste des données à sauvegarder.
        filename (str): Chemin du fichier CSV de sortie.
    """
    if not data:
        raise ValueError("La liste des données est vide. Rien à sauvegarder.")

    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as result:
            writer = csv.DictWriter(result, fieldnames=header)
            writer.writeheader()
            dict_data = [dict(zip(header, row)) for row in data]
            writer.writerows(dict_data)
        print(f"Données sauvegardées avec succès dans le fichier {filename}.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données : {e}")

def sort_data(data: list[list], header: list[str], column: str, reverse: bool = False) -> list[list]:
    if column in header:
        data_sorted = sorted(data, key=lambda x: x[header.index(column)], reverse=reverse)
        return data_sorted
    else:
        raise ValueError(f"Colonne {column} non trouvée.")


if __name__ == "__main__":
    print(load_csv_files('appliances.csv'))