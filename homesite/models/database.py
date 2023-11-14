
import os



from dotenv import load_dotenv
from sqlalchemy import create_engine




load_dotenv()

connection_url = os.getenv("DATABASE_URL_TEST")
if connection_url:
    ENGINE = create_engine(connection_url)
else:
    raise Exception("No Connection string in settings")
