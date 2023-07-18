import random
import webbrowser


def open_game_by_category(category):
    if category == "action":
        action_games = [
            "https://www.primarygames.com/arcade/action/protectmission/",
            "https://www.primarygames.com/holidays/halloween/games/pixelzombies/",
            "https://www.primarygames.com/arcade/adventure/knightsdiamond/",
            "https://www.primarygames.com/arcade/action/falldudes/",
            # Add more action games here
        ]
        game_url = random.choice(action_games)
    elif category == "puzzle":
        puzzle_games = [
            "https://www.primarygames.com/langarts/hangaroo/",
            "https://www.primarygames.com/puzzles/action/fishlove/",
            "https://www.primarygames.com/puzzles/action/rubikscube/",
            "https://www.primarygames.com/holidays/halloween/games/dragdrop/",
            # Add more puzzle games here
        ]
        game_url = random.choice(puzzle_games)
    elif category == "adventure":
        adventure_games = [
            "https://www.primarygames.com/arcade/adventure/zed/",
            "https://www.primarygames.com/arcade/adventure/rockingwheels/",
            "https://www.primarygames.com/arcade/adventure/lostonthelostplanet/",
            "https://www.primarygames.com/arcade/action/runandescape/",
            # Add more adventure games here
        ]
        game_url = random.choice(adventure_games)
    elif category == "sport":
        sport_games = [
            "https://www.crazygames.com/game/8-ball-billiards-classic",
            "https://www.crazygames.com/game/soccer-legends-2021",
            "https://www.crazygames.com/game/basketball-skills",
            "https://www.crazygames.com/game/speedy-golf",

        ]
        game_url=random.choice(sport_games)
    elif category == "horror":
        horror_games = [
            "https://www.crazygames.com/game/haunted-school---horror-game",
            "https://www.crazygames.com/game/krampus",
            "https://www.crazygames.com/game/evil-neighbor-2",
            "https://www.crazygames.com/game/death-attraction-horror-game",

        ]
        game_url=random.choice(horror_games)
    elif category == "racing":
        racing_games = [
            "https://www.primarygames.com/arcade/racing/legocrosstowncraze/",
            "https://www.primarygames.com/arcade/sports/rockitracer/",
            "https://www.primarygames.com/arcade/sports/cyclesprint/",
            "https://www.primarygames.com/arcade/racing/carrush/",

        ]
        game_url=random.choice(racing_games)

    elif category == "cooking":
        cooking_games = [
            "https://www.primarygames.com/arcade/cooking/dreamydishespumpkinspicemuffins/",
            "https://www.primarygames.com/arcade/cooking/burgermaker/",
            "https://www.primarygames.com/arcade/cooking/pizzamakingextravaganza/",
            "https://www.primarygames.com/arcade/cooking/burgertime/",

        ]
        game_url = random.choice(cooking_games)

    elif category == "board":
        board_games = [
            "https://www.primarygames.com/puzzles/board/playcheckers/",
            "https://www.primarygames.com/puzzles/strategy/pegsolitaire/",
            "https://www.primarygames.com/puzzles/strategy/masterchess/",
            "https://www.primarygames.com/puzzles/strategy/dogeblocks/",

        ]
        game_url = random.choice(board_games)

    else:
        game_url = "https://www.primarygames.com"

    webbrowser.open(game_url)