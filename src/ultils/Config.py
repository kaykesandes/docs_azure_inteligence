import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Container and Storage configurations
    CONTAINER_NAME = os.getenv("CONTAINER-NAME")
    CARTOES_CONNECTION_STRING = os.getenv("CARTOES_CONNECTION_STRING")
    STORAGE_ACCOUNT_NAME = os.getenv("STOREGE_ACCOUNT_NAME")
    KEY_STORAGE_ACCOUNT = os.getenv("KEY_SOTOREGE_ACCOUNT")
    
    # Document Intelligence configurations
    DOC_ENDPOINT = os.getenv("DOC_ENDPOINT")
    KEY_DOC_INTELLIGENCE = os.getenv("KEY_DOC_INTELLIGENCE")