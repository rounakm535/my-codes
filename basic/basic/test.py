import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def pygame_input():
    string = ""
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    
    if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key)  
        if len(key) == 1:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                string += key.upper()
            else:
                string += key
        elif key == "space":
            string = string + " "
        elif key == "backspace":
            string = string[:len(string) - 1]
        elif event.key == pygame.K_RETURN:  
            exit()
    return string

def main():
  screen = pygame.display.set_mode((800,600))
  string = ""
  pygame.font.init()
  myfont = pygame.font.Font(None,36)

  while True:
    string += pygame_input()
    pygame.draw.rect(screen, (0,0,0), (0,0,800,600))
    text = myfont.render(string, 1, (255,0,0))
    screen.blit(text, (0,0))
    pygame.display.flip()


if __name__ == '__main__': main()