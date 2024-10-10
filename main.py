from src.videoclub import VideoClub
from src.user import User
import time

if __name__ == "__main__":
    # Instanciation du Vidéo Club avec une période d'ouverture de 5 jours
    videoclub = VideoClub(name="Video Club Retro", open_days=5)

    # Création d'un utilisateur
    user1 = User("Alice")

    # Boucle pour simuler les jours d'ouverture
    while videoclub.status == "ouvert":
        # Affichage du statut et des films disponibles
        videoclub.display_status()
        videoclub.display_available_movies()

        # Simule une journée d'activité
        user1.borrow_movie(videoclub, "Inception")
        user1.return_movie(videoclub, "Inception")

        # Avancer d'un jour
        videoclub.update_status()
        
        # Pause pour simuler le passage des jours
        time.sleep(1)
    
    print(f"Simulation terminée. '{videoclub.name}' est fermé.")
