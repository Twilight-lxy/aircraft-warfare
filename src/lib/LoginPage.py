import pygame
from src.lib.LoginAndRegester import getLoginMess
import src.lib.Constants as CONSTANTS
from src.classes.User import User, UserException
from src.lib.Logo import showLogo
from src.lib.textBox import draw_text_box

def logIn() -> str:
    while not CONSTANTS.threadQueue.empty():
        CONSTANTS.threadQueue.get()
    mess, username = ("logined", "null")
    mouseInloginTextBox = False
    mouseInQuitTextBox = False
    while True:
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        CONSTANTS.screen.blit(CONSTANTS.superResourceDict.getResource(CONSTANTS.BGIMAGE), (0, 0))
        showLogo(0, 100)
        loginTextBox = draw_text_box(
            mess="login or register",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=450,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        quitTextBox = draw_text_box(
            mess="quit",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=550,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                if loginTextBox.collidepoint(mouse_position):
                    mouseInloginTextBox = True
                else:
                    mouseInloginTextBox = False
                if quitTextBox.collidepoint(mouse_position):
                    mouseInQuitTextBox = True
                else:
                    mouseInQuitTextBox = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseInloginTextBox:
                    getLoginMess(CONSTANTS.threadQueue)
                if mouseInQuitTextBox:
                    pygame.quit()
                    break
        if mess == "logined":
            break
        if mouseInloginTextBox:
            loginTextBox = draw_text_box(
                mess="login or register",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=450,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        if mouseInQuitTextBox:
            loginTextBox = draw_text_box(
                mess="quit",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=550,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        try:
            (mess, username) = CONSTANTS.threadQueue.get(False)
        except:
            pass
        pygame.display.flip()
        CONSTANTS.mainClock.tick(CONSTANTS.FPS)
    return username
