from typing import List

class Node:
   def __init__(self, val):
      self.val=val 
      self.next=None 

class LinkedList:
    
    def __init__(self):
      self.head=None
      self.tail=None
    
    def get(self, index: int) -> int:
        current=self.head
        i=0
        while current:
            if i==index:
                return current.val
            current=current.next
            i+=1
        return -1        

    def insertHead(self, val: int) -> None:
        val_actu=Node(val)
        val_actu.next=self.head
        self.head=val_actu
        if self.tail is None:
            self.tail=self.head
    
    def insertTail(self, val: int) -> None:
        val_actu=Node(val)
        if self.tail is None:
            self.tail=val_actu
            self.actu=val_actu
        else:     
          self.tail.next=val_actu
          self.tail=val_actu

    def remove(self, index: int) -> bool:
        if self.head is None :
            return False
        if  index ==0:
            self.head=self.head.next
            if self.head is None:
                self.tail=None
            return True
        current=self.head
        i=0
        while current.next:
            if i+1==index :
                current.next=current.next.next
                if current.next is None:
                    self.tail=current
                return True     
            current=current.next
            i+=1
        return False   

       
    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        return values
