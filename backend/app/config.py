class Config:
    DB_USERNAME = "pass"
    DB_PASSWORD = "pass"
    DB_HOST = "pass"
    DB_DATABASE = "pass"
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}?ssl_disabled=true"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
