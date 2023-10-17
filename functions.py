# Rzeczy z innych plików
from klasy import Czytelnik, Book
from bazunia import Base, database_creation, book_genres, database_SQL_operations, book_creation_prompt

# Do wgrywania wygenerowanych przez AI JSONów do różnych baz
from json import loads

# AI stuff
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

# do sprawdzania, co poszło nie tak
from icecream import ic


# Dodać jakąś weryfikację, czy użytkownik rzeczywiście wpisuje to, co chcemy
def user_creation():
    # Dopisz tu jakieś sprawdzanie, czy nazwa użytkownika nie jest już zajęta
    name = input("\nWprowadź swoje imię:\n")
    surname = input("\nWprowadź swoje nazwisko:\n")

    # username_df = database_SQL_operations("SELECT Nazwa_użytkownika FROM Czytelnicy")
    # while not username_df['Nazwa_użytkownika'].isin([username]).any():
    #     print("Taka nazwa użytkownika jest już zajęta. Wprowadź inną")
    username = input("\nWprowadź swoją nazwę użytkownika:\n")

    return Czytelnik(name, surname, username)


# Dodać jakąś weryfikację, czy użytkownik rzeczywiście wpisuje to, co chcemy
def book_creation():

    publication = book_json_creator()
    title = publication['Tytuł']
    author = publication['Autor']
    publication_year = publication['Rok publikacji']
    genre = publication['Gatunek']
    return Book(title, author, publication_year, genre)


def book_creation_admin():
    title = input("Wpisz tytuł ksiązki:\n")
    author = input("Wpisz imię i nazwisko autora:\n")
    publication_year = input("W którym roku wydano książkę? Wpisz rok jako cyfry:\n")
    genre = book_genre_selection()
    return Book(title, author, publication_year, genre)

# dodaj weryfikację, czy na pewno coś jest wprowadzane - i w ogóle rozwiąż to jakoś rozsądnie, może dekoratorami?
def book_genre_selection():
    print("\nJakiego gatunku jest to książka? Wpisz numer widoczny obok odpowiedniego:\n")
    for genre in range(len(book_genres)):
        print(f"{genre+1} - {book_genres[genre]}")
    chosed_genre = input("Wpisz cyfrę/liczbę: ")
    num = int(chosed_genre)-1 
    return book_genres[num]


def user_database_adding():
    session = database_creation("users.db", Base)
    user = user_creation()
    session.add(user)
    session.commit()
    session.close()


def book_database_adding():
    book_session = database_creation("books.db", Base)
    book = book_creation()
    book_session.add(book)
    book_session.commit()
    book_session.close()
    print("Pomyślnie dodano książkę!")


# users3 albo books
def book_display():
    all_books = database_SQL_operations("SELECT Tytuł, Autor, Gatunek FROM Books", database="books")
    all_books = all_books.set_index('Tytuł').sort_index()
    return print(all_books)
    

# def book_borrowing():
    # do tego trzeba się nauczyć, jak zmieniać dane 


def books_stats():
    book_count = database_SQL_operations("SELECT Tytuł FROM Books", 'books')
    print(f"Ilość książek w naszej bibliotece: {book_count.count()['Tytuł']}")
    author_count = database_SQL_operations("SELECT Autor FROM Books GROUP BY Autor", 'books')
    print(f"W bibliotece mamy książki aż {author_count.count()['Autor']} autorów!\n")
    genre_count = database_SQL_operations("SELECT Gatunek FROM Books", 'books')
    genre_dict = genre_count.value_counts().sort_values().to_dict().items()
    print(f"Oto spis poszczególnych gatunków wraz z ilością książek:\n") 
    for (genre,), count in genre_dict:
        print(f"{genre}: {count}")


def book_json_creator():
    messages = [
    SystemMessage(content=book_creation_prompt),
    HumanMessage(content="Create a JSON file")
]
    chat = ChatOpenAI(
    model="gpt-4",
    temperature=0.9,
    max_tokens=300
)
    result = chat.invoke(messages)
    return loads(result.content)


# def user_profile(Czytelnik):



def library_main_menu():
    # Powitanie
    print("Witamy w naszej bibliotece!".center(40,"_"))
    print()
    print("Nim zaczniesz wypożyczać książki z naszego zbioru, musisz założyć konto lub zakogować się do już istniejącego profilu.\nRejestracja jest darmowa, ale jeżeli nie jesteś pewien/pewna, czy znajdziesz u nas coś dla siebie, możesz najpierw przejrzeć nasz księgozbiór.\nBez względu na to, czy jesteś miłośnikiem literatury, studentem poszukującym materiałów do nauki, czy po prostu kochasz czytać w wolnym czasie, nasza biblioteka ma dla Ciebie coś wyjątkowego!".center(50))
    
    choices = {
        "1": "Załóż nowe konto",
        "2": "Zaloguj się do swojego konta",
        "3": "Przejrzyj nasze książki",
        "4": "Statystyki biblioteki dla ciekawskich",
        "5": "Wyjdź z programu"
    }
    # Dodaj opcję dla administratora, żeby móc... no w sumie co?

    while True:
        print("\nWybierz jedną z dostępnych opcji, wpisując odpowiednią cyfrę:\n")
        for key, value in choices.items():
            print(f"{key} - {value}")

        choice = input()

        if choice == "1":
            user_database_adding()
            
            print("Konto pomyślnie założone!")
            # Tu by trzeba teraz płynnie przejść do konta użytkownika
        elif choice == "2":
            print("Strona w budowie. Zapraszamy potem!")
            pass
        elif choice == "3":
            book_display()
        elif choice == "4":
            books_stats()
        elif choice == "5":
            print("\nSzkoda, że już się żegnamy. Do zobaczenia!")
            break
        else:
            print("Niestety nie zrozumieliśmy tej komendy.\nWpisz cyfrę spośród wymienionych wyżej, wtedy na pewno się zrozumiemy!")









# def books_borrowed()



if __name__ == "__main__":
    # with engine.connect() as connection:
    user_database_adding()
    # book_database_adding()
    # book_display()
    # books_stats()
    # library_main_menu()

    # x = 0
    # while x < 4:
    #     book_database_adding()
    #     x +=1


