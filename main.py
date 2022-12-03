
import pygame
import math 
import  env, sensors
import numpy as np
import sys

environment = env.buildEnviroment((600,1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(50, environment.originalMap , uncertainty = (0.1 , 0.05) )
print('sensor defined')
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()
running = True

while running :
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
            
    if sensorON:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_Obstacles()
        environment.dataStorage(sensor_data)
        environment.show_sensorData()
    environment.map.blit(environment.infomap , (0,0) )
    pygame.display.update()
    

    
    
    