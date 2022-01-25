import pygame

def main():
   pygame.init()
   OknoGry=pygame.display.set_mode((400,400),0,32)
   run=True
   while(run):
       pygame.time.delay(200)
       wazShape=pygame.Rect((140,140),(47,47))
       pygame.draw.rect(OknoGry,(255,192,203),wazShape)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run=False
       pygame.display.update()

main() 