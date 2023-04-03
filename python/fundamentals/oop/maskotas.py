class mascota:
    def __init__(self, name , tipo, golosinas, sonido):
        self.name = name
        self.tipo = tipo
        self.tricks = golosinas
        self.health = 100
        self.energy = 50
        self.sonido = sonido

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def play(self):
        self.salud += 5
        self.energia -= 15
        return self

    def sonido(self):
        print(self.sonido)



class Ninja:
    def __init__(self, name, apellido , premios, comida_mascota, mascota):
        self.name = name
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):

        if len(self.comida_mascota) > 0:
            comida = self.comida_mascota.pop()
            print(f"Feeding {self.mascota.name} {comida}!")
            self.mascota.comer()
        else:
            print("Oh no, necesitas más comida para tu mascota")
        return self

    def respirar (self):
        self.mascota.sonido()

premios = ['galletas','pan',"manzanas"]
comida_mascota= ['cereal','carne cocida']

tikki= mascota("Srta. tikki","chinita",['tikki en cosas','es invisible'],"Hola Hola")

marinette = Ninja("marinette","Dupain-Cheng",premios,comida_mascota, tikki)

marinette.comer();
marinette.comer();
marinette.comer();