import sys

class MaxHeap:

    def __init__(self, size):
        self.realSize = 0
        self.heapSize = size
        self.maxheap = [0]*(self.heapSize+1)

    def add(self, element):
        if (self.realSize + 1)>self.heapSize:
            print("Exceeding Heap Size")
            return
        self.realSize += 1
        self.maxheap[self.realSize] = element
        index = self.realSize
        parent = index // 2
        while self.maxheap[parent]<self.maxheap[index] and index != 1:
            self.maxheap[parent],self.maxheap[index]=self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2

    def peek(self):
        print(self.maxheap[1])
        return self.maxheap[1]

    def pop(self):
        if self.realSize==0:
            return
        print(f"Popped element : {self.maxheap[1]}")
        removedElement = self.maxheap[1]
        self.maxheap[1]=self.maxheap[self.realSize]
        self.realSize-=1
        index = 1
        while(index <= self.realSize // 2):
            left = index*2
            right = index*2 + 1
            if (self.maxheap[index]<self.maxheap[left] or self.maxheap[index]<self.maxheap[right]):
                if self.maxheap[left]>self.maxheap[right]:
                    self.maxheap[left],self.maxheap[index] = self.maxheap[index], self.maxheap[left]
                    index = left
                else:
                    self.maxheap[right],self.maxheap[index] = self.maxheap[index], self.maxheap[right]
                    index = right
            else:
                break
        return removedElement

    def __str__(self):
        return str(self.maxheap[1:self.realSize+1])

if __name__ == "__main__":

        # Test cases
        maxheap = MaxHeap(5)
        maxheap.add(3)
        maxheap.add(1)
        maxheap.add(2)
        # [1,3,2]
        print(maxheap)
        # 1
        print(maxheap.peek())
        # 1
        print(maxheap.pop())
        # 2
        print(maxheap.pop())
        # 3
        print(maxheap.pop())
        maxheap.add(4)
        maxheap.add(5)
        # [4,5]
        print(maxheap)

