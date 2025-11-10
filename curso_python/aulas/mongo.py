import pymongo
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessa a variável de ambiente
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    print("❌ Variável MONGO_URI não encontrada no .env")
else:
    try:
        conn = pymongo.MongoClient(MONGO_URI)
        conn.admin.command('ping')
        print("✅ Conectado com sucesso ao MongoDB!")

        db = conn.loja
        print(f"Banco de dados selecionado: {db.name}")

        produtos_collection = db.produtos
        produto = {"nome": "Teclado Mecânico", "preco": 350.00, "estoque": 15}

        resultado = produtos_collection.insert_one(produto)
        print("\n✅ Documento inserido com sucesso!")
        print(f"ID do documento: {resultado.inserted_id}")

    except pymongo.errors.ConnectionFailure as e:
        print(f"❌ Falha ao conectar ao MongoDB: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    finally:
        conn.close()
