from datetime import date
from dateutil.relativedelta import relativedelta 

class Czytelnik():

    def __init__(self, name, surname, username) -> None:
        self.name = name
        self.surname = surname
        self.username = username
        self.borrowed_books = []
        self.membership_expiration = self.expiration_date().isoformat()
        self.karta_aktywna = self.is_expired()
        self.kara = self.penalty_counter()


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




