
# Data format
# Stardew_Valley Farming RPG Sandbox DatingSim
# Slime_Rancher Farming Adventure Sandbox
# Hollow_Knight Metroidvania Platformer Adventure
# Enter_The_Gungeon Roguelike Shooter Action
# Cult_Of_The_Lamb Roguelike Action Farming


# Main Program
import time

ratings = {}
def search_game(game_name):
    matches = []
    with open("data.txt", "r") as f:
        games = f.readlines()
        for game in games:
            if game_name.lower() in game.lower():
                matches.append(game.strip())
    return matches

def rate(game_name):
    while True:
        try:
            rating = float(input(f"Please enter your rating for {game_name} (0-5): \n"))
            if 0 <= rating <= 5:
                if game_name in ratings:
                    ratings[game_name].append(rating)
                else:
                    ratings[game_name] = [rating]
                print(f"Thank you! Your rating of {rating} for {game_name} has been recorded.\n")
                break
            else:
                print("Please enter a rating between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5.")


def display_ratings():
    if ratings:
        print("\nGame Ratings:")
        for i, (game, rating_list) in enumerate(ratings.items(), start=1):
            for rating in rating_list:
                print(f"{i}. {game} - Rating: {rating}")
    else:
        print("No ratings available.")
    print("\n")


def main():
    while (1):
        in1 = input("1. Search for a game\n2. Games Rated\n3. Exit Program\n")
        # test = int(test)
        if (in1 == "0"):
            print("Wow there bud, you're already as far back as you can be! (PS you can use 3 to quit the program)")
        elif (in1 == "1"):
            in2 = input("Please input a name of a game (or 0 to go back):\n")
            if (in2 == "0"):
                continue
            else:
                results = search_game(in2)
                i = 1
                for r in results:
                    print(f"{i}. {r}")
                    i += 1
                # test = int (input("if you would like to rate a game select its number (Otherwise select 0 to go back):\n"))
                while True:
                    try:
                        in3 =  input("if you would like to rate a game select its number (Otherwise select 0 to go back):\n")
                        if in3 == "0":
                                break
                        index = int(in3) - 1
                        if 0 <= index < len(results):
                            rate(results[index])
                            break
                        else:
                            print("Invalid selection.")
                            break
                    except ValueError:
                        print("Please enter a valid number.")
        elif (in1 == "2"):
            display_ratings()



        
        elif (in1 == "3"):
            quit()
        else:
            print("Please Enter Valid Input")


if __name__ == "__main__":
    main()