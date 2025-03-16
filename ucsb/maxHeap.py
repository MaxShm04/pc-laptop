class minHeap:

    def __init__(self):
        self.heap = [-1]
        self.size = 0

    def insert(self, int):
        self.heap.append(int)
        self.size += 1
        self.percUp(self.size)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] > self.heap[i]:        #swap here for maxHeap
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2

    def delMin(self):
        rmv = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percDown(1)
        return rmv

    def percDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heap[mc] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def minChild(self, i):
        if self.size >= 2*i + 1:
             if self.heap[2*i] > self.heap[2*i + 1]:
                return 2*i + 1
        return 2*i


def test_BinHeap():
    bh = minHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    assert bh.delMin() == 3
    assert bh.delMin() == 5
    assert bh.delMin() == 7
    assert bh.delMin() == 11


class maxHeap:

    def __init__(self):
        self.heap = [-1]
        self.size = 0

    def insert(self, i):
        self.heap.append(i)
        self.size += 1
        self._insert(self.size)

    def _insert(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] < self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2

    def delMax(self):
        rmv = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self._remove(1)
        return rmv

    def _remove(self, i):
        while self.size >= 2*i:
            mc = self.maxChild(i)
            if self.heap[mc] > self.heap[i]:
                self.heap[mc], self.heap[i] = self.heap[i], self.heap[mc]
            i = mc

    def maxChild(self, i):
        if self.size >= 2*i+1:
            if self.heap[2*i+1]>self.heap[2*i]:
                return 2*i+1
        return 2*i

def test_MaxHeap():
    mh = maxHeap()
    mh.insert(5)
    mh.insert(7)
    mh.insert(3)
    mh.insert(11)
    assert mh.delMax() == 11
    assert mh.delMax() == 7
    assert mh.delMax() == 5
    assert mh.delMax() == 3
