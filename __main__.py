from gameManager import GameManager

if __name__ == "__main__":
    game = GameManager()
    while not game.over():
        game.loop()
    game.quit()