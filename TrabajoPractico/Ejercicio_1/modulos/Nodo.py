# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:42:51 2022

@author: Lara
"""

class Nodo:
    def __init__(self, datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return str(self.dato)
        
    def __repr__(self):
        return str(self.dato)
        
    @property
    def siguiente(self):
        """getter de siguiente"""
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nuevoSiguiente):
        """setter de siguiente"""
        self._siguiente = nuevoSiguiente
    
    @property
    def anterior(self):
        """getter de anterior"""
        return self._anterior
    
    @anterior.setter
    def anterior(self, valor):
        """setter de anterior"""
        self._anterior = valor
        
    @property
    def dato(self):
        """getter del dato"""
        return self._dato

    @dato.setter
    def dato(self, nuevodato):
        """setter del dato"""
        self._dato = nuevodato
        
    
