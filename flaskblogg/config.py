import os


class Config:
    SECRET_KEY = "aab15c27a35f15fa41d5b36e58333739"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = "smtp.gmail.com"  # "smtp.gmail.com"
    MAIL_PORT = "465"
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
