from datetime import datetime


class MinHeap:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.size = 0
        self.heap = [ float("inf") for _ in range(capacity)]
        
    def getParentIndex(self, index):
        return (index - 1)//2 if index >0 else -1

    def getLeftChildIndex(self, index):
        return 2*index + 1

    def getRightChildIndex(self, index):
        return 2*index + 2
    
    def incCapacity(self):
        self.heap = self.heap + [ float("inf") for _ in range(self.capacity)]
        self.capacity *= 2
    
    def insert(self, data):
        if self.size == self.capacity:
            self.incCapacity()
        self.heap[self.size] = data
        p = self.getParentIndex(self.size)
        i = self.size
        while p>=0 and self.heap[p] > self.heap[i]:
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
                i = p
                p = self.getParentIndex(i)
                
        self.size += 1 
    
    def minChild(self, index):
        l = self.getLeftChildIndex(index)
        r = self.getRightChildIndex(index)
        if l < self.capacity and r < self.capacity:
            if self.heap[l] > self.heap[r] :
                return r
            else:
                return l
        else:
            return index 
        
    def peek(self):
        return self.heap[0]
    
    def removeAt(self, index):
        if index > self.size :
            return None
        popped = self.heap[index]
        self.heap[index] = self.heap[self.size - 1]
        self.heap[self.size - 1] = float('inf')
        i = self.minChild(index)
        j = index
        while self.heap[i] < self.heap[j]:
            self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
            j = i
            i = self.minChild(j)
        self.size -= 1
        return popped
    
    def pop(self):
        return self.removeAt(0)
    
    def remove(self, data):
        if data < self.heap[0]:
            return
        i = self.heap.index(data)
        self.removeAt(i)
        return 
        # # for i in range(self.size):
        # #     if data == self.heap[i]:
        # #         self.removeAt(i)
        # #         break
        # k = 0
        # for i in self.heap:
        #     if data == i:
        #         self.removeAt(k)
        #         break
        #     k += 1
    

def dispRunTime(fun):
    def run():
        start = datetime.now().timestamp()
        fun()
        end = datetime.now().timestamp()
        print((end - start)," seconds")
    return run

@dispRunTime
def main():
    file = open("input08.txt")
    inp = file.readline()
    p = int(inp)
    dh = MinHeap()
    for _ in range(p):
        query = list(map(int, str(file.readline()).split(" ")))
        match query[0]:
            case 3:
                print(dh.peek())
            case 1:
                dh.insert(query[1])
            case 2:
                dh.remove(query[1])
                

if __name__ == "__main__":
    main()