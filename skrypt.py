import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd podczas wczytywania pliku JSON: {e}")
        return None
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return None

def save_as_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Dane zapisane do pliku {file_path} w formacie JSON.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu danych do pliku JSON: {e}")

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Błąd podczas wczytywania pliku YAML: {e}")
        return None
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return None

def save_as_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        print(f"Dane zapisane do pliku {file_path} w formacie YAML.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu danych do pliku YAML: {e}")

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd podczas wczytywania pliku XML: {e}")
        return None
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return None

def save_as_xml(data, file_path):
    try:
        root = ET.Element("data")
        for key, value in data.items():
            sub_element = ET.SubElement(root, key)
            sub_element.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(file_path)
        print(f"Dane zapisane do pliku {file_path} w formacie XML.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu danych do pliku XML: {e}")

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file

    # Wybór formatu pliku na podstawie rozszerzenia
    if input_file.endswith('.json'):
        # Task2: Wczytywanie danych z pliku JSON
        data = load_json(input_file)
        if data:
            # Task3: Zapis danych do pliku JSON
            save_as_json(data, output_file)
    elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
        # Task4: Wczytywanie danych z pliku YAML
        data = load_yaml(input_file)
        if data:
            # Task5: Zapis danych do pliku YAML
            save_as_yaml(data, output_file)
    elif input_file.endswith('.xml'):
        # Task6: Wczytywanie danych z pliku XML
        data = load_xml(input_file)
        if data:
            # Task7: Zapis danych do pliku XML
            save_as_xml(data, output_file)
    else:
        print("Nieobsługiwany format pliku.")

if __name__ == "__main__":
    main()


