class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size= 0
        self.data= [0]*capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError('Index invalid')
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError('Index invalid')
        self.data[i] = n
    
    def pushback(self, n: int) -> None:
        if self.size==self.capacity:
          self.resize()
        self.data[self.size] = n  
        self.size += 1  

    
    def popback(self) -> int: 
       self.size-=1
       prof = self.data[self.size]
       return prof

    def resize(self) -> None:
      self.capacity= self.capacity*2
      new = [0] * self.capacity
      for i in range(self.size):
        new[i]=self.data[i]
      self.data= new  

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity