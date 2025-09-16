def main():
    difficulty = input("difficult or casual? ").strip().lower()
    if not (difficulty == "difficult" or difficulty == "casual"):
        print("enter a valid difficulty")
        return
    players = input("single-player or multiplayer? ").strip().lower()
    if not (players == "single-player" or players == "multiplayer"):
        print("enter a valid number of players")
        return
    if difficulty == "difficult" and players == "single-player":
        recommend("Dark Souls")
    elif difficulty == "difficult" and players == "multiplayer":
        recommend("Overwatch")
    elif difficulty == "casual" and players == "single-player":
        recommend("Stardew Valley")
    else:
        recommend("Mario Kart")

def recommend(game):
    print(f"We recommend you play {game}!")
    
main()