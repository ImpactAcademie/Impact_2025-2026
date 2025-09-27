from functools import wraps

nom = input("Votre prénom: ")

def deco(function):
  @wraps(function)
  def w():
    print("---------")
    function()
    print("---------")
  return w

@deco
def prenom():
  """docstring"""
  print("Bienvenue",nom,"!")
prenom()

print(prenom.__name__)
print(prenom.__doc__)