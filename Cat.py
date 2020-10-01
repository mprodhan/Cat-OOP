""" This is a further example of an Object Oriented Program for Python.
Here I created a constructor class for Cat to then instantiate it further."""
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Felix = Cat("Felix", 3)
TomCat = Cat("Tom Cat", 4)
HouseCat = Cat("House Cat", 5)



""" 2 Create a function that finds the oldest cat. Below, 
*args take Felix, TomCat and House Cat as arfuments. If I used just args, 
only one positiional argument would have been recognized and not the rest.
*args takes care of that, in order to encompasee all of the positional 
arguments and not just one. Rule: (args, *args, default parameters, **kwargs.
on return max only args was applied as an argument, because it is then implied
that args is referring to *args."""
def OlderCat(*args):
  return max(args)



""" 3 Print out: "The oldest cat is x years old.". 
x will be the oldest cat age by using the function in #2."""

print(f"The oldest cat is {OlderCat(Felix.age, TomCat.age, HouseCat.age)} years old.")