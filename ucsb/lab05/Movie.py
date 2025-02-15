class Movie:
    def __init__(self, movieName, director, year, rating=None):
        self.rating = rating
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = year
    def getMovieName(self):
        return self.movieName

    def getDirector(self):
        return self.director

    def getYear(self):
        return self.year

    def getRating(self):
        return self.rating

    def getMovieDetails(self):
        directorName = self.getDirector().split(", ")[1] + " " + self.getDirector().split(",")[0]
        return f"{self.getMovieName().upper()} directed by {directorName.upper()} ({self.year}), Rating: {self.rating}"

    def __gt__(self, rhs):  #größer weiter unten
        return True if self.director.upper() > rhs.director.upper() else True if self.year > rhs.year and self.director.upper() == rhs.director.upper() else True if self.movieName > rhs.movieName and self.director.upper() == rhs.director.upper() and self.year == rhs.year else False
