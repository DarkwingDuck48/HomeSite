
from sqlalchemy import create_engine
from src.config import Settings


settings = Settings()

print(f"{settings.database_url_test=}")
ENGINE = create_engine(settings.database_url_test)
