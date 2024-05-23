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

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file

    # Wczytywanie danych z pliku YAML
    data = load_yaml(input_file)
    if data:
        print("Dane wczytane poprawnie.")
        # Tutaj możesz kontynuować pracę z wczytanymi danymi

if __name__ == "__main__":
    main()

