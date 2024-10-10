import json
from datetime import datetime


def update_movie_status(func):
    """Décorateur pour mettre à jour le statut d'emprunt d'un film."""
    def wrapper(_, videoclub, movie_title):
        if movie_title in videoclub.stock:
            print(f"--- Mise à jour du statut de '{movie_title}' ---")
        return func(_, videoclub, movie_title)
    return wrapper


class VideoClub:
    def __init__(self, name, open_days):
        self.name = name
        self.open_days = open_days
        self.status = "ouvert"
        self.current_day = 0
        self.movies = self.load_movies_from_json()
        self.stock = {movie['title']: 1 for movie in self.movies}  # Stock de 1 film par défaut

    @staticmethod
    def load_movies_from_json(file_path='data/movies.json'):
        with open(file_path, 'r') as file:
            return json.load(file)

    def update_status(self):
        """Met à jour le statut du VideoClub en fonction du nombre de jours restants."""
        self.current_day += 1
        if self.current_day >= self.open_days:
            self.status = "fermé"
            print(f"\nLe Vidéo Club '{self.name}' est maintenant fermé.\n")

    def display_status(self):
        print(f"\nJour {self.current_day}/{self.open_days} - Statut: {self.status}")

    def display_available_movies(self):
        print(f"\n{"-"*3} Films disponibles chez {self.name} {"-"*3}")
        for movie, stock in self.stock.items():
            if stock > 0:
                print(f"{movie}: Stock = {stock}")
