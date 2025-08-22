import pandas as pd
import os
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Contract, Employee, db as engine


print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso.")

Session = sessionmaker(bind=engine)
session = Session()

csv_folder_path = 'data_csv'
try:
    csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]
    if not csv_files:
        print(f"Nenhum arquivo .csv encontrado na pasta '{csv_folder_path}'.")
        exit()
    print(f"Arquivos CSV encontrados: {csv_files}")
except FileNotFoundError:
    print(f"Erro: A pasta '{csv_folder_path}' não foi encontrada.")
    exit()

companies_cache = {}
contracts_cache = {}

for csv_file in csv_files:
    print(f"\nProcessando arquivo: {csv_file}...")
    file_path = os.path.join(csv_folder_path, csv_file)

    try:
        df = pd.read_csv(file_path, encoding='latin-1', sep=';', skiprows=4)
    except Exception as e:
        print(f"Não foi possível ler o arquivo {csv_file}. Erro: {e}")
        continue

    for index, row in df.iterrows():
        try:
            company_name_csv = row['CONTRATADA']
            contract_number_csv = row['CONTRATO']
            employee_name_csv = row['EMPREGADO']
            employee_cpf_csv = row['CPF']
            employee_position_csv = row['FUNCAO']
            employee_sector_csv = row['LOTACAO']

            if pd.isna(employee_name_csv) or pd.isna(employee_cpf_csv):
                continue

            company = companies_cache.get(company_name_csv)
            if not company:
                company = session.query(Company).filter_by(name=company_name_csv).first()
                if not company:
                    company = Company(name=company_name_csv)
                    session.add(company)
                    session.flush()
                companies_cache[company_name_csv] = company

            contract = contracts_cache.get(contract_number_csv)
            if not contract:
                contract = session.query(Contract).filter_by(contract_number=contract_number_csv).first()
                if not contract:
                    contract = Contract(contract_number=contract_number_csv, company_id=company.id)
                    session.add(contract)
                    session.flush()
                contracts_cache[contract_number_csv] = contract

            employee_exists = session.query(Employee).filter_by(cpf=employee_cpf_csv).first()
            if not employee_exists:
                new_employee = Employee(
                    name=employee_name_csv,
                    cpf=employee_cpf_csv,
                    position=employee_position_csv,
                    sector=employee_sector_csv,
                    contract_id=contract.id
                )
                session.add(new_employee)

        except KeyError as e:
            print(f"Erro no arquivo '{csv_file}': A coluna {e} não foi encontrada.")
            session.rollback()
            exit()
        except Exception as e:
            print(f"Ocorreu um erro na linha {index + 5} do arquivo '{csv_file}': {e}")
            session.rollback()
            exit()

print("\nFinalizando... Realizando commit de todos os dados.")
session.commit()
print("Dados de todos os arquivos inseridos com sucesso!")

session.close()
print("Sessão com o banco de dados fechada.")