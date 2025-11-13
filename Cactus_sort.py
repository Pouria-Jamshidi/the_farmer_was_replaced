from movements import goTo

limit = get_world_size()


# fills the map with cactus
def fullCactus():
    for i in range(limit):
        for j in range(limit):
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Cactus)
            move(North)
        move(East)


# gives a matrix of current cactus status
def cactusMatrix():
    goTo()
    cactusList = []
    for i in range(limit):
        tempList = []
        for j in range(limit):
            tempList.append(measure())
            move(East)
        cactusList.append(tempList)
        move(North)
    return cactusList


# sorts the cactus in farm using bobble sort algorithm
def sortCactus_bobble_singleDrone():
    # sorting the rows
    goTo()

    for i in range(limit):
        again = True
        while again:
            again = False
            for j in range(limit - 1):
                if measure() > measure(East):
                    swap(East)
                    again = True
                if j + 1 == limit - 1:
                    move(East)
                    move(East)
                else:
                    move(East)
        move(North)
    # sorting the columns
    goTo()

    for j in range(limit):
        again = True
        while again:
            again = False
            for i in range(limit - 1):
                if measure() > measure(North):
                    swap(North)
                    again = True
                if i + 1 == limit - 1:
                    move(North)
                    move(North)
                else:
                    move(North)
        move(East)


# sorts the cactus in farm using cocktail shake sort algorithm (still under maintenance)
def sortCactus_cocktail_singleDrone():
    # moving to the (0,0) coordinates
    goTo()
    # sorting the rows
    for i in range(limit):
        again = True
        moveDirection = "left-to-right"
        while again:
            again = False
            # sorting the smaller value when moving left to right
            if moveDirection == "left-to-right":
                #limit minus 2 because world size starts from 1 instead of 0 like in range
                #if we do minus 1 we reach edge of map and we cant measure East as it is out of bound and it ruins the code                
                for j in range(limit - 2):
                    if measure() > measure(East):
                        swap(East)
                        again = True
                    move(East)
                moveDirection = "right-to-left"
            move(East)
            # breaking out of while loop so we dont have to waste time moving back and check if there was no swap
            if again==False:
                move(East)
                break
            #making the again=False so if it is sorted already and no swaps when moving back we dont start while loop again
            again=False
            # sorting bigger valuse when moving right to left
            if moveDirection == "right-to-left":
                for j in range(limit - 2):
                    if measure() < measure(West):
                        swap(West)
                        again = True
                    move(West)
                moveDirection = "left-to-right"
            move(West)
        move(North)
    # sorting the columns
    goTo()

    for j in range(limit):
        again = True
        moveDirection = "down-to-up"
        while again:
            again = False
            #sorting lower value when moving down to up
            if moveDirection == "down-to-up":
                for i in range(limit - 2):
                    if measure() > measure(North):
                        swap(North)
                        again = True
                    move(North)
                moveDirection = "up-to-down"
            move(North)
            # breaking out of while loop so we dont have to waste time moving back and check if there was no swap
            if again==False:
                move(North)
                break
            #making the again=False so if it is sorted already and no swaps when moving back we dont start while loop again
            again=False
			#sorting bigger value when moving up to down
            if moveDirection == "up-to-down":
                for i in range(limit - 2):
                    if measure() < measure(South):
                        swap(South)
                        again = True
                    move(South)
                moveDirection = "down-to-up"
            move(South)
        move(East)


# runs if you run this python file
if __name__ == "__main__":
    while True:
        fullCactus()
        # sortCactus_bobble_singleDrone()
        sortCactus_cocktail_singleDrone()
        # quick_print(cactusMatrix())
        harvest()
