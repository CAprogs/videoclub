import pytest
from src.videoclub import VideoClub
from src.user import User


def test_videoclub_status_update():
    videoclub = VideoClub("TestClub", 2)
    assert videoclub.status == "ouvert"
    videoclub.update_status()
    assert videoclub.status == "ouvert"
    videoclub.update_status()
    assert videoclub.status == "fermé"


def test_borrow_and_return_movie():
    videoclub = VideoClub("TestClub", 5)
    user = User("Bob")

    user.borrow_movie(videoclub, "Inception")
    assert "Inception" in user.borrowed_movies
    assert videoclub.stock["Inception"] == 0

    user.return_movie(videoclub, "Inception")
    assert "Inception" not in user.borrowed_movies
    assert videoclub.stock["Inception"] == 1
