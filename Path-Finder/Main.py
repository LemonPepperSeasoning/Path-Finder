import pygame
import numpy as np
import A_star
pygame.init()

screen = pygame.display.set_mode([500, 500]) #pygame.RESIZABLE
pygame.display.set_caption("First Game")

start = (0, 0)
end = (49,49)

class node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x*10, y*10, 10, 10)
        self.color = (255,255,255)
                
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, 0) 
        
    def changeColorToRed(self):
        self.color = (255,0,0)
        self.draw()
    
    def changeColorToBlue(self):
        self.color = (0,0,255)
        self.draw()

cols = 50
grid = [0 for i in range(cols)]
graph = [0 for i in range(cols)]
row = 50
for i in range(cols):
    grid[i] = [0 for i in range(row)]
    graph[i] = [0 for i in range(row)]

# Create Spots
for i in range(cols):
    for j in range(row):
        x = node(i, j)
        grid[i][j] = x
        x.draw()
        graph[i][j] = 0

run = True
findPath = False     
while run:
    # pygame.time.delay(1)
    
    if findPath:
        path = A_star.search(graph, start, end)
        if path == None:
            print("no path")
            run = False
        else:
            for i in range(0,len(path)):
                for j in range(0,len(path[i])):
                    if path[i][j] != -1:
                        node(i, j).changeColorToRed()
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if pygame.mouse.get_pressed()[0] & ( not findPath ) :
            try:
                x,y = pygame.mouse.get_pos()
                x1 = x // (500 // cols)
                y1 = y // (500 // row)
                grid[x1][y1].changeColorToBlue();   
                graph[x1][y1] = 1  
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                findPath = True

    pygame.display.update()

pygame.quit()