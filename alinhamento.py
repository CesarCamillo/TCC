import csv
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def needleman_wunsch_alignment(seq1, seq2):
    alignments = pairwise2.align.globalms(seq1, seq2, 1, -0.5, -0.2, -0.1, score_only=True)
    return alignments

def process_csv(input_csv_file, output_directory):
    with open(input_csv_file, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Lê o cabeçalho do CSV

        for i in range(len(headers)):
            for j in range(i + 1, len(headers)):
                # Achar jeito melhor de resetar o arquivo para iniciar o processamento
                csv_file.seek(0)
                csv_reader = csv.reader(csv_file)
                next(csv_reader)

                col1 = ""
                col2 = ""
                result = []
                col1_name = headers[i]
                col2_name = headers[j]

                output_file = f"{output_directory}/{col1_name}_{col2_name}.csv"
                with open(output_file, 'w', newline='') as output_csv:
                    csv_writer = csv.writer(output_csv)
                    csv_writer.writerow([col1_name, col2_name, "Alignment Score"])          

                    for row in csv_reader:
                        col1 = row[i]
                        col2 = row[j]
                        alignment_score = needleman_wunsch_alignment(col1, col2)
                        lower = min(len(col1), len(col2))

                                            #tirar negativo              normalizar
                        dnormal = 1 - ((alignment_score + lower/2) / (3 * lower / 2))
                                                
                        csv_writer.writerow([col1, col2, dnormal])                
                

if __name__ == "__main__":
    input_csv_file = "maisfreq1200.csv"  # Substitua pelo nome do seu arquivo CSV de entrada
    output_directory = "resultados1200"  # Substitua pelo diretório onde deseja salvar os resultados

    process_csv(input_csv_file, output_directory)
