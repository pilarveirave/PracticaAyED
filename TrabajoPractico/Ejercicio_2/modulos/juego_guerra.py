from modulos.LDE.Ejercicio1 import LDE


class Jugador:
    def __init__(self):
        self._mazo #LDE
        pass
        
    @property
    def mazo(self):
        return self.mazo
    
    
class JuegoGuerra:
    
    def __init__(self):
        self.turnos_jugados = 0
        self.jugador1 = Jugador()
        self.jugador2 = Jugador()
    
    def iniciar_juego(self):
        pass