limit = get_world_size()

#go to certain coordinates
def goTo(x=0,y=0):
	while get_pos_x()!=x and get_pos_y()!=y:
		if get_pos_x()>x:
			move(West)
		else:
			move(East)
	while get_pos_y()!=y:
		if get_pos_y()>y:
			move(South)
		else:
			move(North)
			
def current_pos():
	return {'x':get_pos_x(),'y':get_pos_y()}

#test or run codes here:
if __name__=='__main__':
	goTo()