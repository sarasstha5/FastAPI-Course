from fastapi import FastAPI,Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker, declarative_base

app = FastAPI()

engine = create_engine("sqlite:///./alchemydatabase.db") # Create a new SQLite database file named "alchemydatabase.db"
sessionlocal = sessionmaker(bind = engine)               # Create a session factory bound to the engine

Base = declarative_base()                                # Create a base class for the ORM models, that work internally like mapping the database tables to Python classes

class User(Base):                                        # Define a User model that inherits from the Base class, it defines the table structure for the "user" table in the database
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

Base.metadata.create_all(bind=engine) # Create the "user" table in the database

#commonly used dependency to get a database session
#session is used to interact with the database operations, such as querying, inserting, updating, and deleting records. It acts as a bridge between the application code and the database, allowing developers to work with Python objects instead of writing raw SQL queries.
def get_db():
    db = sessionlocal()                                   # Create a new database session
    try:
        yield db         
    finally:
        db.close()

@app.get("/users")
def get_user(db: Session = Depends(get_db)):
    return"database connection successful"