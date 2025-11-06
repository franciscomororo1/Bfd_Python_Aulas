import pymongo
import os
from dotenv import load_dotenv


#Carregar variaveis do arquivo .env
load_dotenv()

#Acessa a variavel de ambiente
MONGO_URI = os.getenv("MONGO_URI")

#Verfica se a URI foi carregada

if MONGO_URI is None:
    print("não encontrado")
else:
    try:
        conn = pymongo.MongoClient(MONGO_URI)

        conn.admin.command('ping')
        print("conectado com sucesso!")
        print(conn)
        conn.close()

    except pymongo.errors.ConnectionFailure as e:
        print(f"Falha ao conectar ao MONGODB {e}")

        