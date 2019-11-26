
from types import MethodType
from abc import ABC, abstractmethod

class EstudianteEstratega(ABC): 
    def __init__(self, *args, **kwargs):
        self.Nombre = None
        
        self.MetodoEstudio = None
    def MetodoEstudio(self):
        pass
class Asesorias(EstudianteEstratega):  
    def metodoEstudio_Asistir_A_Asesorias(self):
        pass   
class VideosYoutube(EstudianteEstratega):  
    def metodoEstudio_Ver_VideosYoutube(self):
        pass
    
class LeerLibros(EstudianteEstratega):
    def metodoEstudio_LeerLibros(self):
        pass
    
class RepasarApuntes(EstudianteEstratega):
    def metodoEstudio_RepasarApuntes(self):
        pass
    
class Examen(EstudianteEstratega): 
    def Examenprogramacion(self):
        pass
