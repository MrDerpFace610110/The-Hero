#pygame
import pygame, sys
from pygame import mixer

#Import stuff
from button import Button
from settings import *
from Level import Level1
from Game_Data import level_0

##Initilization 
pygame.init()

iconImg = pygame.image.load("Icon.png")

#width = 1280
#height = 720

SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("A Journey's First Choice")
pygame.display.set_icon(iconImg)
mixer.init()

BG = pygame.image.load("MenuBG.png")
SettingBG = pygame.image.load("SettingBG.png")

##Get Level info
#level1 = Level1(level_map, SCREEN)
Level1 = Level1(level_0, SCREEN)

##Sound
Intro = pygame.mixer.Sound("LevelIntro.wav")
Select = pygame.mixer.Sound("Select.wav")

##Title Stuff
Title = pygame.image.load("Title.png")

#KeySprites
KKey = pygame.image.load("KKey.png")
LKey = pygame.image.load("LKey.png")
JKey = pygame.image.load("JKey.png")
WKey = pygame.image.load("WKey.png")
AKey = pygame.image.load("AKey.png")
SKey = pygame.image.load("SKey.png")
DKey = pygame.image.load("DKey.png")
IKey = pygame.image.load("IKey.png")
OKey = pygame.image.load("OKey.png")
MKey = pygame.image.load("MKey.png")
SpaceKey = pygame.image.load("SpaceKey.png")
EnterKey = pygame.image.load("EnterKey.png")

#self explained
def get_font(size): 
    return pygame.font.Font("text.ttf", size)

#play button
def play():
    while True:
        pygame.display.set_caption("You Quest Begins...")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("blue")

        PLAY_TEXT = get_font(45).render("Shit my Background Crashed", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        #level1.run()
        Level1.run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Sound.play(Select)
                    main_menu()

        pygame.display.update()

#guide button
def guide():
    while True:
        pygame.display.set_caption("Everything to Start Your Journey")
        GUIDE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        #SCREEN.blit(SettingBG, (0, 0))
        
        #painfully displaying the key sprites and text
        SCREEN.blit(WKey, (100, 25))
        SCREEN.blit(SKey, (100, 100))
        SCREEN.blit(AKey, (25, 100))
        SCREEN.blit(DKey, (175, 100))
        Move_Text = get_font(30).render("Movement Keys", True, "White")
        Move_Rect = Move_Text.get_rect(center = (470, 100))
        SCREEN.blit(Move_Text, Move_Rect)
        
        
        SCREEN.blit(JKey, (100, 225))
        J_Text = get_font(30).render("Rope Dart/Back", True, "White")
        J_Rect = J_Text.get_rect(center = (490, 255))
        SCREEN.blit(J_Text, J_Rect)
        
        SCREEN.blit(KKey, (100, 325))
        K_Text = get_font(30).render("Attack", True, "White")
        K_Rect = K_Text.get_rect(center = (370, 355))
        SCREEN.blit(K_Text, K_Rect)
        
        SCREEN.blit(LKey, (100, 425))
        L_Text = get_font(30).render("Lightfoot Tabi", True, "White")
        L_Rect = L_Text.get_rect(center = (490, 455))
        SCREEN.blit(L_Text, L_Rect)
        
        SCREEN.blit(SpaceKey, (40, 525))
        Space_Text = get_font(30).render("Jump/Confirm", True, "White")
        Space_Rect = Space_Text.get_rect(center = (460, 555))
        SCREEN.blit(Space_Text, Space_Rect)
        
        SCREEN.blit(OKey, (800, 75))
        O_Text = get_font(30).render("Shuriken", True, "White")
        O_Rect = O_Text.get_rect(center = (1060, 110))
        SCREEN.blit(O_Text, O_Rect)
        
        SCREEN.blit(MKey, (800, 225))
        M_Text = get_font(30).render("Map", True, "White")
        M_Rect = M_Text.get_rect(center = (990, 255))
        SCREEN.blit(M_Text, M_Rect)
                
        SCREEN.blit(IKey, (800, 325))
        I_Text = get_font(30).render("Inventory", True, "White")
        I_Rect = I_Text.get_rect(center = (1075, 355))
        SCREEN.blit(I_Text, I_Rect)
        
        SCREEN.blit(EnterKey, (745, 425))
        Enter_Text = get_font(30).render("Pause", True, "White")
        Enter_Rect = Enter_Text.get_rect(center = (1025, 455))
        SCREEN.blit(Enter_Text, Enter_Rect)

        GUIDE_BACK = Button(image=None, pos=(640, 680), text_input="[ BACK ]", font=get_font(30), base_color="white", hovering_color="Green")

        GUIDE_BACK.changeColor(GUIDE_MOUSE_POS)
        GUIDE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(GUIDE_MOUSE_POS):
                    pygame.mixer.Sound.play(Select)
                    main_menu()

        pygame.display.update()

#display main menu
def main_menu():
    while True:
        pygame.display.set_caption("A Journey's First Choice")
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(Title, (225, 25))
    
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("PlayButton.png"), pos=(640, 325), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        GUIDE_BUTTON = Button(image=pygame.image.load("GuideButton.png"), pos=(640, 475), text_input="GUIDE", font=get_font(70), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("QuitButton.png"), pos=(640, 625), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(Select)
                    play()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Sound.play(Select)
                    guide()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#start on opening
#pygame.mixer.Sound.play(Intro)
main_menu()