class MovieLister:

    def __init__(self, finder):
        self.finder = finder
 
    def moviesDirectedBy(self, director):
        return [movie for movie in self.finder.find_all() if movie.director == director]


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

 
class Assembler:

    def __init__(self):
        finder = DummyMovieFinder("western_library.txt")
        self.lister = MovieLister(finder)


class Container:

    def __init__(self, system_data):
        for component_name, component_class, component_args in system_data:
            if component_args != None:
                args = [self.__dict__[arg] for arg in component_args]
                self.__dict__[component_name] = component_class(*args)
            else:
                self.__dict__[component_name] = component_class

 
if __name__ == '__main__':
    SYSTEM_DATA = (
        ('filename', 'western_library.txt', None),
        ('finder', DummyMovieFinder, ('filename',)),
        ('lister', MovieLister, ('finder',)),
    )
 
    c = Container(SYSTEM_DATA)
    movies = c.lister.moviesDirectedBy("Sergio Leone")
    print ('\n'.join(map(str, movies)))
