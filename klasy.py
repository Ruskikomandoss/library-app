from datetime import date
from dateutil.relativedelta import relativedelta 
from sqlalchemy import ForeignKey, Column, String, Integer, CHAR
from bazunia import Base

# Do hasła
from re import match
from werkzeug.security import generate_password_hash

class Czytelnik(Base):

    __tablename__ = "Czytelnicy"
    name = Column("Imię", String)
    surname = Column("Nazwisko", String)
    username = Column("Nazwa_użytkownika", String, primary_key=True)
    password = Column("Hasło", String)
    borrowed_books = Column("Wypożyczone_ksiązki", String)
    membership_expiration = Column("Konto_aktywne_do", String)
    karta_aktywna = Column("Karta_aktywna?", String)
    kara = Column("Wysokość_kary", String)


    def __init__(self, name, surname, username) -> None:
        self.name = name
        self.surname = surname
        self.username = username
        self.password = None
        self.borrowed_books = None
        self.membership_expiration = None
        self.karta_aktywna = None
        self.kara = None

        # Call these at the end of your constructor
        self.password = self.password_validation()
        self.membership_expiration = self.expiration_date().isoformat()
        self.karta_aktywna = self.is_expired()
        self.kara = self.penalty_counter()


    # DO ZROBIENIA: Setters & getters dla danych użytkownika przy użyciu funkcji factory
    # @property
    # def name(self):
    #     return self.name
    # @name.setter
    # def name(self, name):
    #     if name.isalpha() == False:
    #         raise ValueError("Imię może zawierać wyłącznie litery alfabetu")
    #     self.name = name


    def password_validation(self):
        while True:            
            password = input("Wpisz hasło, jakim chcesz się logować do konta.\nHasło powinno zawierać co najmniej jedną wielką literę i jedną cyfrę.\n Powinno być też nie krótsze niż 5 znaków.\nZapamiętaj je dobrze!\nHasło: ")
            pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{5,}'
            if match(pattern, password):
                print("Hasło jest w porządku!")
                return generate_password_hash(password)
            else:
                print("Hasło nie jest prawidłowe. Wpisz inne!\n")

    @staticmethod
    def user_authentication():






    def __str__(self):
        return f"Profil czytelnika: {self.username}\nJesteś członkiem naszej biblioteki do: {self.membership_expiration}\nWypożyczyłeś: {self.borrowed_books}\n(Ewentualna) kara na Twoim koncie za niezwrócone ksiązki wynosi: {self.kara}."



    def expiration_date(self):
        today = date.today()
        twoyearsfromnow = today + relativedelta(months=24)
        return twoyearsfromnow


    def is_expired(self):
        return bool(self.expiration_date() > date.today())
        

    def penalty_counter(self):
        days_gone = date.today() - self.expiration_date()
        if days_gone.days > 0:
            return f"Kara za każdy dzień zwłoki wynosi 50 gr. Twoja kara wynosi obecnie {days_gone.days*0.5:.2f}. Opłać ją czym prędzej!"
        else:
            return f"Kary brak, tak trzymać!"
        

    # def borrow_book():


    
'''
Dodaj jeszcze jakąś fajną funkcję, żeby borrowed books, gdy puste, wyświetlało komunikat
'''


class Book(Base):

    __tablename__ = "Books"
    title = Column("Tytuł", String, primary_key = True)
    author = Column("Autor", String)
    publication_year = Column("Rok publikacji", Integer)
    genre = Column("Gatunek", String)
    availability = Column("Dostępna?", String)
    borrowed_by = Column("Wypożyczone przez użytkownika", String)


    def __init__(self,title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availibility = None
        self.borrowed_by = None
        self.genre = genre


    def __hash__(self):
        return hash(self.title)^hash(self.publication_year)


# to jeszcze wymaga wyjaśnienia, ale chyba będzie przydatne
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return False

