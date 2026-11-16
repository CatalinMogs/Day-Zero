location = "house"
health = 100
food = 2
water = 2
game_running = True

while game_running:
    print("==============================")
    print("          DAY ZERO")
    print("     THE APOCALYPSE BEGINS")
    print("==============================")

    if food <= 0 or water <= 0:
        print("You're starving or dehydrated!")
        health -= 10

    if location == "house":
        print("\nHealth:", health)
        print("Food:", food)
        print("Water:", water)

        print("\nThe world has fallen apart...")
        print("You are inside your house.")
        print("You need to find supplies and survive.")
        print("What do you want to do?")
        print("1. Search the house for supplies")
        print("2. Go to the supermarket")
        print("3. Turn on the radio")
        print("4. Travel to the evacuation point")

        answer = input("Choose 1-4: ")

        if answer == "1":
            print("You search the house and find some food.")
            food += 1
        elif answer == "2":
            location = "supermarket"
        elif answer == "3":
            print("The radio crackles.")
            print("'Survivors are gathering at the military evacuation point.'")
            print("'Bring at least 3 food and 2 water supplies.'")
        elif answer == "4":
            if food >= 3 and water >= 2:
                location = "ending"
            else:
                print("You don't have enough supplies!")
        else: 
            print("Invalid choice!")

    elif location == "supermarket":
        print("\nHealth:", health)
        print("Food:", food)
        print("Water:", water)

        print("\nYou arrive at the supermarket.")
        print("The shelves are mostly empty.")
        print("You hear strange noises coming from the storage room.")
        print("What do you want to do?")
        print("1. Search the shelves")
        print("2. Investigate the storage room")
        print("3. Return home")
        print("4. Travel to the gas station")

        answer = input("Choose 1-4: ")

        if answer == "1":
            print("You find some bottled water!")
            water += 1
        elif answer == "2":
            print("A zombie suddenly appears!")
            print("You run away, but it scratches your arm.")
            health -= 25
        elif answer == "3":
            location = "house"
        elif answer == "4":
            location = "gas_station"
        else:
            print("Invalid choice!")

    elif location == "gas_station":
        print("\nHealth:", health)
        print("Food:", food)
        print("Water:", water)

        print("\nYou arrive at an abandoned gas station.")
        print("There is an old car parked outside.")
        print("What do you want to do?")
        print("1. Search the building")
        print("2. Inspect the car")
        print("3. Return to the supermarket")

        answer = input("Choose 1-3: ")

        if answer == "1":
            print("You find some canned food!")
            food += 1
        elif answer == "2":
            print("You find some fuel, but something is moving behind the car...")
            health -= 10
        elif answer == "3":
            location = "supermarket"
        else:
            print("Invalid choice!")

    elif location == "ending":
        print("\nYou arrive at the evacuation point.")
        print("Soldiers welcome you aboard a rescue helicopter.")
        print("You survived DAY ZERO!")
        print("GOOD ENDING")
        game_running = False

    if health <= 0:
        print("\nYou didn't survive the outbreak...")
        print("GAME OVER")
        game_running = False
        break