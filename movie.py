# Import here the packages who are use in the file
# The package json is use to act in the file json
import json
# The package act on the directories processing
import os
# The package allows to define the errors message
import logging

# Here, we configure the format for message display with time, the nature, the message
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

# The function is use here, because with ui for display the movies from launch
def get_movies():
    # Here, open the file and read
    with open(DATA_FILE, "r") as f:
        # Variable for the data, because we will be used with other variable
        movies_titles = json.load(f)

    # Here, it's a list comprehension for optimization of code
    movie = [Movie(movie_title) for movie_title in movies_titles]
    # return her and no print because display with ui
    return movie

# Class creation
class Movie:
    # Method for initialization of instance with attribute title
    def __init__(self, title):
        # Definition title with method title, uppercase for every word
        self.title = title.title()

    # Method, which when we print a instance, return attribute title
    def __str__(self):
        return self.title

    # This method is use for read the file, the underscore is necessary because it's method for the class
    def _get_movies(self):
        # We use with for close the file after than reading finish
        with open(DATA_FILE, "r") as f:
            # Use return and no print because it's a method
            return json.load(f)

    # This method is use for writing in the file, same for underscore. The argument movies is necessary because it's a
    # set method and we must define the values
    def _write_movies(self, movies):
        # Here, we use "w" for writing in the file and delete the data before
        with open(DATA_FILE, "w") as f:
            # For dump, the first argument is the data for the file, the second argument is the file, the third is,
            # optional argument, indentation for the data
            json.dump(movies, f, indent=4)

    # This method lets add movie with method _get_movies and _write_movies, that is why there isn't movie an argument,
    # because it will be used with the instance
    def add_to_movie(self):
        # Here, we get movies in the file and register in a variable
        movies = self._get_movies()
        # Condition for check if the movie instance not exist in the file
        if self.title not in movies:
            # If no so add at the list movies
            movies.append(self.title)
            # And after add in the file, like that we find all the movies before and the recent
            self._write_movies(movies)
            # return True because there is a possibility of False
            return True
        # If the movie exist in the file
        else:
            # We display a message warning
            logging.warning(f"Le film {self.title} est déjà dans la liste")
            # return False because before return True
            return False

    # This method for delete movie in the file
    def remove_to_movie(self):
        # We get the all movies in the file
        movies = self._get_movies()
        # Condition if the movie exist in the file
        if self.title in movies:
            # Here, we delete the movie with method remove of the class list
            movies.remove(self.title)
            # After, we writing the new list movie in the file
            self._write_movies(movies)
            # return True because there is a possibility of False
            return True
        # If the movie not exist in the file
        else:
            # We display a message warning
            logging.warning(f"Le film {self.title} ne se trouve pas dans votre liste")
            # return False because before return True
            return False

# Condition who start when run the file movie.py
if __name__ == "__main__":
    m = Movie("le seigneur des anneaux")
    movies = get_movies()
