# /algo_practice/binary_heap.py

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.__percolate_up(len(self.heap)-1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def remove_max(self):
        if len(self.heap) > 1:
            max_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(0)
            return max_value
        
        elif len(self.heal) == 1:
            max_value = self.heap[0]
            del self.heap[0]
            return max_value

        else:
            return None

    def __percolate_up(self, index):
        parent = (index-1)//2

        if index <= 0:
            return

        elif self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.__percolate_up(parent)
        
    def __max_heapify(self, index):
        left = (index*2) + 1
        right = (index*2) + 2 
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__max_heapify(largest)


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.__percolate_up(len(self.heap)-1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def remove_min(self):
        if len(self.heap) > 1:
            min_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__min_heapify(0)
            return min_value

        elif len(self.heap == 1):
            min_value = self.heap[0]
            del self.heap[0]
            return min_value

        else:
            return None

    def __percolate_up(self, index):
        parent = (index-1) // 2
        if index <= 0:
            return

        elif self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.__percolate_up(parent)

    def __min_heapify(self, index):
        left = (index*2) + 1
        right = (index*2) + 2
        smallest = index

        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left

        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.__min_heapify(smallest)

if __name__ == '__main__':
    heap = MaxHeap()

    heap.insert(1)
    heap.insert(10)
    heap.insert(12)
    heap.insert(4)

    print(heap.get_max())

    heap.remove_max()

    print(heap.get_max())

    heap = MinHeap()

    heap.insert(1)
    heap.insert(10)
    heap.insert(12)
    heap.insert(4)

    print(heap.get_min())

    heap.remove_min()

    print(heap.get_min())
