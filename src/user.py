from src.videoclub import update_movie_status


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_movies = []

    @update_movie_status
    def borrow_movie(self, videoclub, movie_title):
        """Emprunte un film si disponible dans le stock du VideoClub."""
        if videoclub.status == "ouvert":
            if videoclub.stock.get(movie_title, 0) > 0:
                videoclub.stock[movie_title] -= 1
                self.borrowed_movies.append(movie_title)
                print(f"{self.name} a emprunté le film '{movie_title}'.")
            else:
                print(f"Le film '{movie_title}' n'est pas disponible.")
        else:
            print(f"Le VideoClub est fermé. {self.name} ne peut pas emprunter de films.")

    @update_movie_status
    def return_movie(self, videoclub, movie_title):
        """Retourne un film emprunté au VideoClub."""
        if movie_title in self.borrowed_movies:
            videoclub.stock[movie_title] += 1
            self.borrowed_movies.remove(movie_title)
            print(f"{self.name} a retourné le film '{movie_title}'.")
        else:
            print(f"Le film '{movie_title}' n'a pas été emprunté par {self.name}.")
