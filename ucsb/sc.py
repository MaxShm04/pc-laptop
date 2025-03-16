class minheap:
    def __init__(self, x=None):
        if x is None:
            x = []
        self.heaplist = [0] + x
        self.currentsize = len(self.heaplist) -1

    def insert(self, x):
        self.heaplist.append(x)
        self.currentsize += 1
        self.percUp(self.currentsize)

    def percUp(self, i):
        while i > 1:
            if self.heaplist[i//2] < self.heaplist[i]:
                self.heaplist[i//2], self.heaplist[i] = self.heaplist[i], self.heaplist[i//2]
            i = i//2

    def out(self):
        print(self.heaplist)

    def remove(self, i):


h = minheap([5,3,4,1,0,2])
h.out()
h.insert(8)
h.out()
