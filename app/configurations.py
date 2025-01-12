from decouple import config
import ast


class FASTApiApp:

    APP_NAME = config("APP_NAME", default="FastAPI Backend Template")
    DEBUG = config("DEBUG", cast=bool)
    ORIGINS = config("ORIGINS", cast=lambda x: ast.literal_eval(x))
    METHODS = config("METHODS", cast=lambda x: ast.literal_eval(x))
    HEADERS = config("HEADERS", cast=lambda x: ast.literal_eval(x))


class POSTGRES:

    POSTGRES_USER = config("POSTGRES_USER", cast=str)
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
    POSTGRES_HOST = config("POSTGRES_HOST", cast=str)
    POSTGRES_PORT = config("POSTGRES_PORT", cast=int)
    POSTGRES_DB = config("POSTGRES_DB", cast=str)
    POSTGRES_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    
    POSTGRES_MIN_CONNECTIONS = config("POSTGRES_MIN_CONNECTIONS", cast=int)
    POSTGRES_MAX_CONNECTIONS = config("POSTGRES_MAX_CONNECTIONS", cast=int)