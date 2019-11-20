import pygame
import math

class Square(object):
    def __init__(self, size, XY, mass, velocity):
        self.x = XY[0]
        self.y = XY[1]
        self.mass = mass
        self.v = velocity
        self.size = size

    def collision(self, otherblock):
        if self.x + self.size < otherblock.x or self.x > otherblock.x + otherblock.size:
            return False
        else:
            return True

    def NewVelocity(self, otherblock):
        sumM = self.mass + otherblock.mass
        newV = (self.mass - otherblock.mass)/sumM * self.v
        newV += (2 * otherblock.mass/ sumM) * otherblock.v
        return newV

    def collide_wall(self):
        if self.x <= 0:
            self.v *= -1
            return True

    def update(self):
        self.x += self.v

    def draw(self, background, otherblock):
        if self.x < 10:
            pygame.draw.rect(background, red, [10, self.y , self.size, self.size])
            pygame.draw.rect(background, red, [0, otherblock.y , otherblock.size, otherblock.size])
        else:
            pygame.draw.rect(background, red, [self.x, self.y , self.size, self.size])
            pygame.draw.rect(background, red, [otherblock.x, otherblock.y , otherblock.size, otherblock.size])


def redraw():
    background.fill(white)
    pygame.draw.rect(background, gray, [0 , 0, 800, 250])
    SquareBig.draw(background, SquareSmall)
    font = pygame.font.SysFont(None, 50)
    text = font.render(str(count), True, (0,0,0))
    background.blit(text, [100, 270])
    pygame.display.update()

width, height = 800, 400
white = (255,255,255)
gray = (190,190,190)
red = (200,0,0)

pygame.init()
power = math.pow(100, 5)
background = pygame.display.set_mode((width, height))

SquareBig = Square(50, (320,200), power, -0.9/10000)
SquareSmall = Square(10, (100, 240), 1, 0)


count = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for i in range(10000):
        if(SquareSmall.collision(SquareBig)):
            count+=1
            v1 = SquareSmall.NewVelocity(SquareBig)
            v2 = SquareBig.NewVelocity(SquareSmall)
            SquareBig.v = v2
            SquareSmall.v = v1
        if SquareSmall.collide_wall():
            count+=1
        SquareBig.update()
        SquareSmall.update()
    redraw()


pygame.quit()
