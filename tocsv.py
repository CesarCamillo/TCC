import csv
import unidecode as uc

def transform_to_csv(input_file, output_file):
    header = ["pt","en","es","fr","it","gl","ro"]
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file, open(original_file, 'r') as or_file:
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(header)
        buffer = []
        string = or_file.readline()
        buffer.append(uc.unidecode(string.rstrip('\n')))
        
        for line in in_file:
            
            string = uc.unidecode(line.strip().lower())
            buffer.append(string)

            if len(buffer) == 7:
                csv_writer.writerow(buffer)
                buffer = []
                string = or_file.readline()
                if string != "":
                    buffer.append(uc.unidecode(string.rstrip('\n')))

        if buffer:
            csv_writer.writerow(buffer)

if __name__ == "__main__":
    original_file = "maisfreq1200.txt" #Substituia pelo nome do seu arquivo com as palavras originais
    input_file = "maisfreq1200-google.txt"  # Substitua pelo nome do seu arquivo de texto de entrada
    output_file = "maisfreq1200.csv"  # Substitua pelo nome do arquivo CSV de saída

    transform_to_csv(input_file, output_file)