""" remote """
import sys
import pygame

#pylint: disable=no-member

pygame.init()
clock = pygame.time.Clock()
joy = pygame.joystick.Joystick(0)
joy.init()
print(pygame.joystick.Joystick(0).get_name())
screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("test")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.JOYBUTTONDOWN:
            print(event)
        elif event.type == pygame.JOYHATMOTION:
            print(event)
    screen.fill(pygame.Color("white"))
    pygame.draw.rect(screen, pygame.Color("black"), (50,50,100,100))
    pygame.display.flip()
    clock.tick(60)
