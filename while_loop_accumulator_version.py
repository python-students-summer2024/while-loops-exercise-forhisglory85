def get_starting_number():
    while True:
        how_many_beers = input("How many bottles of beer on the wall? ")
        if how_many_beers.isnumeric() and int(how_many_beers) >= 1:
            return int(how_many_beers)
        else:
            print("Please enter a valid number (1 or greater).")

def sing(starting_bottles):
    i = starting_bottles
    while i > 0:
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i - 1 == 1:
                print(f"Take one down, pass it around, {i - 1} bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.\n")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        i -= 1