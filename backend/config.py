import os

class Config:
    MEXC_API_KEY = os.getenv("MEXC_API_KEY")
    MEXC_SECRET_KEY = os.getenv("MEXC_SECRET_KEY")
    MEXC_BASE_URL = os.getenv("MEXC_BASE_URL")
