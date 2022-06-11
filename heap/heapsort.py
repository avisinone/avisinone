import sys

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
        #traverse while parent in not shorter than element
        while(self.minheap[index] < self.minheap[parent] and index > 1):
            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            index = parent
            parent = index // 2

    #Function to peek the top element
    def peek(self):
        return self.minheap[1]

    #Function to pop the top element of Heap
    def pop(self):
        #Checking for empty heap
        if self.realSize < 1:
            print('Heap is empty, nothing to pop')
            return sys.maxsize
        else:
            removeElement = self.minheap[1]
            self.minheap[1] = self.minheap[self.realSize]
            self.realSize -= 1
            index = 1
            while(index <= self.realSize // 2):
                # the left child of the deleted element
                left = index * 2
                # the right child of the deleted element
                right = (index * 2) + 1
                # If the deleted element is larger than the left or right child
                # its value needs to be exchanged with the smaller value
                # of the left and right child
                if (self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]):
                    if self.minheap[left] < self.minheap[right]:
                        self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
                        index = left
                    else:
                        self.minheap[right], self.minheap[index] = self.minheap[index], self.minheap[right]
                        index = right
                else:
                    break
            return removeElement
                
    def size(self):
        return self.realSize

    def __str__(self):
        return str(self.minheap[1:self.realSize+1])


if __name__ == "__main__":
    	# Test cases
        minHeap = MinHeap(20)
        """minHeap.add(3)
        minHeap.add(1)
        minHeap.add(2)
        # [1,3,2]
        print(minHeap)
        # 1
        print(minHeap.peek())
        # 1
        print(minHeap.pop())
        # 2
        print(minHeap.pop())
        # 3
        print(minHeap.pop())
        minHeap.add(4)
        minHeap.add(5)"""
        # [4,5]
        #print(minHeap)
        a = [1,23,41,13,141,13221,43,2,52,-23,-342]
        length = len(a)
        for i in range(length):
            minHeap.add(a[i])
        while(minHeap.size()>0):
            print(f"{minHeap.pop()} ")
