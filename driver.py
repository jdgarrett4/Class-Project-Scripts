from mines import Mines

def main():
    
    print("Field Test One\n")
    minefield = Mines()
    print(minefield)
    minefield.set_mines(6)
    minefield.place_mines()
    print(minefield)

    print("\nField Test Two\n")
    minefield = Mines('#', 8, 9)
    print(minefield)
    minefield.set_mines(8)
    minefield.place_mines()
    print(minefield)

main()