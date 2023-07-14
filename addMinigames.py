import random
import webbrowser

def play_game():
    games = [
        "https://www.primarygames.com/langarts/hangaroo/",
        "https://www.primarygames.com/holidays/thanksgiving/games/turkeytens/",
        "https://www.primarygames.com/arcade/simulation/farmfactory/",
        "https://www.primarygames.com/arcade/simulation/farmfactory/"
    ]
    game_url = random.choice(games)
    webbrowser.open(game_url)