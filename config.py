import os

class Config:
    # PostgreSQL configuration
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/pranith")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
