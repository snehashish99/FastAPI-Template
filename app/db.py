from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from configurations import POSTGRES

sync_engine = create_engine(POSTGRES.POSTGRES_DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), nullable=False, default=func.now())
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(300), unique=True, nullable=False)
    phone = Column(String(300), unique=True)
    photo = Column(String(100))
    password = Column(String(500),unique=True)


Base.metadata.create_all(sync_engine)

