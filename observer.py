import abc
from abc import ABC, abstractmethod
class Seguidor:

    def __init__(self):
        self.cuentas = set()
        self.estado_seguidor = None

    def attach(self, cuentaYoutube):
        cuentaYoutube.seguidor = self
        self.cuentas.add(cuentaYoutube)

    def detach(self, cuentaYoutube):
        cuentaYoutube.seguidor = None
        self.cuentas.discard(cuentaYoutube)

    def notificar(self):
        for cuentaYoutube in self._cuentas:
            observer.update(self.estado_seguidor)

    @property
    def estado_seguidor(self):
        return self.estado_seguidor

    @estado_seguidor.setter
    def estado_seguidor(self, arg):
        self.estado_seguidor = arg
        self.notificar()

class CuentaYoutube(metaclass=abc.ABCMeta):

    def __init__(self):
        self.notificarSeguidores = None

    @abc.abstractmethod
    def update(self, arg):
        pass

class Marcelo(CuentaYoutube):

    def update(self, arg):
        self.estado_cuenta = arg
        self.notificarSeguidores = None

def main():
    seguidor = Seguidor()
    marcelo = Marcelo()
    seguidor.attach(marcelo)
    seguidor.estado_seguidor = ""
