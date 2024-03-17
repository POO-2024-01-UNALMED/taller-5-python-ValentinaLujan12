from animal import Animal

class Mamifero(Animal):
    _listado: list = []
    caballos: int = 0
    leones: int = 0

    def __init__(self, nombre, edad, habitat, genero, zona = None,
                 pelaje = None, patas = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        if pelaje: 
            self._pelaje = pelaje
        if patas:
            self._patas = patas
        self._listado.append(self)

    def getListado(self):
        return self._listado
    def setListado(self, listado):
        self._listado = listado

    def getPelaje(self):
        return self._pelaje
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas
    def setPatas(self, patas):
        self._patas = patas

    @staticmethod
    def cantidadMamiferos(self):
        return Mamifero._totalAnimales

    @staticmethod
    def crearCaballo(nombre, edad, genero, zona = None):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, zona,
                 True, 4)

    def crearLeon(nombre, edad, genero, zona = None):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, zona,
                 True, 4)
