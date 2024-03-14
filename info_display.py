class Person:
  def __init__(self, name: str , age: int, gender: str) :
   self.name=name
   self.age= age
   self.gender= gender
  def introduce(self):
    return f"Hello! My name is {self.name}, I am {self.age} years old, and I identify as {self.gender}."

person1=Person("Charity",19,"Female")
print(person1.introduce())
    