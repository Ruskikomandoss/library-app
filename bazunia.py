from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

# Do weryfikowania danych w db, np. dostępności
import pandas as pd
import sqlite3 
import os

# Do zapełnienia biblioteki 


book_genres = ['Romans', 'Thriller', 'Fantasy', 'Sci-fi', 'Kryminał', 'Horror', 'Dla dzieci', 'Powieść historyczna', 'Literatura faktu', 'Biografia', 'Dramat', 'Poezja', 'Komedia', 'Przygodowa', 'Psychologiczna', 'Poradnik', 'Instruktażowa']

book_creation_prompt = """
#MAIN GOAL
You are an AI powered Chatbot who helps me creating JSON files of made-up book data for my Python project that imitates a library. Your purpose in life is to return me a fully-fledged, crafted JSON file with single book entry. 
#RULES
The JSON data is returned in Polish.
Do not talk to me. Do not engage in any sort of conversation. You just hand me back a JSON.
The book data are all purely fictional, you can't cite me real books or authors. Book titles should be silly. Author's name and surname can be of foreign origin.
Every entry you create must be unique.
The entry consist of following pieces of information: "Tytuł", "Autor", "Rok publikacji" and "Gatunek". As for the first three, it's up to you to come up with them. As for the Gatunek, your task is to select the best matching one from the following Python list: 
book_genres = ['Romans', 'Thriller', 'Fantasy', 'Sci-fi', 'Kryminał', 'Horror', 'Dla dzieci', 'Powieść historyczna', 'Literatura faktu', 'Biografia', 'Dramat', 'Poezja', 'Komedia', 'Przygodowa', 'Psychologiczna', 'Poradnik', 'Instruktażowa']
#AN EXAMPLE
book = {
"Tytuł": "Dlaczego warto jeść karmę"
"Autor": "Mysz Remi"
"Rok publikacji": 2021
"Gatunek": "Poradnik"
}
"""

Base = declarative_base()

def database_creation(db_name, Base):

    # Sprawdzamy najpierw, czy coś się nie spieprzyło
    directory = os.path.dirname(f"D:\Python\Rzeczy\Library\{db_name}.db")
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # Jeśli nie, jazda
    engine_path = 'sqlite:///'+db_name
    engine = create_engine(engine_path, echo=True, poolclass = NullPool)    
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()



def database_SQL_operations(sql_query, database):
    conn = sqlite3.connect(f"D:\Python\Rzeczy\Library\{database}.db")
    cur = conn.cursor()
    sql = pd.read_sql_query(sql_query, conn)
    conn.close()
    return pd.DataFrame(sql)


# def 


