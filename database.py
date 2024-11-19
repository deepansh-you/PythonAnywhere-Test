from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Products

DATABASE_URL = "sqlite:///database.db"

engine = create_engine("mysql+pymysql://deepanshyou:deep2808@deepanshyou.mysql.pythonanywhere-services.com/deepanshyou$fynd")
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()