import pygame
import random

def main():
    xApple=random.randint(0,9)*40+20
    yApple=random.randint(0,9)*40+20
    pygame.init()
    OknoGry=pygame.display.set_mode((400,400),0,32)
    run=True
    zmienna1=120
    zmienna2=120
    while(run):
        pozycja=[1,2,3,5,7,"a","d"]
        print("To jest tekst:",pozycja)
        OknoGry.fill((0,0,0))
        pygame.time.delay(200)
        #rysowanie weza
        wazShape=pygame.Rect((zmienna1,zmienna2),(40,40))
        pygame.draw.rect(OknoGry,(255,192,203),wazShape)
            #rysowanie jabłka
        pygame.draw.circle(OknoGry,(0,255,0),(xApple,yApple),20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            #ruch weza
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zmienna2=zmienna2-40
                elif event.key == pygame.K_DOWN:
                    zmienna2=zmienna2+40
                elif event.key == pygame.K_LEFT:
                    zmienna1=zmienna1-40
                elif event.key == pygame.K_RIGHT:
                    zmienna1=zmienna1+40
        #waż zjada jabłko
        if zmienna1==xApple-20 and zmienna2==yApple-20:
            xApple=random.randint(0,9)*40+20
            yApple=random.randint(0,9)*40+20
            pygame.draw.circle(OknoGry,(255,255,0),(xApple,yApple),20)
       #zmienna1=zmienna1+20
       #zmienna2=zmienna2+20
       #przejście strona prawa
        if zmienna1>400:
            zmienna1=0
            #przejście dół
        if zmienna2>400:
            zmienna2=0
        #przejście strona lewa
        if zmienna1<0:
            zmienna1=400
            #przejście góra
        if zmienna2<0:
            zmienna2=400    
        pygame.display.update()

main() 