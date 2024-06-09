from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    total_value = Column(Float, nullable=False)
    estimated_tax = Column(Float, nullable=False)

# Database connection setup
DATABASE_URL = "postgresql://user:password@localhost:5432/blockchain_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
