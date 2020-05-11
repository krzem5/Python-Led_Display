#!/usr/bin/python
# -*- coding: utf-8 -*-
from display import color,Display
from PIL import Image,ImageDraw
import math
import random
import time



def hue(v):
	if (v<85):
		return (v*3,255-v*3,0)
	elif (v<170):
		v-=85
		return (255-v*3,0,v*3)
	v-=170
	return (0,v*3,255-v*3)



def main(d):
	img=Image.new("RGB",(32,8),(0,0,0))
	draw=ImageDraw.Draw(img)
	BALL_COLOR=(10,181,239)#(233,82,35)#(110,220,123)#(226,106,182)
	BALL_POS=[15.5,3.5]
	a=random.random()*math.pi*2
	BALL_VEL=[math.cos(a),math.sin(a)]
	BALLS_SIZE=4
	for _ in range(30*10):
		draw.rectangle((0,0,31,7),fill=(0,0,0))
		draw.ellipse((BALL_POS[0]-BALLS_SIZE/2,BALL_POS[1]-BALLS_SIZE/2,BALL_POS[0]+BALLS_SIZE/2,BALL_POS[1]+BALLS_SIZE/2),fill=BALL_COLOR)
		BALL_POS[0]+=BALL_VEL[0]
		BALL_POS[1]+=BALL_VEL[1]
		if (BALL_POS[0]-BALLS_SIZE/2<0):
			BALL_POS[0]=BALLS_SIZE/2-BALL_VEL[0]
			BALL_VEL[0]*=-1
		elif (BALL_POS[0]+BALLS_SIZE/2>31):
			BALL_POS[0]=31-BALLS_SIZE/2
			BALL_VEL[0]*=-1
		if (BALL_POS[1]-BALLS_SIZE/2<0):
			BALL_POS[1]=BALLS_SIZE/2-BALL_VEL[1]
			BALL_VEL[1]*=-1
		elif (BALL_POS[1]+BALLS_SIZE/2>7):
			BALL_POS[1]=7-BALLS_SIZE/2
			BALL_VEL[1]*=-1
		d.data.image(img)
		d.update()
		time.sleep(1/30)
	##########################################
	# for _ in range(1000):
	# 	for j in range(0,256):
	# 		d.data[j]=hue(random.randint(0,255))
	# 	d.brightness(random.randint(1,255))
	# 	d.update()
	# 	time.sleep(0.01)
	##########################################
	# for i in range(1000):
	# 	for j in range(0,256):
	# 		d.data[j]=hue((j+i)%255)
	# 	d.update()
	# 	time.sleep(0.01)
Display(brightness=16).run(main)