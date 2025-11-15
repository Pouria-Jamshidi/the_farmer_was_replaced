
#full harvest before reset
def fullHarvest():
	for i in range (get_world_size()):
		for j in range (get_world_size()):
			harvest()
			if get_ground_type()==Grounds.Soil:
				till()
			move(North)
		move(East)
			

#function needed for watering
def watering(amount=0.5):
	if get_water()<=amount:
		use_item(Items.Water)
		
#getting the ground ready after expansion
def ggr():
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
#Auto harvest for pumpkin,tree,grass,carrot
def startHarvesting():
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
							watering()
				if get_ground_type()==Grounds.Soil:
					if get_entity_type()==Entities.Dead_Pumpkin or get_entity_type()==None:
						plant(Entities.Pumpkin)
					elif get_entity_type()==Entities.Pumpkin:
						if can_harvest():
							harvest()
							plant(Entities.Pumpkin)
							watering()
					elif get_entity_type()==Entities.Carrot:
						if can_harvest():
							harvest()
							plant(Entities.Carrot)
							watering()
					elif get_entity_type()==Entities.Sunflower:
						if can_harvest():
							harvest()
							plant(Entities.Sunflower)
							watering()
				move(North)
			move(East)