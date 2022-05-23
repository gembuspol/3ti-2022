import pygame
import pygame_menu
import lekcja1
def iloscJablek(value,ilosc):
    lekcja1.iloscJablek=ilosc
def zmianaRozdzielczosci(nazwaPola,atrybut):
    lekcja1.rozdzielczosc=atrybut
def zmienKolorWaz1(value):
    lekcja1.zmienaKolorWaz1(value)
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((400,400))
    pygame.display.set_caption("Menu Snake")
    menu = pygame_menu.Menu('Snake 3TI', 400, 400,theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Start Gry",lekcja1.main,background_color=(0,0,0))
    menu.add.selector("Rozmiar ekranu",[('400x400',400),('600x600',600),('800x800',800)],onchange=zmianaRozdzielczosci)
    menu.add.color_input("Kolor wąż 1",'rgb',default=(25,25,100),onreturn=zmienKolorWaz1)
    menu.add.selector("Ilość jabłek",[("1",1),("3",3),("5",5),("10",10),("20",20)],onchange=iloscJablek)
    menu.mainloop(OknoMenu)

main()