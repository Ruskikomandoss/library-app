import json
from langchain import PromptTemplate, OpenAI, LLMChain
import os
os.environ["OPENAI_API_KEY"] = "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"


    
books = """
  {
    "Jane Austen": ["Duma i uprzedzenie", "Rozważna i romantyczna", "Emma"],
    "Charles Dickens": ["Wielkie nadzieje", "Oliver Twist", "Opowieść wigilijna"],
    "F. Scott Fitzgerald": ["Wielki Gatsby", "Tęsknota jest cierpieniem", "Na tym brzegu raju"],
    "Charlotte Bronte": ["Jane Eyre", "Shirley", "Villette"],
    "William Shakespeare": ["Hamlet", "Makbet", "Romeo i Julia"],
    "George Orwell": ["Rok 1984", "Folwark zwierzęcy", "Do dna w Paryżu i Londynie"],
    "Leo Tolstoy": ["Wojna i pokój", "Anna Karenina", "Śmierć Iwana Iljicza"],
    "Mark Twain": ["Przygody Hucka Finna", "Przygody Tomka Sawyera", "Książę i żebrak"],
    "Emily Bronte": ["Wichrowe Wzgórza"],
    "Herman Melville": ["Moby Dick", "Billy Budd", "Typee"],
    "Nathaniel Hawthorne": ["Grzechy mnicha", "Dom siedmiu szczytów", "Nathaniel Hawthorne Opowieści"],
    "Joseph Conrad": ["Jądro ciemności", "Lord Jim", "Nostromo"],
    "Edgar Allan Poe": ["Kruk i inne wiersze", "Zbrodnia w Rue Morgue", "Zabicie człowieka wiszącego"],
    "H. G. Wells": ["Wojna światów", "Człowiek niewidzialny", "Maszyna czasu"],
    "Oscar Wilde": ["Portret Doriana Graya", "Istotna sprawa", "Wachlarz lady Windermere"],
    "Jules Verne": ["Dwadzieścia tysięcy mil podmorskiej żeglugi", "Podróż do wnętrza Ziemi", "Wokół świata w osiemdziesiąt dni"],
    "Mary Shelley": ["Frankenstein", "Ostatni człowiek", "Lodore"],
    "Robert Louis Stevenson": ["Wyspa skarbów", "Doktor Jekyll i pan Hyde", "Porwany"],
    "Homer": ["Iliada", "Odyseja"],
    "Thomas Hardy": ["Tess z d'Urberville", "Za młodu", "Burmistrz casterbridge"],
    "Jack London": ["Zew krwi", "Biały kieł", "Zbudować ogień"],
    "Fiodor Dostojewski": ["Zbrodnia i kara", "Bracia Karamazow", "Idiota"],
    "Charlotte Perkins Gilman": ["Z żółtej tapety", "Krzyż", "Herland"],
    "Henry David Thoreau": ["Walden", "O nieposłuszeństwie", "Tydzień nad Concord i Merrimack"],
    "Gustave Flaubert": ["Pani Bovary", "Salammbô", "Wykształcenie uczuć"],
    "Arthur Conan Doyle": ["Przygody Sherlocka Holmesa", "Pies Baskerville'ów", "Znak czterech"],
    "Ralph Waldo Emerson": ["Samowystarczalność", "Poeta", "Natura"],
    "Hans Christian Andersen": ["Mała syrenka", "Nowe szaty cesarza", "Brzydkie kaczątko"],
    "Louisa May Alcott": ["Małe kobietki", "Synowie i kochankowie", "Mali mężczyźni"],
    "Kahlil Gibran": ["Prorok", "Szaleniec", "Ogród proroka"]
  }
    """

# funkcja pozwala nam zobaczyć wszystkich autorów, a następnie dostępne książki jego/jej autorstwa

def autorzy(books):

  x = [author for author in enumerate(json.loads(books))]
  
  print("Oto dostępni autorzy. Żeby sprawdzić, jakie książki tego autora są dostępne, wpisz numer widniejący obok imienia i nazwiska autora.\n")
  for tuple in x:
      print(tuple)
  print()
  num = int(input("Wpisz liczbę obok autora, żeby wyświetlić jego ksiązki:"))
  if num in range(0, len(x)):
      author_name = x[num][1]
      y = json.loads(books)
      return y[f"{author_name}"]
  else:
     raise ValueError("Niestety nie mamy autora pod tym numerem. Wpisz numer od 0 do 29!")
    

# Tu będziemy generować opisy książek - taka pomoc przy wyborze
def about(ksiazki):
  
  title = input("Nie znasz wszystkich tytułów? Wpisz tytuł książki, której opis chciałbyś przeczytać: \n")
  prompt_template = "Opisz następują książkę po polsku w pięciu zdaniach: {książka}"
  llm = OpenAI(temperature=0.8, max_retries=3, max_tokens=1000, model_name="text-davinci-003")
  chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))

  response = chain(f"{title}")

  return response["text"].lstrip("\n\n")


def main():
   
  print("\nWitamy w wypożyczalni książek!\n")
  ksiazki = autorzy(books)
  print()
  print(ksiazki, "\n")

  x = input("Wiesz już, co wybierasz? Jesli tak, wpisz tytuł. Jeśli nie, możemy Ci pomóc! Wpisz 'porada', żeby móc przeczytać streszczenie którejś z nich")
  if x == "porada".lower():
     

  opis = about(ksiazki)
  print(opis, "\n")
  print("Czy chcesz wypożyczyć tę książkę? Wpisz 'tak', by ją wypożyczyć, lub 'nie', by wrócić do ekranu głównego")


if __name__ == "__main__":
   main()
