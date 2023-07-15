import random

import pygame


def play_song():
    pygame.mixer.init()
    songs = [
        "C:\\Users\\Dell\\Desktop\\sdgp\\mp3_songs\\anxiety\\sleep.mp3",
        "C:\\Users\\Dell\\Desktop\\sdgp\\mp3_songs\\anxiety\\easy-lifestyle.mp3",
        "C:\\Users\\Dell\\Desktop\\sdgp\\mp3_songs\\anxiety\\game-of-thrones.mp3",
        # Add more song filenames here
    ]
    song = random.choice(songs)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    # Code to play the song goes here