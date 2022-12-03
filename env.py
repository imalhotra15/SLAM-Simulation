# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 22:56:41 2022

@author: ishaa
"""

import pygame
import math

class buildEnviroment :
    def __init__(self , MapDimensions) :
        # pygame.init()
        
        self.pointCloud = []
        self.externalMap = pygame.image.load('map3.png')
        self.maph , self.mapw = MapDimensions
        self.map = pygame.display.set_mode((self.mapw , self.maph))
        self.MapWindowName = 'RRT Path Planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map.blit(self.externalMap , (0,0))
        # Colors
        self.black = (0 , 0 , 0)
        self.grey = (70 , 70 , 70)
        self.blue = (0 , 0 , 225)
        self.green = (0 , 225 , 0)
        self.red = (225 , 0 , 0)
        self.white = (225 , 225 , 225)
        
        
        
    def AD2pos(self , distance , angle , robotPosition) :
        x = robotPosition[0] + distance*math.cos(angle)
        y = robotPosition[1] - distance*math.sin(angle)
        return (int(x) , int(y))
    
    def dataStorage(self , data) :
        print(self.pointCloud)
        for element in data:
            point = self.AD2pos(element[0] , element[1] , element[2])
            if point not in self.pointCloud:
                self.pointCloud.append(point)
    
    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]) , int(point[1]) ) , (255,0,0) )
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        