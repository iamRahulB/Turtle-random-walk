import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



def random_walk(ran_angle,ran_color,ran_move):
	tim.forward(ran_move)
	tim.right(ran_angle)
	tim.color(ran_color)


for _ in range(0,200):
	ran_angle=random.randint(0,90)
	ran_move=random.randint(0,20)
	ran_color=random.choice(colours)
	random_walk(ran_angle,ran_color,ran_move)

	