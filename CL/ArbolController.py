from BL.ArbolBinario import ArbolBinario
from BL.Nodo import Nodo


class ArbolController(object):
    def __init__(self):
        self.arbol = ArbolBinario()
        self.cont = 0

    def agregarNodo(self, info):
        nodo = Nodo(info)
        if self.cont == 0:
            self.arbol.inicializarRoot(info)
            self.cont = self.cont+1
        else:
            self.arbol.insert(self.arbol.root, nodo)

    def obtenerInOrden(self):
        return self.arbol.inOrden()

    def obtenerPreOrden(self):
        return self.arbol.preOrden()

    def obtenerPostOrden(self):
        return self.arbol.postOrden()