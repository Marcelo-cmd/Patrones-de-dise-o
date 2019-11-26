from abc import ABC, abstractmethod

class PaquetesEnviados(ABC):

    @abstractmethod
    def Lista(self):
        pass

class FamiliarMexico(PaquetesEnviados):
    def Lista(self):
        pass
        
class AjenteAduanaProxy(PaquetesEnviados):
     def __init__(self,familiar_mexico:FamiliarMexico):
        self._FamiliarMexico = FamiliarMexico()

     def Lista(self):

        if self.validarPaquetes():
            self._FamiliarMexico.Lista()
            self.pasarPaquetes()

     def validarPaquetes(self):
        
        return True

     def pasarPaquetes (self):
        pass

def PersonaMexico(PaquetesEnviados):
    PaquetesEnviados.Lista()

if __name__ == "__main__":
    
    Familiar = FamiliarMexico()
    PersonaMexico(Familiar)

    
    
