# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:44:21 2022

@author: Lara
"""

from modulos.Nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0
    
    def __iter__(self):
        nodo = self.cabeza
        while nodo is not None:
            yield nodo
            nodo = nodo.siguiente
    
    def __str__(self):
        lista = [nodo for nodo in self]
        return str(lista)
    
    @property
    def cabeza(self):
        """getter de cabeza"""
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self, valor):
        """setter de cabeza"""
        self._cabeza = valor
        
    @property 
    def cola(self):
        """getter de cola"""
        return self._cola
    
    @cola.setter
    def cola(self, valor):
        """setter de cola"""
        self._cola = valor
    
    def estaVacia(self):
        """Devuelve True si la lista está vacía"""
        return self._tamanio == 0
    
    @property
    def tamanio(self):
        """Devuelve el tamaño de la lista"""
        return self._tamanio
    
    def agregar(self, item):
        """Agrega un nuevo ítem al inicio de la lista."""
        nodo = Nodo(item)
        
        if self.estaVacia():
            self.cola = nodo
            self.cabeza = nodo
            
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo
            
        self._tamanio +=1
        
    def anexar(self, item):
        """Agrega un nuevo ítem al final de la lista."""
        nodo = Nodo(item)
        
        if self.estaVacia():
            self.cola = nodo
            self.cabeza = nodo
            
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
            
        self._tamanio +=1        
        
    def insertar(self, posicion, item):
        """Agrega un nuevo ítem a la lista en "posicion"."""
        nodo = Nodo(item)
        
        if(posicion >= 0 and posicion <= self.tamanio):
            
            if(posicion == 0):
                self.agregar(item)
            
            elif(posicion == self.tamanio):
                self.anexar(item)
                
            elif(posicion > 0 and posicion < self.tamanio):
                nodo_aux = self.cabeza
                for i in range (posicion - 1):
                    nodo_aux = nodo_aux.siguiente
                nodo.siguiente = nodo_aux.siguiente
                nodo_aux.siguiente.anterior = nodo
                nodo.anterior = nodo_aux
                nodo_aux.siguiente = nodo
                
                self._tamanio +=1
                
        else:
            raise Exception ("No existe la posición asignada.")
        
    def extraer(self, posicion = None):
        """elimina y devuelve el ítem en "posición". Si no se indica el parámetro posición, se elimina 
        y devuelve el último elemento de la lista."""
        
        if(posicion == None or posicion >= 0 and posicion < self._tamanio or posicion == -1):
            
            if(posicion == None or posicion == self.tamanio - 1 or posicion == -1):
                item_aeliminar = self.cola
                self.cola.anterior.siguiente = None
                self.cola = self.cola.anterior
            
            elif (posicion == 0):
                item_aeliminar = self.cabeza
                self.cabeza.siguiente.anterior = None
                self.cabeza = self.cabeza.siguiente
                
            elif(posicion > 0 and posicion < self.tamanio-1):
                item_aeliminar = self.cabeza
                for i in range (posicion):
                    item_aeliminar = item_aeliminar.siguiente
                item_aeliminar.siguiente.anterior = item_aeliminar.anterior
                item_aeliminar.anterior.siguiente = item_aeliminar.siguiente
                
            self._tamanio -= 1
            return item_aeliminar
        
        else:
            raise Exception ("La posición no puede ser menor que cero o se encuentra fuera de la cantidad de elementos de la lista")

    def copiar(self):
        """Realiza una copia de la lista elemento a elemento y devuelve la copia."""
        copia_lista = ListaDobleEnlazada()
        
        if(self.estaVacia()):
            return copia_lista
        
        else:
            aux = self.cabeza
            
            while aux:
                copia_lista.anexar(aux.dato)
                aux = aux.siguiente
            
        return copia_lista
    
    def invertir(self):
        """Invierte el orden de los elementos de la lista."""
        lista_invertida = ListaDobleEnlazada()
        
        if(self.estaVacia()):
            return lista_invertida
        
        else:
            aux = self.cabeza
            for i in range(self._tamanio):
                lista_invertida.agregar(aux.dato)
                aux = aux.siguiente
                
            self.cabeza = lista_invertida.cabeza
            self.cola = lista_invertida.cola
            self = lista_invertida.copiar()
    
    def insertarOrdenado(self, nodo):
        """Inserta el nodo ordenado"""
        cabeza = self.cabeza
        p = None
        
        if(cabeza == None or cabeza.dato > nodo.dato):
            nodo.siguiente = cabeza
            cabeza = nodo
            
        else:
            p = cabeza
            
            while(p.siguiente and p.siguiente.dato < nodo.dato):
                p = p.siguiente
            nodo.siguiente = p.siguiente
            p.siguiente = nodo
            
        self.cabeza = cabeza
    
    def ordenar(self):
        """Ordena los elementos de la lista de menor a mayor"""
        if(self.estaVacia()):
            raise Exception ("La lista está vacía")
            return self
        
        lista_ordenada = ListaDobleEnlazada()
        aux = self.cabeza
        p = aux
        
        while p:
            siguiente = p.siguiente
            lista_ordenada.insertarOrdenado(p)
            p = siguiente
            
        aux = lista_ordenada.cabeza
        self.cabeza = aux
        del lista_ordenada
            
                
    def concatenar(self, Lista):
        """Recibe una lista como argumento y retorna la lista actual con la lista pasada como 
        parámetro concatenada al final de la primera. Esta operación también debe ser posible 
        utilizando el operador de suma ‘+’."""
        if(Lista.tamanio == 0):
            raise Exception ("La lista recibida está vacía")
            return self
        
        self.cola.siguiente = Lista.cabeza
        Lista.cabeza.anterior = self.cola
        self.cola = Lista.cola
            
        self._tamanio += Lista.tamanio
        
        return self