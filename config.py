from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['POSTGRESQL_USER']
password = os.environ['POSTGRESQL_PASSWORD']
database = os.environ['POSTGRESQL_DATABASE']
host = os.environ['POSTGRESQL_HOST']
port = os.environ['POSTGRESQL_PORT']
entropy = os.environ['ENTROPY']


DATA_BASE_CONNECTION_URI = f"postgresql://{user}:{password}@{host}:{port}/{database}"

ENTROPY = entropy

