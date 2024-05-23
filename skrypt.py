import argparse
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")
    return parser.parse_args()

def save_as_xml(data, file_path):
    try:
        # Tworzenie głównego elementu XML
        root = ET.Element("data")

        # Tworzenie elementów i dodawanie ich do głównego elementu
        for key, value in data.items():
            sub_element = ET.SubElement(root, key)
            sub_element.text = str(value)

        # Tworzenie drzewa XML i zapis do pliku
        tree = ET.ElementTree(root)
        tree.write(file_path)

        print(f"Dane zapisane do pliku {file_path} w formacie XML.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu danych do pliku XML: {e}")

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file

    # Tutaj wczytaj dane z pliku wejściowego, np. z pliku JSON lub YAML
    data = {}  # Załóżmy, że dane zostały wczytane z innego formatu i są dostępne jako słownik

    # Zapis danych do pliku XML
    save_as_xml(data, output_file)

if __name__ == "__main__":
    main()

