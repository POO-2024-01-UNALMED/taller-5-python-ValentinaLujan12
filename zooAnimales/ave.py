from animal import Animal

class Ave(Animal):
    _listado: list = []
    halcones: int = 0
    aguilas: int = 0
    def __init__(self, nombre, edad, habitat, genero, zona = None,
                 colorPlumas = None) -> None:
        super().__init__(nombre, edad, habitat, genero, zona)
        if colorPlumas:
            self._colorPlumas = colorPlumas
        self._listado.append(self)

    def getListado(self):
        return self._listado
    def setListado(self, listado):
        self._listado = listado

    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, color):
        self._colorPlumas = color

    @staticmethod
    def cantidadAves():
        return Ave._totalAnimales

    def movimiento(self):
        pass

    def crearHalcon(nombre, edad, genero, zona = None):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, zona,
                 "café glorioso")

    def crearAguila(nombre, edad, genero, zona = None):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, zona,
                 "blanco y amarillo")