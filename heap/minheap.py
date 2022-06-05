#Implementing min heap in python
class MinHeap:
    def __init__(self, heapSize):
        #Create a complete binary tree using array
        self.heapSize = heapSize
        #creating list of size heapsize + 1
        self.minheap = [0] * (heapSize + 1)
        #realsize will maintain actual number of contents
        self.realSize = 0

    #Function to add a element into heap
    def add(self, element):
        self.realSize += 1
        if self.realSize > self.heapSize:
            print("Exceeding heap size")
            self.realSize -= 1
            return
        self.minheap[self.realSize] = element
        index = self.realSize
        #Parent node index calculation
        parent = index // 2
