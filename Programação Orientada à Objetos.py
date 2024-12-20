#_____________________________________________Classe_____________________________________________

# LibraryBook é o nome da classe
class LibraryBook:
  """
  A library book
  """

  # pass indica que o corpo/fato da definição da classe está vazio.
  pass
# Isto irá criar uma instância da classe.
my_book = LibraryBook()

print(my_book)
print(type(my_book))

print(isinstance(my_book, LibraryBook))

#_____________________________________________init, parâmetro Self_____________________________________________

"""
class LibraryBook(object):
  
  #O parâmetro self é OBRIGATÓRIO dentro da classe,
  #porque ele diz ao programa para buscar/atuar sobre o objeto de instância
  #que a executou.

  def __init__(self, title, author, pub_year, call_no):
    self.title = title
    self.author = author
    self.year = pub_year
    self.call_number = call_no
    self.checked_out = False

my_book.title = "Harry Potter and the Philosopher's Stone"
my_book.author = ('Rowling', 'J.K.')
my_book.year = 1998
my_book.call_number = "PZ7.R79835"

"""
#_____________________________________________Métodos_____________________________________________

class LibraryBook(object):

  #Um livro da biblioteca.

  def __init__(self, title, author, pub_year, call_no):
    self.title = title
    self.author = author
    self.year = pub_year
    self.call_number = call_no

  """
  Métodos para o LibraryBook
  """

  # Retorna o título e as informações do autor do livro como uma string
  def title_and_author(self):
    return "{} {}: {}".format(self.author[1], self.author[0], self.title)

    # Imprime todas as informações associadas a um livro neste formato

  def __str__(self):  # certifique-se de que __str__ retorna uma string!
    return "{} {} ({}): {}".format(self.author[1], self.author[0], self.year, self.title)

    # Retorna uma representação de string do livro com o título e call_number

  def __repr__(self):
    return "<Book: {} ({})>".format(self.title, self.call_number)



#_____________________________________________Herança_____________________________________________

class ClownFish(object):
  pass

nemo = ClownFish()
print(type(nemo))

print(isinstance(nemo, ClownFish))

class Animal(object):
  pass

class Vertebrate(Animal):
  pass

class Fish(Vertebrate):
    def speak(self):
        return "Blub"

class ClownFish(Fish):
  pass

class TangFish(Fish):
    def speak(self):
        return "Hello, I'm a TangFish instance."





class Fish(Vertebrate):

  # self.name não é definido na classe Fish, mas é definido na classe ClownFish.
  def __str__(self):
    return "Hello, my name is {}".format(self.name)


class ClownFish(Fish):
  def __init__(self, name):
    self.name = name








