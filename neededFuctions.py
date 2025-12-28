
#full harvest before reset(1=Grassland,2=Soil,Empty=No change)
def fullHarvest(groundChange=0):
	# """
	# full harvest before reset

	# :param int groundChange: decides the state of ground after harvest.
	# 0 or empty for no change
	# 1 for grassland
	# 2 for soil
	# """
	groundList=['',Grounds.Grassland,Grounds.Soil]
	neededGround=groundList[groundChange]
	if groundChange>=0 and groundChange<=2:
		for i in range (get_world_size()):
			for j in range (get_world_size()):
				harvest()
				if groundChange:
					if get_ground_type()!=neededGround:
						till()
				move(North)
			move(East)
	else:
		print('value should be between 0 to 2')

#function needed for watering
def watering(amount=0.5):
	# """
	# a function needed for watering, the defult value is 0.5 water level
	
	# :param amount: wetness of soil
	# """

	if get_water()<=amount:
		use_item(Items.Water)
		
#getting the ground ready after expansion
def ggr():
	# """
	# getting the ground ready after expansion or loading the save
	# """
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_pos_x()<=5 and get_pos_y()<=5:
				till()
			elif (get_pos_x()+get_pos_y()+1)%2!=0:
				till()
			move(East)
		move(South)
		
#Replanting after getting ground ready
def replanting():
	# """
	# replanting the default layout after calling ggr() method
	# """
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type()==Grounds.Soil:
				if get_pos_x()<=5 and get_pos_y()<=5:
					plant(Entities.Pumpkin)
				
				elif get_pos_y()==0:
					plant(Entities.Sunflower)
				else:
					plant(Entities.Carrot)
					
			elif get_ground_type()==Grounds.Grassland:
				if get_pos_x()>0 and get_pos_y()>0 and get_pos_x()!=get_world_size()-1 and get_pos_y()!=get_world_size()-1:
					plant(Entities.Tree)
			move(East)
		move(South)

#Auto harvest for pumpkin,tree,grass,carrot (default=False, first input for water level and second 0/1 for fertilizer)
def startHarvesting(toWater=0,toFertilize=0):
	# '''
	# Auto harvest for pumpkin,tree,grass,carrot 

	# :param toWater: indicated the level of moisture in land.
	# :param toFertilize: indicated whether or not to add fertilizer using 0 or 1.
	# '''
	#decided whether or not to water/fertilize
	def additional_actions():
		if toWater:
			watering(toWater)
		if toFertilize:
			use_item(Items.Fertilizer)
		
	while True:
			for i in range(get_world_size()):
				if get_ground_type()==Grounds.Grassland:
					if get_entity_type()==Entities.Grass:
						if can_harvest():
							harvest()
					elif get_entity_type()==Entities.Tree:
						if can_harvest():
							harvest()
							plant(Entities.Tree)
							additional_actions()
				if get_ground_type()==Grounds.Soil:
					if get_entity_type()==Entities.Dead_Pumpkin or get_entity_type()==None:
						plant(Entities.Pumpkin)
					elif get_entity_type()==Entities.Pumpkin:
						if can_harvest():
							harvest()
							plant(Entities.Pumpkin)
							additional_actions()
					elif get_entity_type()==Entities.Carrot:
						if can_harvest():
							harvest()
							plant(Entities.Carrot)
							additional_actions()
					elif get_entity_type()==Entities.Sunflower:
						if can_harvest():
							harvest()
							plant(Entities.Sunflower)
							additional_actions()
				move(North)
			move(East)