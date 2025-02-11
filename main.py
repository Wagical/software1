
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
            time.sleep(1)
            if 0 <= rating <= 5:
                if game_name in ratings:
                    overwrite = input(f"Do you want to overwrite your previous rating for {game_name}? (Y or N): \n")
                    time.sleep(.7)
                    if overwrite.lower() == "y":
                        ratings[game_name] = [rating]
                        print(f"Your rating for {game_name} has been updated to {rating}.\n")
                    else:
                        print("Your previous rating remains unchanged.\n")
                else:
                    ratings[game_name] = [rating]
                    print(f"Thank you! Your rating of {rating} for {game_name} has been recorded.\n")
                break
            else:
                print("Please enter a rating between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5.")

def browse_games():
    with open("data.txt", "r") as f:
        games = f.readlines()
    total_games = len(games)
    index = 0
    while index < total_games:
        try:
            num_to_print = int(input(f"How many games would you like to see at a time? (1-{total_games - index}): "))
            if 1 <= num_to_print <= total_games - index:
                for i in range(index, index + num_to_print):
                    print(f"{i + 1}. {games[i].strip()}")
                index += num_to_print
                if index < total_games:
                    cont = input("Would you like to see more games? (Y/N): ")
                    if cont.lower() != 'y':
                        break
            else:
                print(f"Please enter a number between 1 and {total_games - index}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


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
        in1 = input("If its you'r first time try 1 and rate a game!\n1. Search for a game\n2. Games Rated\n3. Exit Program\n")
        time.sleep(.7)
        # test = int(test)
        if (in1 == "0"):
            print("Wow there bud, you're already as far back as you can be! (PS you can use 3 to quit the program)")
        elif (in1 == "1"):
            in2 = input("Don't know what game? try Mario!\nPlease input a name of a game to rate (which will be saved to your games rated!)\n OR type ALL to just browse(or 0 to go back):\n")
            time.sleep(.7)
            if (in2 == "0"):
                continue
            elif(in2 == "ALL"):
                browse_games()
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
                        time.sleep(.7)
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
