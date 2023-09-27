from datetime import date
from dateutil.relativedelta import relativedelta 
from functions import create_user

class Czytelnik():

    def __init__(self, name, surname, username) -> None:
        self.name = name
        self.surname = surname
        self.username = username
        self.borrowed_books = []
        self.membership_expiration = self.expiration_date().isoformat()
        self.karta_aktywna = self.is_expired()
        self.kara = self.penalty_counter()


    def __str__(self):
        return f"Profil czytelnika: {self.username}\nJesteś członkiem naszej biblioteki do: {self.membership_expiration}\nWypożyczyłeś: {self.borrowed_books}\n(Ewentualna) kara na Twoim koncie za niezwrócone ksiązki wynosi: {self.kara}."

    def expiration_date(self):
        today = date.today()
        twoyearsfromnow = today + relativedelta(months=24)
        return twoyearsfromnow


    def is_expired(self):
        return self.expiration_date() > date.today()
        

    def penalty_counter(self):
        days_gone = date.today() - self.expiration_date()
        if days_gone.days > 0:
            return f"Kara za każdy dzień zwłoki wynosi 50 gr. Twoja kara wynosi obecnie {days_gone.days*0.5:.2f}. Opłać ją czym prędzej!"
        else:
            return f"Kary brak, tak trzymać!"

    
'''
Dodaj jeszcze jakąś fajną funkcję, żeby borrowed books, gdy puste, wyświetlało komunikat
'''


class Book():

    def __init__(self,title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availibility = bool
        self.borrowed_by = str
        self.genre = genre



    def __hash__(self):
        return hash(self.title)^hash(self.publication_year)

# to jeszcze wymaga wyjaśnienia, ale chyba będzie przydatne
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return False





if __name__ == "__main__":
    create_user()
