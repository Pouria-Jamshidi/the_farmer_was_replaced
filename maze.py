from movements import current_pos
#create a maze if desired value
def spawnMaze(size = 1):
	"""
	creates a maze
	
	:param size: percentage of full size (between 0.01 and 1)
	"""
	if size > 1:
		size = 1
	elif size < 0:
		size = 0.01

	full_size = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	maze_size = size * full_size
	harvest()
	till()
	plant(Entities.bush)
	use_item(Items.Weird_Substance, maze_size)

def entity_check():
	return get_entity_type()

# def already_explored(facing): # Needs fixing later
# 	pass

# def mazeMovement(): # Does not work yet.
# 	directions = [North,East,South,West]
# 	facing = 0

# 	go_forward = facing
# 	go_backward = (facing + 2) % 4
# 	turn_right = (facing + 1) % 4
# 	turn_left = (facing - 1) % 4
	
# 	explored = []

# 	explored.append(current_pos())

# 	while entity_check() != Entities.Treasure:

# 		if can_move(directions[turn_right]): # If we can turn right, turn right
# 			move(directions[turn_right])
# 			facing = turn_right
# 			if current_pos() in explored:
# 				while current_pos() in explored:
# 					move(directions[go_backward]) # Stepping back if the pose was explored
# 				facing = go_backward
# 			else : 
# 				explored.append(current_pos())
				
		
# 		elif can_move(directions[go_forward]): # If we can move forward, move forward
# 			move(directions[go_forward])
# 			if current_pos() in explored:
# 				while current_pos() in explored:
# 					move(directions[go_backward]) # Stepping back if the pose was explored
# 				facing = go_backward
# 			else : 
# 				explored.append(current_pos())

# 		elif can_move(directions[turn_left]): # If we can move left, move left
# 			move(directions[turn_left])
# 			facing = turn_left
# 			if current_pos() in explored:
# 				while current_pos() in explored:
# 					move(directions[go_backward]) # Stepping back if the pose was explored
# 				facing = go_backward
# 			else : 
# 				explored.append(current_pos())


# 		else: # Only way to move is backward
# 			move(directions[go_backward]) # Move backward
# 			facing = go_backward
# 			if current_pos() in explored:
# 				while current_pos() in explored:
# 					move(directions[go_backward]) # Stepping back if the pose was explored
# 				facing = go_backward
# 			else : 
# 				explored.append(current_pos())
				
# 	harvest()

def mazeMovement_no_explored():
	
	directions = [North,East,South,West]
	facing = 0

	while entity_check() != Entities.Treasure:

		if can_move(directions[(facing + 1) % 4]): # If we can turn right, turn right
			move(directions[(facing + 1) % 4])
			facing = (facing + 1) % 4
		
		elif can_move(directions[facing]): # If we can move forward, move forward
			move(directions[facing])

		elif can_move(directions[(facing - 1) % 4]): # If we can move left, move left
			move(directions[(facing - 1) % 4])
			facing = (facing - 1) % 4

		else: # Only way to move is backward
			move(directions[(facing + 2) % 4]) # Move backward
			facing = (facing + 2) % 4
				
	harvest()

if __name__ == '__main__':
	
	while True:
		spawnMaze()
		mazeMovement_no_explored()