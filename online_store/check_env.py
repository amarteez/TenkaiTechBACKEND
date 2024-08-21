import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

def check_env_vars():
    print("SECRET_KEY:", os.getenv('SECRET_KEY'))
    print("DEBUG:", os.getenv('DEBUG'))
    print("DJANGO_SETTINGS_MODULE:", os.getenv('DJANGO_SETTINGS_MODULE'))
    print("DB_NAME:", os.getenv('DB_NAME'))
    print("DB_USER:", os.getenv('DB_USER'))
    print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))
    print("DB_HOST:", os.getenv('DB_HOST'))
    print("DB_PORT:", os.getenv('DB_PORT'))

if __name__ == "__main__":
    check_env_vars()
