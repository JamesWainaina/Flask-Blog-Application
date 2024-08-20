import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASS')


    # export  EMAIL_USER="mojay9905@gmail.com"
    # export  EMAIL_PASS="James9905"
    # export  SECRET_KEY='5791628bb0b13ce0c676dfde280ba245'
    # export  SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
