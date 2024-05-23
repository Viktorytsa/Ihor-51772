import argparse
import yaml

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

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

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file

    # Wczytywanie danych z pliku YAML
    data = load_yaml(input_file)
    if data:
        print("Dane wczytane poprawnie.")
        # Tutaj możesz kontynuować pracę z wczytanymi danymi

        # Zapis danych do pliku YAML
        save_as_yaml(data, output_file)
    else:
        print("Wystąpił błąd podczas wczytywania danych.")

if __name__ == "__main__":
    main()

