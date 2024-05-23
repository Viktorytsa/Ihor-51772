import argparse
import json

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

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file

    # Wczytywanie danych z pliku JSON
    data = load_json(input_file)
    if data:
        print("Dane wczytane poprawnie.")
        # Tutaj możesz kontynuować pracę z wczytanymi danymi
    else:
        print("Wystąpił błąd podczas wczytywania danych.")

if __name__ == "__main__":
    main()

