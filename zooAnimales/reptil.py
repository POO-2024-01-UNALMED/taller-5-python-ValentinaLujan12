from animal import Animal

class Reptil(Animal):
    _listado: list = []
    iguanas: int = 0
    serpientes: int = 0

    def __init__(self, nombre, edad, habitat, genero, zona = None,
                 colorEscamas = None, largoCola = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        if colorEscamas:
            self._colorEscamas = colorEscamas
        if largoCola:
            self._largoCola = largoCola
        self._listado.append(self)

    def getListado(self):
        return self._listado
    def setListado(self, listado):
        self._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self, largo):
        self._largoCola = largo

    @staticmethod
    def cantidadReptiles():
        return Reptil._totalAnimales

    def movimiento(self):
        pass

    @staticmethod
    def crearIguana(nombre, edad, genero, zona = None):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, zona,
                 "verde", 3)

    def crearSerpiente(nombre, edad, genero, zona = None):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, zona,
                 "blanco", 1)