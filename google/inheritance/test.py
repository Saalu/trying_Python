class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Pig(Animal):
    sound = "Oink"

hamlet = Pig("Hamlet")
hamlet.speak()