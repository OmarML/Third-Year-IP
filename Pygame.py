import pygame
import random
import math as m
import csv
from ProcessData import My_Trajectory_Dict, Pedestrian_IDs
# Use a que / stack to load pedestrians in order as they come in and leave

background_colour = (255,255,255)
(width, height) = (1000, 1000)

# print(x_pos, y_pos)

# xarr = [200, 202, 204, 206, 208, 210, 208, 206, 204, 202]*100
# yarr = [200, 198, 196, 194, 192, 190, 192, 194, 196, 198]*100

counter = 0

class Particle:
	def __init__(self, x, y, size, R, G, B):
		self.x = x
		self.y = y
		self.size = size
		self.colour = (R, G, B)
		self.thickness = 0
		self.speed = 1
		self.angle = m.pi/2

	def display(self):
		pygame.draw.circle(screen, self.colour, ((int(self.x) + 500), (int(self.y) + 500)), self.size, self.thickness)

	def move(self, index, x_pos, y_pos):
		try:
			self.x = x_pos[index]
			self.y = y_pos[index]
			print(index, len(bigArr2[0][0]))
		except IndexError:
			counter = 0
			index = counter


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Omar's Simulation")
screen.fill(background_colour)

number_of_particles = 8
my_particles = []

bigArr2 = []
for pedestrian in Pedestrian_IDs[:10]:
	size = 10
	x1 = My_Trajectory_Dict[pedestrian][0][0]
	y1 = My_Trajectory_Dict[pedestrian][1][0]
	x = My_Trajectory_Dict[pedestrian][0]
	y = My_Trajectory_Dict[pedestrian][1]
	bigArr2.append([x, y])
	my_particles.append(Particle(x1, y1, size, random.randint(20,255), random.randint(20,255), random.randint(0,255)))



# for i in range(number_of_particles):
# 	size = 10
# 	# x = random.randint(size, width - size)
# 	# y = random.randint(size, height - size)
# 	x = My_Trajectory_Dict[]
# 	# x = bigArr[i][0][0]
# 	# y = bigArr[i][1][0]
# 	my_particles.append(Particle(x, y, size, random.randint(20,255), random.randint(20,255), random.randint(0,255)))


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill(background_colour)
	indexing = 0
	for particle in my_particles:
		particle.move(counter, bigArr2[indexing][0], bigArr2[indexing][1])
		indexing += 1
		particle.display()
		counter += 1
	pygame.display.update()
