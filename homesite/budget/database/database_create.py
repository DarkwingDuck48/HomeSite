import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from models import Base, Users, Categories, Accounts, Operations

load_dotenv()

print(os.getenv("DATABASE_URL_PROD"))



#engine = create_engine('sqlite:///test.db')
#Base.metadata.create_all(bind=engine)


#engine = create_engine(f'postgresql+psycopg2://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}')


