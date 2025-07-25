import os
from dotenv import load_dotenv

load_dotenv() 

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'aman-meena')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:MySQLPassword%402004@localhost/crime')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
