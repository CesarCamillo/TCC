import pandas as pd
import os

def split_csv_randomly(input_csv, output_folder, num_splits=10):
    # Crie a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Carregue o CSV original
    df = pd.read_csv(input_csv)

    # Embaralhe as linhas aleatoriamente
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Calcule o número de linhas por CSV dividido
    rows_per_split = len(df) // num_splits

    # Divida o DataFrame em partes
    dfs = [df.iloc[i*rows_per_split:(i+1)*rows_per_split] for i in range(num_splits)]

    # Salve os CSVs divididos
    for i, split_df in enumerate(dfs):
        output_csv = os.path.join(output_folder, f'{i}/split_{i}.csv')
        split_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    input_csv = "maisfreq1200.csv"  # Substitua pelo caminho do seu arquivo CSV
    output_folder = "resultadossplit"  # Substitua pelo diretório de saída desejado
    num_splits = 10

    split_csv_randomly(input_csv, output_folder, num_splits)