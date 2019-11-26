from abc import ABC, abstractmethod

class PaquetesEnviados(ABC):

    @abstractmethod
    def Lista(self):
        pass

class FamiliarMexico(PaquetesEnviados):
    def Lista(self):
        print("Manda una lista de las cosas que quiere que le manden sus parientes de USA (video juegos, Dinero, Productos agricolas)")
        
class AjenteAduanaProxy(PaquetesEnviados):
     def __init__(self,familiar_mexico:FamiliarMexico):
        self._FamiliarMexico = FamiliarMexico()

     def Lista(self):

        if self.validarPaquetes():
            self._FamiliarMexico.Lista()
            self.pasarPaquetes()

     def validarPaquetes(self):
        print("la gente de la aduana solo valida los paquetes que sean legales pasar a México")
        return True

     def pasarPaquetes (self):
        print("se decomisan los paquetes de Productos agricolas")

def PersonaMexico(PaquetesEnviados):
    PaquetesEnviados.Lista()

if __name__ == "__main__":
    print("Lo que manda la familia de Mexico")
    Familiar = FamiliarMexico()
    PersonaMexico(Familiar)

    print("Lo que deja pasar la aduana a territorio Mexicano")
    print("la gente de la aduana solo valida los paquetes que sean legales pasar a México")
    print("se decomisan los paquetes de Productos agricolas")
    
