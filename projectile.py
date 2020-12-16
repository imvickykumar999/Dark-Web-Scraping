import pygame, math
pygame.init() 
 
green = (0, 255, 0) 
light_blue = (0, 200, 255) 
black = (0, 0, 0) 
red = (255, 50, 50) 

X, Y = 1000, 600
g, a = -10, 25
u, b = 100, 60

display_surface = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption('Projectile')  
display_surface.fill(light_blue) 

pygame.draw.polygon(display_surface, green, 
    [(0, Y-100), (X, Y-X*math.sin(a/57.295)), (X, Y-100)]) 
pygame.draw.rect(display_surface, red, (0, Y-100, X, Y)) 

def drawGrid():
    blockSize = 100
    for x in range(X):
        for y in range(Y):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(display_surface, (255,255,255), rect, 1)

while True : 
    drawGrid()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 

    for t in range(100):
        a=0
        x = int(u*math.cos(b/57.295)*t + 0.5*g*math.sin(a/57.295)*t*t)
        y = Y - 100 - int(u*math.sin(b/57.295)*t + 0.5*g*math.cos(a/57.295)*t*t)

        pygame.draw.circle(display_surface, black, (x, y), 10, 0) 
        pygame.display.update()

        # print(x, y)
