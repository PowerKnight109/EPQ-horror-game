def main():
    from Horror_game import intro
    import time
    print(intro())
    from Horror_game import gameloop
    print(gameloop())
    from Horror_game import gamend
    time.sleep(1.5)
    gamend()
    pass

main()