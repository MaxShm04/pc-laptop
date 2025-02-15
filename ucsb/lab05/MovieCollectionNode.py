class MovieCollectionNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, NewData):
        self.data = NewData

    def setNext(self, newNode):
        if not self.getNext():
            self.next = newNode
            return

        if self.getNext().getData() > newNode.getData():
            newNode.setNext(self.getNext())
            self.next = newNode
        else:
            self.getNext().setNext(newNode)

    def printCollection(self):
        if self.getNext():
            return self.getData().getMovieDetails() + "\n" + self.getNext().printCollection()
        return self.getData().getMovieDetails() + "\n"

    def count(self):
        if self.next:
            return 1 + self.next.count()
        return 1

    def getByDirector(self, director):
        if self.getData().getDirector().upper() == director.upper():
            return self.getData().getMovieDetails() + "\n" + self.getNext().getByDirector(director) if self.getNext() else self.getData().getMovieDetails() + "\n"
        return self.getNext().getByDirector(director) if self.getNext() else ""

    def removeDirector(self, director):
        if not self.getNext():
            if self.getData().getDirector().upper() == director.upper():
                return None
            return self

        self.next = self.getNext().removeDirector(director)
        if self.getData().getDirector().upper() == director.upper():
            return self.next
        return self

    def avgRating(self, director):
        if self.next:
            result = self.getNext().avgRating(director)
            if self.getData().getDirector().upper() == director.upper():
                result.append(self.getData().getRating())
            return result
        else:
            if self.getData().getDirector().upper() == director.upper():
                return [self.getData().getRating()]
        return []

    def searchMovie(self, movie):
        if self.getData().getMovieName().upper() == movie.upper():
            return True
        return self.getNext().searchMovie(movie) if self.getNext() else False