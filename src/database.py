
from sqlalchemy import create_engine
from src.config import Settings


settings = Settings()
ENGINE = create_engine(settings.database_url_test)
