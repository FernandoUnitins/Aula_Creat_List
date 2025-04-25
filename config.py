import os
from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do banco de dados MySQL
class Config:
    MYSQL_DATABASE_HOST = os.getenv('MYSQL_HOST')
    MYSQL_DATABASE_USER = os.getenv('MYSQL_USER')
    MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE_DB = os.getenv('MYSQL_DB')
