#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: A.Akdogan
"""
from random import randint
import os
import sys 
import time
from time import sleep
print(sys.path)

class Node:

    def __init__(self, x, y):

        self.x = x 
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self. obstacle = False


    def add_neighbors(self,grid, columns, rows):

        neighbor_x = self.x
        neighbor_y = self.y
    
        if neighbor_x < columns - 1:
            self.neighbors.append(grid[neighbor_x+1][neighbor_y])
        if neighbor_x > 0:
            self.neighbors.append(grid[neighbor_x-1][neighbor_y])
        if neighbor_y < rows -1:
            self.neighbors.append(grid[neighbor_x][neighbor_y +1])
        if neighbor_y > 0: 
            self.neighbors.append(grid[neighbor_x][neighbor_y-1])
        #diagonals
        """ if neighbor_x > 0 and neighbor_y > 0:
            self.neighbors.append(grid[neighbor_x-1][neighbor_y-1])
        if neighbor_x < columns -1 and neighbor_y > 0:
            self.neighbors.append(grid[neighbor_x+1][neighbor_y-1])
        if neighbor_x > 0 and neighbor_y <rows -1:
            self.neighbors.append(grid[neighbor_x-1][neighbor_y+1])
        if neighbor_x < columns -1 and neighbor_y < rows -1:
            self.neighbors.append(grid[neighbor_x+1][neighbor_y+1]) """


        
class AStar:

    def __init__(self, cols, rows, start, end):

        self.cols = cols
        self.rows = rows
        self.start = start
        self.end = end
        self.obstacle_ratio = False
        self.obstacle_list = False

    @staticmethod
    def clean_open_set(open_set, current_node):

        for i in range(len(open_set)):
            if open_set[i] == current_node:
                open_set.pop(i)
                break

        return open_set

    @staticmethod
    def h_score(current_node, end):

        distance =  abs(current_node.x - end.x) + abs(current_node.y - end.y)
        
        return distance

    @staticmethod
    def create_grid(cols, rows):

        grid = []
        for _ in range(cols):
            grid.append([])
            for _ in range(rows):
                grid[-1].append(0)
        
        return grid

    @staticmethod
    def fill_grids(grid, cols, rows, obstacle_ratio = False, obstacle_list = False):

        for i in range(cols):
            for j in range(rows):
                grid[i][j] = Node(i,j)
                if obstacle_ratio == False:
                    pass
                else:
                    n = randint(0,100)
                    if n < obstacle_ratio: grid[i][j].obstacle = True
        if obstacle_list == False:
            pass
        else:
            for i in range(len(obstacle_list)):
                grid[obstacle_list[i][0]][obstacle_list[i][1]].obstacle = True

        return grid

    @staticmethod
    def get_neighbors(grid, cols, rows):
        for i in range(cols):
            for j in range(rows):
                grid[i][j].add_neighbors(grid, cols, rows)
        return grid
    
    @staticmethod
    def start_path(open_set, closed_set, current_node, end):

        best_way = 0
        for i in range(len(open_set)):
            if open_set[i].f < open_set[best_way].f:
                best_way = i

        current_node = open_set[best_way]
        final_path = []
        if current_node == end:
            temp = current_node
            while temp.previous:
                final_path.append(temp.previous)
                temp = temp.previous

        open_set = AStar.clean_open_set(open_set, current_node)
        closed_set.append(current_node)
        neighbors = current_node.neighbors
        for neighbor in neighbors:
            if (neighbor in closed_set) or (neighbor.obstacle == True):
                continue
            else:
                temp_g = current_node.g + 1
                control_flag = 0
                for k in range(len(open_set)):
                    if neighbor.x == open_set[k].x and neighbor.y == open_set[k].y:
                        if temp_g < open_set[k].g:
                            open_set[k].g = temp_g
                            open_set[k].h= AStar.h_score(open_set[k], end)
                            open_set[k].f = open_set[k].g + open_set[k].h
                            open_set[k].previous = current_node
                        else:
                            pass
                        control_flag = 1
                if control_flag == 1:
                    pass
                else:
                    neighbor.g = temp_g
                    neighbor.h = AStar.h_score(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current_node
                    open_set.append(neighbor)

        return open_set, closed_set, current_node, final_path

    def main(self):

        grid = AStar.create_grid(self.cols, self.rows)
        grid = AStar.fill_grids(grid, self.cols, self.rows, obstacle_ratio = 30)
        grid = AStar.get_neighbors(grid, self.cols, self.rows)
        open_set  = []
        closed_set  = []
        current_node = None
        final_path  = []
        open_set.append(grid[self.start[0]][self.start[1]])
        self.end = grid[self.end[0]][self.end[1]]
        while len(open_set) > 0:
            open_set, closed_set, current_node, final_path = AStar.start_path(open_set, closed_set, current_node, self.end)
            if len(final_path) > 0:
                break

        return final_path


cols = 25
rows = 25 
start = [0,0]
end = [24,24]
open_set  = []
closed_set  = []
current_node = None
final_path  = []
grid = []


def show_func(grid_element,color, width,height): 
    if grid_element.obstacle == True:
            fill("black")
    else:
        fill(color)
    noStroke()
    rect(grid_element.x * width, grid_element.y * height, width-1 , height-1)


def setup():
    global grid
    createCanvas(500, 500)
    background(160)

        
    
flag = False   


def draw():
    
    global grid
    global end
    global open_set
    global closed_set
    global final_path
    global current_node
    global flag
    global start

    global cols 
    global rows 
  
    frameRate(60)
    w = width / cols
    h = height / rows
    if flag == False:
        
 

        grid = AStar.create_grid(cols, rows)   
        grid = AStar.fill_grids(grid, cols, rows, obstacle_ratio = 30)
        grid = AStar.get_neighbors(grid, cols, rows)
        start = grid[start[0]][start[1]]
        end = grid[end[0]][end[1]]
        end.obstacle = False
        start.obstacle = False

        background(0)
        for i in range(cols):
            for j in range(rows):
                show_func(grid[i][j], color(255),w,h)
        stroke(0,0,0)
        line(0, 0, 0, width)
        line(0,0,height, 1)
        open_set.append(start)

        
        flag = True

    if len(open_set) > 0:
        open_set, closed_set, current_node, final_path = AStar.start_path(open_set, closed_set, current_node, end)

    
    #grid
        show_func(start, "green", w,h)
        show_func(end, "red",w,h)
        for i in range(len(open_set)):
            #show_func(open_set[i], "#00ffbf",w,h)
            show_func(open_set[i], "#00ffbf",w,h)

        for i in range(len(closed_set)):
            show_func(closed_set[i], "#ffa500",w,h)
            show_func(start, "green", w,h)

        show_func(current_node, "#8a2be2",w,h)

        if len(open_set) == 0:
            print("No way!")
            #noLoop()
    
            frameRate(1)
            cols = 25
            rows = 25 
            start = [0,0]
            end = [24,24]
            open_set  = []
            closed_set  = []
            current_node = None
            final_path  = []
            grid = []
            flag = False
            

        if len(final_path) > 0:
            for i in range(len(final_path)):
                show_func(final_path[i], "#8a2be2",w,h)
                #show_func(final_path[i], "red",w,h)
            show_func(start, "green", w,h)
            show_func(end, "red",w,h)

            print("Done!!")
            frameRate(1)
            cols = 25
            rows = 25 
            start = [0,0]
            end = [24,24]
            open_set  = []
            closed_set  = []
            current_node = None
            final_path  = []
            grid = []
            flag = False
            
   
            
