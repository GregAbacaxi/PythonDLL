# Gregor U.
# 30/SEP/2024

# Importing the DLL
from Lists import *

# Testing the DLL's methods
lista = DoublyLinkedList.DLL()
lista.addFirst(3)
lista.addFirst(2)
lista.addLast(5)
lista.addLast(8)
print('\nDLL : {}'.format(lista.show()))
backup = lista.show()
print('Current First : {} \nCurrent Last : {} '.format(lista.getFirst().getValue(), lista.getLast().getValue()))
print('Size : {} \n'.format(len(lista)))
lista.removeFirst()
lista.removeLast()
print('DLL : {} '.format(lista.show()))
print('Current First : {} \nCurrent Last : {} '.format(lista.getFirst().getValue(), lista.getLast().getValue()))
print('Size : {} \n'.format(len(lista)))
lista.removeAll()
print('DLL : {}'.format(lista.show()))
print('Is it empty? {} \n'.format(lista.isEmpty()))
lista.absorb(backup)
print('DLL : {}'.format(lista.show()))
print('Is it empty? {} \n'.format(lista.isEmpty()))