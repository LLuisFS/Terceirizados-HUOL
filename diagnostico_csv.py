import os

# Pega o primeiro arquivo da sua pasta de dados
csv_folder_path = 'data_csv'

try:
    files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]
    if not files:
        print(f"Nenhum arquivo .csv encontrado em '{csv_folder_path}'")
        exit()

    primeiro_arquivo = files[0]
    file_path = os.path.join(csv_folder_path, primeiro_arquivo)

    print(f"--- Inspecionando as 5 primeiras linhas do arquivo: {primeiro_arquivo} ---")

    # Abre o arquivo e lê as 5 primeiras linhas
    with open(file_path, 'r', encoding='latin-1') as f:
        for i in range(5):
            line = f.readline()
            print(f"Linha {i+1}: {repr(line)}") # repr() mostra caracteres invisíveis como \n

except Exception as e:
    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")

print("\n--- Fim da inspeção ---")