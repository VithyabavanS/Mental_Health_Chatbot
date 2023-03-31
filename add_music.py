import random
import os

import pygame #import pygame library

pygame.mixer.init() #initialize the mixture module with default value

def play_song(songs): #method for load and play music file

    song=random.choice(songs)
    pygame.mixer.music.load(song) #load the music file
    pygame.mixer.music.play() #playing loaded file

    while pygame.mixer.music.get_busy():#loop for wait for the until music playing finish
        continue

def get_response(intents_list,intents_json):
    tag=intents_list[0]['intent']
    list_of_intents=intents_json['intents']
    result="sorry,can't understand you,please give me more info"
    for i in list_of_intents:
        if i['tag']==tag:
            result=random.choice(i['responses'])
            user_input([tag])
            break
    return result

def user_input(user_message):#method to get user's input messages list and playing music according to message
    current_dir=os.path.dirname(__file__) #extract the current path and assigned to the current_dir
    for message in user_message:
        if message=="anxiety":
            songs=[os.path.join(current_dir,"mp3_songs","anxiety","easy-lifestyle.mp3"),
                   os.path.join(current_dir,"mp3_songs","anxiety","relaxed-vlog-night-street.mp3"),
                   os.path.join(current_dir,"mp3_songs","anxiety","river-tram.mp3"),
                   os.path.join(current_dir,"mp3_songs","anxiety","sleep.mp3"),
                   os.path.join(current_dir,"mp3_songs","anxiety","game-of-thrones.mp3"),
                   os.path.join(current_dir, "mp3_songs", "anxiety", "Enya_-_Only_Time.mp3"),
                   os.path.join(current_dir, "mp3_songs", "anxiety", "scott-buckley-jul.mp3"),
                   os.path.join(current_dir, "mp3_songs", "anxiety", "The_Black_Eyed_Peas_-_I_Gotta_Feeling.mp3"),
                   os.path.join(current_dir, "mp3_songs", "anxiety", "Colbie_Caillat_-_Bubbly.mp3"),

                   ]
            play_song(songs)
        elif message=="depression":
            songs=[os.path.join(current_dir,"mp3_songs","depression","good-memories.mp3"),
                   os.path.join(current_dir,"mp3_songs","depression","soft-calm-sad-solo-piano.mp3"),
                   os.path.join(current_dir,"mp3_songs","depression","the-sad-minimal-piano-background.mp3"),
                   os.path.join(current_dir,"mp3_songs","depression","dark.mp3"),
                   os.path.join(current_dir, "mp3_songs", "depression", "Imagine_Dragons_-_On_top_of_the_world.mp3"),
                   os.path.join(current_dir, "mp3_songs", "depression", "Sia_-_Moon.mp3"),
                   os.path.join(current_dir, "mp3_songs", "depression", "Love Me Like You Do.mp3"),
                   os.path.join(current_dir, "mp3_songs", "depression", "Sia_-_Breathe_Me.mp3")
                   ]
            play_song(songs)
        elif message=="happy":
            songs=[os.path.join(current_dir,"mp3_songs","funny","Better-call-saul.mp3"),
                   os.path.join(current_dir,"mp3_songs","funny","Rockabye---Clean-Bandit.mp3"),
                   os.path.join(current_dir,"mp3_songs","funny","Fluffing-a-Duck.mp3"),
                   os.path.join(current_dir,"mp3_songs","funny","alex-productions.mp3"),
                   os.path.join(current_dir,"mp3_songs","funny","Jason_Mraz_-_I_m_Yours.mp3"),
                   os.path.join(current_dir, "mp3_songs", "funny", "Miley_Cyrus_-_The_Climb.mp3"),
                   os.path.join(current_dir, "mp3_songs", "funny", "Lady_Gaga_feat._Colby_O_Donis_-_Just_Dance.mp3"),
                   os.path.join(current_dir, "mp3_songs", "funny", "i'm blue.mp3")

                   ]
            play_song(songs)
user_input(["happy","depression","anxiety"])#call the user input method