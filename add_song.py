import random
import os
import pygame.mixer

pygame.mixer.init()

def play_song_by_category(category):
    current_dir = os.path.dirname(__file__)

    #if category == "Play song for anxiety":
    if "anxiety" in category.lower():
        songs = [
            os.path.join(current_dir, "mp3_songs", "anxiety", "easy-lifestyle.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "relaxed-vlog-night-street.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "river-tram.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "sleep.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "game-of-thrones.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "Enya_-_Only_Time.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "scott-buckley-jul.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "The_Black_Eyed_Peas_-_I_Gotta_Feeling.mp3"),
            os.path.join(current_dir, "mp3_songs", "anxiety", "Colbie_Caillat_-_Bubbly.mp3"),
            # Add more anxiety songs here
        ]
    #elif category == "play song for depression":
    elif "depression" in category.lower():
        songs = [
            os.path.join(current_dir, "mp3_songs", "depression", "good-memories.mp3"),
            os.path.join(current_dir, "mp3_songs", "depression", "soft-calm-sad-solo-piano.mp3"),
            os.path.join(current_dir, "mp3_songs", "depression", "the-sad-minimal-piano-background.mp3"),
            os.path.join(current_dir, "mp3_songs", "depression", "dark.mp3"),
            os.path.join(current_dir, "mp3_songs", "depression", "Imagine_Dragons_-_On_top_of_the_world.mp3"),
            os.path.join(current_dir, "mp3_songs", "depression", "Sia_-_Moon.mp3"),
            os.path.join(current_dir, "mp3_songs", "depression", "Love Me Like You Do.mp3"),
            os.path.join(current_dir, "mp3_songs", "depression", "Sia_-_Breathe_Me.mp3")
            # Add more depression songs here
        ]
    #elif category == "play funny song":
    elif "funny" in category.lower():
        songs = [
            os.path.join(current_dir, "mp3_songs", "funny", "i'm blue.mp3"),
            os.path.join(current_dir, "mp3_songs", "funny", "Rockabye---Clean-Bandit.mp3"),
            os.path.join(current_dir, "mp3_songs", "funny", "Fluffing-a-Duck.mp3"),
            os.path.join(current_dir, "mp3_songs", "funny", "alex-productions.mp3"),
            os.path.join(current_dir, "mp3_songs", "funny", "Jason_Mraz_-_I_m_Yours.mp3"),
            os.path.join(current_dir, "mp3_songs", "funny", "Miley_Cyrus_-_The_Climb.mp3"),
            os.path.join(current_dir, "mp3_songs", "funny", "Lady_Gaga_feat._Colby_O_Donis_-_Just_Dance.mp3"),
            os.path.join(current_dir, "mp3_songs", "funny", "i'm blue.mp3")
            # Add more happy songs here
        ]
    else:
        songs = []

    if songs:
        song = random.choice(songs)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue
    else:
        print("No songs available for the selected category.")

# Additional helper function for playing a specific song by path
def play_specific_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue