from MovieCollectionNode import MovieCollectionNode
from Movie import Movie

class MovieCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if not self.head else False

    def getNumberOfMovies(self):
        return self.head.count() if self.head else 0

    def insertMovie(self, movie):
        ins = MovieCollectionNode(movie)
        if not self.head:
            self.head = ins
            return
        if self.head.getData() > movie:
            ins.setNext(self.head)
            self.head = ins
            return
        self.head.setNext(ins)
        return

    def getAllMoviesInCollection(self):
        if self.head:
            return self.head.printCollection()
        return

    def getMoviesByDirector(self, director):
        return self.head.getByDirector(director)

    def removeDirector(self, director):
        self.head = self.head.removeDirector(director)

    def avgDirectorRating(self, director):
        result = [x for x in self.head.avgRating(director) if x is not None]
        return round(sum(result) / len(result), 2) if result else None

    def recursiveSearchMovie(self, movie, movieNode):
        return movieNode.searchMovie(movie)

