class Movie:

    def __init__(self, title, director):
        self.title = title
        self.director = director

    def __str__(self):
        return '%s, %s' % (self.title, self.director)

 
class DummyMovieFinder:

    def __init__(self, filename):
        print ('Loading movies from: %s' % (filename))
        self.movies = (
            Movie("Once Upon a Time in the West", "Sergio Leone"),
            Movie("Dances With Wolves", "Kevin Costner")
        )
 
    def find_all(self):
        return self.movies

 
class MovieLister:

    def __init__(self):
        self.finder = DummyMovieFinder("western_library.txt")
 
    def moviesDirectedBy(self, director):
        return [movie for movie in self.finder.find_all() if movie.director == director]

 
if __name__ == '__main__':
    lister = MovieLister()
    movies = lister.moviesDirectedBy("Sergio Leone")
    print ('\n'.join(map(str, movies)))
