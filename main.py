import cv2
from screen import cap_screen
from player import Player

def check_player_pos(p):
	pross_screen = cap_screen()
	if pross_screen[p.x][p.y] == 255:
		print("go up")
	cv2.imshow('window', pross_screen)

p = Player(0, 177, 89)
while(True):
	check_player_pos(p)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break