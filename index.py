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
	if (v<170):
		v-=85
		return (255-v*3,0,v*3)
	v-=170
	return (0,v*3,255-v*3)



def main(d):
	# img=Image.new("RGB",(32,8),(0,0,0))
	# draw=ImageDraw.Draw(img)
	# BALL_COLOR=[(40,60,180),(20,180,100),(255,128,0),(60,60,90),(255,255,255),(226,106,182),(10,181,239),(233,82,35),(110,220,123)][1]
	# BALL_POS=[15.5,3.5]
	# BALL_SPEED=10
	# a=random.random()*math.pi*2
	# BALL_VEL=[math.cos(a)*BALL_SPEED,math.sin(a)*BALL_SPEED]
	# BALLS_SIZE=4
	# lt=time.time()
	# for _ in range(30*10):
	# 	c=time.time()
	# 	dt=c-lt
	# 	lt=c
	# 	BALL_POS[0]+=BALL_VEL[0]*dt
	# 	BALL_POS[1]+=BALL_VEL[1]*dt
	# 	if (BALL_POS[0]-BALLS_SIZE/2<0):
	# 		BALL_POS[0]=BALLS_SIZE/2-BALL_VEL[0]*dt
	# 		BALL_VEL[0]*=-1
	# 	elif (BALL_POS[0]+BALLS_SIZE/2>31):
	# 		BALL_POS[0]=31-BALLS_SIZE/2
	# 		BALL_VEL[0]*=-1
	# 	if (BALL_POS[1]-BALLS_SIZE/2<0):
	# 		BALL_POS[1]=BALLS_SIZE/2-BALL_VEL[1]*dt
	# 		BALL_VEL[1]*=-1
	# 	elif (BALL_POS[1]+BALLS_SIZE/2>7):
	# 		BALL_POS[1]=7-BALLS_SIZE/2
	# 		BALL_VEL[1]*=-1
	# 	draw.rectangle((0,0,31,7),fill=(226,106,182))
	# 	draw.ellipse((BALL_POS[0]-BALLS_SIZE/2,BALL_POS[1]-BALLS_SIZE/2,BALL_POS[0]+BALLS_SIZE/2,BALL_POS[1]+BALLS_SIZE/2),fill=BALL_COLOR)
	# 	d.data.image(img)
	# 	d.update()
	# 	time.sleep(0.016)
	##########################################
	for _ in range(75):
		for j in range(0,256):
			d.data[j]=hue(random.randint(0,255))
		d.brightness(random.randint(1,255))
		d.update()
		time.sleep(0.01)
	##########################################
	# d.brightness(16)
	# for i in range(1000):
	# 	for j in range(0,256):
	# 		d.data[j]=hue((j+i)%256)
	# 	d.update()
	# 	time.sleep(0.01)
Display(brightness=16).run(main)
