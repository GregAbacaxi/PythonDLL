# Gregor U.
# 30/SEP/2024

# Private Class Node
class _Node:
    # Constructor
    def __init__(self, nxt, prv, val) :
        self.next = nxt
        self.prev = prv
        self.value = val

    # Get & Set Next
    def getNext(self) :
        return self.next
    def setNext(self, nxt) :
        self.next = nxt

    # Get & Set Previous
    def getPrev(self) :
        return self.prev
    def setPrev(self, prv) :
        self.prev = prv

    # Get & Set Value
    def getValue(self) :
        return self.value
    def setValue(self, val) :
        self.value = val

# Public Class DoublyLinkedList
class DLL:
    # Constructor
    def __init__(self) :
        self.header = _Node(None,None,None)
        self.trailer = _Node(None,None,None)
        self.size = 0
        self.header.setNext(self.trailer)
        self.trailer.setPrev(self.header)

    # Override on len() to get the size
    def __len__(self) :
        return self.size
    
    # To know if the DLL is empty
    def isEmpty(self) :
        return self.size == 0
    
    # Gets First element or Last element
    def getFirst(self) :
        return self.header.getNext()
    def getLast(self) :
        return self.trailer.getPrev()
    
    # Private function that adds a node between two existing nodes
    def _addBetween(self,val, pred, succ) :
        if ((pred.getNext() == succ) and (succ.getPrev() == pred)):
            n = _Node(succ,pred,val)
            pred.setNext(n)
            succ.setPrev(n)
            self.size += 1
            return True
        else :
            return False
        
    # Add a new element to the "head / start / top" of the DLL
    def addFirst(self, val) :
        return self._addBetween(val, self.header,self.header.getNext())
    
    # Add a new element to the "tail / end / bottom" of the DLL
    def addLast(self, val) :
        return self._addBetween(val, self.trailer.getPrev(), self.trailer)
    
    # Private function to remove one given node
    def _removeNode(self, node) :
        p = node.getPrev()
        s = node.getNext()
        p.setNext(s)
        s.setPrev(p)
        self.size -= 1
        return node.getValue()
    
    # Removes the element at the "head / start / top" of the DLL (if possible)
    def removeFirst(self) :
        if (self.isEmpty()) :
            return None
        return self._removeNode(self.header.getNext())
    
    # Removes the element at the "tail / end / bottom" of the DLL (if possible)
    def removeLast(self) :
        if (self.isEmpty()) :
            return None
        return self._removeNode(self.trailer.getPrev())
    
    # Removes all elements from the DLL
    def removeAll(self) :
        while (not self.isEmpty()) :
            self.removeFirst()

    # Returns an array with the contents of the DLL
    def show(self) :
        out = []
        if (not self.isEmpty()) : 
            curr = self.header.getNext()
            while (curr != self.trailer) :
                out.append(curr.getValue())
                curr = curr.getNext()
        return out
    
    # Absorbs an array. Clearing the DLL and then adding the elements of the array, in the same order, to the DLL
    def absorb(self, arr) :
        if (not self.isEmpty) :
            self.removeAll()
        for n in arr :
            self.addLast(n)
