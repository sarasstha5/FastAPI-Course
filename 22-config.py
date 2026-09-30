import os
from dotenv import load_dotenv

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")

setting = Settings()