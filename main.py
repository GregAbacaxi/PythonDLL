# Gregor U.
# 17/FEB/2024

# Importing the DLL
from Lists import *

# Testing the DLL's methods
lista = DoublyLinkedList.DLL()
lista.addFirst(3)
lista.addFirst(2)
lista.addLast(5)
lista.addLast(8)
print('\nArray : {} '.format(lista.show()))
backup = lista.show()
print('Current First : {} \nCurrent Last : {} \n'.format(lista.getFirst().getValue(), lista.getLast().getValue()))
lista.removeFirst()
lista.removeLast()
print('Array : {} '.format(lista.show()))
print('Current First : {} \nCurrent Last : {} \n'.format(lista.getFirst().getValue(), lista.getLast().getValue()))
lista.removeAll()
print('Array : {}'.format(lista.show()))
print('Is it empty? {} \n'.format(lista.isEmpty()))
lista.absorb(backup)
print('Array : {}'.format(lista.show()))
print('Is it empty? {} \n'.format(lista.isEmpty()))