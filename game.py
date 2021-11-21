#pygame Basics

import pygame
pygame.init()



#window width,Height in pixels
window=pygame.display.set_mode((500,500))

pygame.display.set_caption("exercise by LemOnHerO")


x=50 #x-coordiante
y=420 #y-coordinate
width=40
height=60
vel=5

is_jump=False
jump_count=10



run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

#keypress
	keys=pygame.key.get_pressed()

	if keys[pygame.K_a] and x > vel:
		x -= vel

	if keys[pygame.K_d] and x < 500 - width - vel:
		x += vel

	if not (is_jump):
		if keys[pygame.K_w] and y > vel :
			y -= vel

		if keys[pygame.K_s] and y < 500 - height - vel:
			y += vel
	
	
		#jumping
		if keys[pygame.K_SPACE]:
			is_jump = True
	else:
		if jump_count >= -10:
			neg=1
			if jump_count < 0:
				neg = -1 
			y-=(jump_count**2)*0.5* neg
			jump_count-=1

		else:
			is_jump = False
			jump_count = 10




	#to prvent red duplicates making in the screen '#' it to see red line
	window.fill((0,0,0))
	#draw shape		
	pygame.draw.rect(window,(255,0,0),(x,y,width,height))
	pygame.display.update()	



pygame.quit()



