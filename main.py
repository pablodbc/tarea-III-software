# -*- encoding: utf-8 -*-
'''
Created on 1 feb. 2017

@author: carlos
'''
from datetime import *

class Registro:
    def __init__(self, monto, fecha, localID):
        self.monto = monto
        self.fecha = fecha
        self.localID = localID

    def __str__(self):
        return "\nMonto: "+str(self.monto)+"\nFecha: "+str(self.fecha)+"\nEstablecimiento: "+str(self.localID)+"\n"

class BilleteraElectronica:
    def __init__(self, identificador, nombres, apellidos, CI, PIN, balance = 0):
        self.identificador = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        assert(CI >=0)
        self.CI = CI
        self.PIN = PIN
        self.recargas = []
        self.consumos = []
        self.balance = balance

    def recargar(self, monto, fecha = datetime.now(), localID):
        self.recargas += [Registro(monto, fecha, localID)]
        self.balance += monto

    def consumir(self, PIN, monto, fecha = datetime.now(), localID):
        if self.PIN == PIN:
            if self.balance >= monto:
                self.consumos += [Registro(monto, fecha, localID)]
                self.balance -= monto

            else:
                print("No hay suficiente crédito para llevar acabo la operación")

        else:
            print("El número de PIN no coincide con el registrado en la billetera")

    def saldo(self):
        return self.balance

if __name__ == '__main__':
    pass