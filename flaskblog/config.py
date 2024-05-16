import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER')   
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # export  EMAIL_USER="mojay9905@gmail.com"
    # export  EMAIL_PASS="James9905"
    # export  SECRET_KEY='5791628bb0b13ce0c676dfde280ba245'
    # export  SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
