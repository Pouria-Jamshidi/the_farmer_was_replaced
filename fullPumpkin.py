import movements
from neededFuctions import watering

limit = get_world_size()


# planting the pumpkins (the watered input is a float number for our moisture level)
def pumpkinFarm(watered=False, fertilizing=False):
	# move to the start
	movements.goTo()
	for i in range(limit):
		for j in range(limit):
			# tilling the ground if not tilled
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Pumpkin)
			# watering or fertilizing depending on our input (defult = no water and fertilizer)
			if watered:
				watering(watered)
			if fertilizing:
				use_item(Items.Fertilizer)
			move(East)
		move(North)


# start farming the land for pumpkin
def startFarmingPumpkin(watered=False, fertilizing=False):
	for i in range(limit):
		for j in range(limit):
			if get_entity_type() == Entities.Dead_Pumpkin:
				if fertilizing:
					#due to a bug or coding error, if fertilizer is used , it changes the state of pumpking.
					#dead ones stay dead , but if normal, it starts to grow healthy again.
					#this while loop ensures enough fertilizer used to recreate a healty pumpkin (current ver. 1.0 , workes till patched)
					while get_entity_type()==Entities.Dead_Pumpkin:
						use_item(Items.Fertilizer)
				else:
					plant(Entities.Pumpkin)
			harvest()
			plant(Entities.Pumpkin)
			# watering or fertilizing depending on our input (defult = no water and fertilizer)
			if watered:
				watering(watered)
			if fertilizing:
				use_item(Items.Fertilizer)
			move(East)
		move(North)


if __name__ == "__main__":
	pumpkinFarm(0,1)
	while True:
		startFarmingPumpkin(0,1)