def create_user():
    name = input("Wprowadź swoje imię:\n")
    surname = input("Wprowadź swoje nazwisko:\n")
    username = input("Wprowadź swoją nazwę użytkownika")
    
    user = Czytelnik(name, surname, username)

    with open(r'.\users.txt', a) as f:
        f.write(user.__str__)

    return "Pomyślnie utworzono konto"


