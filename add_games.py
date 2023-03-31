import os
import webbrowser as wb
import random


def user_input(user_message): #methos to get user's input
    for message in user_message:
        if message=="anxiety":
           games=["https://www.primarygames.com/langarts/hangaroo/",
                  "https://www.primarygames.com/holidays/thanksgiving/games/turkeytens/",
                  "https://www.primarygames.com/arcade/simulation/farmfactory/",
                  "https://www.primarygames.com/holidays/valentines/games/savethelove/"]
           wb.open_new(random.choice(games))
        elif message=="depression":
           games=["https://www.primarygames.com/arcade/cooking/pizzaparty/",
                  "https://www.primarygames.com/arcade/cooking/hazelandmomsrecipes/hazelandmomsrecipescpumpkinmuffins/",
                  "https://www.primarygames.com/arcade/adventure/snowballchristmasworld/",
                  "https://www.primarygames.com/arcade/cooking/cupcakefrenzy/"]
           wb.open_new(random.choice(games))
        elif message=="funny":
            games=["https://www.primarygames.com/puzzles/physics/cutforcat2/",
                   "https://www.primarygames.com/puzzles/action/ninjapainter/",
                   "https://www.primarygames.com/arcade/classic/germageddon/",
                   "https://www.primarygames.com/arcade/simulation/customcarshop/"]

            wb.open_new(random.choice(games))

user_input(["funny"])