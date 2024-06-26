import pygame
import src.lib.Constants as CONSTANTS
from src.classes.User import User, UserException
from src.lib.Logo import showLogo
from src.lib.textBox import draw_text_box


def mainPage(
    username: User
) -> str:
    mouseInchangeUserTextBox = False
    mouseInStartTextBox = False
    mouseInRankingTextBox = False
    mouseInQuitTextBox = False
    while True:
        CONSTANTS.screen.fill(CONSTANTS.WHITE)
        CONSTANTS.screen.blit(CONSTANTS.superResourceDict.getResource(CONSTANTS.BGIMAGE), (0, 0))
        showLogo(0, 100)
        welcomeTextBox = draw_text_box(
            mess="Welcome " + username + " !",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=350,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        changeUserTextBox = draw_text_box(
            mess="Change User Info",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=450,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )

        startTextBox = draw_text_box(
            mess="START",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=550,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        rankingTextBox = draw_text_box(
            mess="Ranking List",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=650,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        quitTextBox = draw_text_box(
            mess="Back",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=750,
            textBoxMidX=CONSTANTS.WIDTH / 2,
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                if changeUserTextBox.collidepoint(mouse_position):
                    mouseInchangeUserTextBox = True
                else:
                    mouseInchangeUserTextBox = False

                if startTextBox.collidepoint(mouse_position):
                    mouseInStartTextBox = True
                else:
                    mouseInStartTextBox = False

                if rankingTextBox.collidepoint(mouse_position):
                    mouseInRankingTextBox = True
                else:
                    mouseInRankingTextBox = False

                if quitTextBox.collidepoint(mouse_position):
                    mouseInQuitTextBox = True
                else:
                    mouseInQuitTextBox = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseInchangeUserTextBox:
                    return "changePassword"
                if mouseInStartTextBox:
                    return "start"
                if mouseInRankingTextBox:
                    return "ranking"
                if mouseInQuitTextBox:
                    return "back"
        if mouseInchangeUserTextBox:
            changeUserTextBox = draw_text_box(
                mess="Change User Info",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=450,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        if mouseInStartTextBox:
            startTextBox = draw_text_box(
                mess="START",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=550,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        if mouseInRankingTextBox:
            rankingTextBox = draw_text_box(
                mess="Ranking List",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=650,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        if mouseInQuitTextBox:
            quitTextBox = draw_text_box(
                mess="Back",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=750,
                textBoxMidX=CONSTANTS.WIDTH / 2,
                textColor=CONSTANTS.WHITE,
                textBoxSideWidth=0,
            )
        pygame.display.flip()
        CONSTANTS.mainClock.tick(CONSTANTS.FPS)
