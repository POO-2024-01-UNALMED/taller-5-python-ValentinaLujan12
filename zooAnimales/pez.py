from animal import Animal

class Pez(Animal):
    _listado: list
    salmones: int = 0
    bacalaos: int = 0

    def __init__(self, nombre, edad, habitat, genero, zona = None,
                 colorEscamas = None, cantidadAletas = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        if colorEscamasself._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getListado(self):
        return self._listado
    def setListado(self, listado):
        self._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad

    def cantidadPeces(self):
        pass

    def movimiento(self):
        pass

    def crearIguana(self):
        pass

    def crearSerpiente(self):
        pass