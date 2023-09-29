
# Função para converte csv em json
def csv_para_json(arquivo):
    import csv
    with open(arquivo, 'r', encoding='utf-8', errors='replace') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        dados = [linha for linha in leitor]
    return dados


# Função para adicionar dados no MongoDB
def adicionar_dados(dados, bd_nome, collection_nome):
    from pymongo import MongoClient
    cliente = MongoClient('127.0.0.1:27017')
    bd = cliente[bd_nome]
    collection = bd[collection_nome]
    collection.insert_many(dados)
    print(f"Dados inseridos com sucesso em {bd_nome}.{collection_nome}!")


# Função de conexão
def conexao(bd_nome, collection_nome):
    from pymongo import MongoClient
    cliente = MongoClient('127.0.0.1:27017')
    bd = cliente[bd_nome]
    collection = bd[collection_nome]
    return collection


# Função de Criação de arquivo JSON
def criar_json(dados, arquivo):
    import json
    with open(arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
    print(f"Arquivo {arquivo} criado com sucesso!")
