import pytest
from Movie import Movie
from MovieCollection import MovieCollection
from MovieCollectionNode import MovieCollectionNode

def test_movie_creation():
    m = Movie("INCEPTION", "Nolan, CHRISTOPHER", 2010, 8.8)
    assert m.getMovieName() == "INCEPTION"
    assert m.getDirector() == "NOLAN, CHRISTOPHER"
    assert m.getYear() == 2010
    assert m.getRating() == 8.8

def test_movie_default_rating():
    m = Movie("DUNE", "VILLENEUVE, DENIS", 2021)
    assert m.getRating() is None

def test_movie_details():
    m = Movie("TENET", "NOLAN, CHRISTOPHER", 2020, 7.5)
    assert m.getMovieDetails() == "TENET directed by CHRISTOPHER NOLAN (2020), Rating: 7.5"

def test_movie_comparison():
    m1 = Movie("MEMENTO", "NOLAN, CHRISTOPHER", 2000, 8.4)
    m2 = Movie("DUNKIRK", "NOLAN, CHRISTOPHER", 2017, 7.9)
    assert m2 > m1

def test_node_creation():
    m = Movie("THE PRESTIGE", "NOLAN, CHRISTOPHER", 2006, 8.5)
    node = MovieCollectionNode(m)
    assert node.getData() == m
    assert node.getNext() is None

def test_node_set_next():
    m1 = Movie("INTERSTELLAR", "NOLAN, CHRISTOPHER", 2014, 8.6)
    m2 = Movie("BATMAN BEGINS", "NOLAN, CHRISTOPHER", 2005, 8.2)
    node1 = MovieCollectionNode(m1)
    node2 = MovieCollectionNode(m2)
    node1.setNext(node2)
    assert node1.getNext() == node2

def test_collection_insert():
    mc = MovieCollection()
    assert mc.isEmpty()
    m = Movie("BLADE RUNNER 2049", "VILLENEUVE, DENIS", 2017, 8.0)
    mc.insertMovie(m)
    assert not mc.isEmpty()
    assert mc.getNumberOfMovies() == 1

def test_collection_order():
    mc = MovieCollection()
    m1 = Movie("ARRIVAL", "VILLENEUVE, DENIS", 2016, 7.9)
    m2 = Movie("SICARIO", "VILLENEUVE, DENIS", 2015, 7.6)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    assert "SICARIO" in mc.getAllMoviesInCollection().split('\n')[0]

def test_getMoviesByDirector():
    mc = MovieCollection()
    mc.insertMovie(Movie("DUNE", "VILLENEUVE, DENIS", 2021, 8.1))
    mc.insertMovie(Movie("PRISONERS", "VILLENEUVE, DENIS", 2013, None))
    mc.insertMovie(Movie("ARRIVAL", "SCHMITT, DENIS", 2016, 7.9))
    assert mc.getMoviesByDirector("VILLENEUVE, DENIS") == "PRISONERS directed by DENIS VILLENEUVE (2013), Rating: None\nDUNE directed by DENIS VILLENEUVE (2021), Rating: 8.1\n"
    assert mc.getMoviesByDirector("abc, def") == ""

def test_collection_remove_director():
    mc = MovieCollection()
    m1 = Movie("ENEMY", "VILLENEUVE, DENIS", 2013, 6.9)
    m2 = Movie("INCENDIES", "VILLENEUVE, DENIS", 2010, 8.3)
    m3 = Movie("INCENDIES", "SCHMITT, DENIS", 2010, 8.3)
    mc.insertMovie(m1)
    mc.insertMovie(m2)
    mc.insertMovie(m3)
    mc.removeDirector("VILLENEUVE, DENIS")
    assert not mc.isEmpty()
    mc.removeDirector("SCHMITT, DENIS")
    assert mc.isEmpty()

def test_collection_avg_rating():
    mc = MovieCollection()
    mc.insertMovie(Movie("DUNE", "VILLENEUVE, DENIS", 2021, 8.1))
    mc.insertMovie(Movie("PRISONERS", "VILLENEUVE, DENIS", 2013, None))
    mc.insertMovie(Movie("ARRIVAL", "VILLENEUVE, DENIS", 2016, 7.9))
    assert mc.avgDirectorRating("VILLENEUVE, DENIS") == 8.0
    assert mc.avgDirectorRating("NOLAN, CHRISTOPHER") is None
    mc.insertMovie(Movie("DUNE2", "VILLENEUVE, DENIS", 2024, 8.5))
    mc.insertMovie(Movie("DUNE3", "VILLENEUVE, DENIS", 2024, 8.5))
    assert mc.avgDirectorRating("VILLENEUVE, DENIS") == 8.25
    assert mc.avgDirectorRating("abc, def") is None

def test_collection_search():
    mc = MovieCollection()
    m = Movie("PRISONERS", "VILLENEUVE, DENIS", 2013, 8.1)
    mc.insertMovie(m)
    assert mc.recursiveSearchMovie("PRISONERS", mc.head)
    assert not mc.recursiveSearchMovie("INCEPTION", mc.head)