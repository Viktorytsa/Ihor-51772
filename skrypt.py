import argparse
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    return parser.parse_args()

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

def main():
    args = parse_arguments()
    input_file = args.input_file

    # Wczytywanie danych z pliku XML
    root = load_xml(input_file)
    if root is not None:
        print("Dane wczytane poprawnie.")
        # Tutaj możesz kontynuować pracę z wczytanymi danymi

if __name__ == "__main__":
    main()
