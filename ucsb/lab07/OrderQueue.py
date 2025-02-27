class QueueEmptyException(Exception):
    pass

class OrderQueue:
    def __init__(self):
        self.heapList = [None]
        self.currentSize = 0

    def percUp(self, i):
        # "Percolate Up" (Aufsteigen): Bewegt das Element an Index i nach oben,
        # falls dessen Versanddistanz größer ist als die seines Elternteils.
        while i // 2 > 0:
            # Vergleiche die Versanddistanz des aktuellen Elements mit der des Elternteils.
            if self.heapList[i].distance > self.heapList[i // 2].distance:
                # Tausche das aktuelle Element mit seinem Elternteil, wenn es eine höhere Versanddistanz hat.
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def addOrder(self, teaOrder):
        # Fügt einen neuen Teeauftrag zur Auftragswarteschlange hinzu.
        # Der Auftrag wird an der ersten freien Stelle im Heap eingefügt,
        # danach wird 'percUp' aufgerufen, um die MaxHeap-Eigenschaft wiederherzustellen.
        self.heapList.append(teaOrder)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def maxChild(self, i):
        # Liefert den Index des Kindes, das die höhere Versanddistanz hat.
        # Wenn nur ein Kind existiert, wird dessen Index zurückgegeben.
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2].distance >= self.heapList[i * 2 + 1].distance:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        # "Percolate Down" (Absteigen): Bewegt das Element an Index i nach unten,
        # falls dessen Versanddistanz kleiner ist als die eines seiner Kinder.
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i].distance < self.heapList[mc].distance:
                # Tausche das aktuelle Element mit dem Kind, das die höhere Versanddistanz hat.
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def processNextOrder(self):
        # Entfernt und verarbeitet den nächsten Auftrag aus der Warteschlange,
        # welcher den höchsten Versanddistanzwert besitzt.
        if self.currentSize == 0:
            raise QueueEmptyException("Die Auftragswarteschlange ist leer!")
        # Speichere das Wurzelelement (Auftrag mit maximaler Versanddistanz)
        rootOrder = self.heapList[1]
        # Ersetze das Wurzelelement durch das letzte Element in der Liste
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()  # Entferne das letzte Element (jetzt redundant)
        # Stelle die MaxHeap-Eigenschaft wieder her, indem das Element nach unten "absteigt"
        self.percDown(1)
        # Gib die Auftragsbeschreibung des entfernten Auftrags zurück
        return rootOrder.getOrderDescription()
