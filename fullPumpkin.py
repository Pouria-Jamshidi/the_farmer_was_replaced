import movements
from neededFuctions import watering

def customSized_singleDrone_pumpkinFarm(world_size, watered = False, fertelized = False):
	# """
	# Create a custom size world for farming only pumpkin with a single drone\n
	
	# :param world_size: creates a n*n world. any number less than 3 means full world size
	# :param watered: should the drone water, and if yes gow dry the ground should be to water (between 0 and 1)
	# :param fertelized: should we add fertilizer or no (0/False = no , 1/True = yes)
	# """
	set_world_size(world_size)
	limit = get_world_size()
	for i in range(limit):

		for j in range(limit):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			if watered:
				watering(watered)
			if fertelized:
				use_item(Items.Fertilizer)
			move(East)

		all_ripe = False
		while not all_ripe:
			all_ripe = True
			for j in range(limit):
				if get_entity_type() == Entities.Dead_Pumpkin:
						all_ripe = False
						all_ripe = False
						plant(Entities.Pumpkin)
						if fertelized:
							use_item(Items.Fertilizer)
						if watered:
							watering(watered)

				move(East)
		move(North)
	harvest()

if __name__ == "__main__":
	# pumpkinFarm(0,1)
	# while True:
	# 	startFarmingPumpkin(0,1)

	while True:
		customSized_singleDrone_pumpkinFarm(6,1,1)