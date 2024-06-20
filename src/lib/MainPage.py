import pygame
from src.lib.Constants import FPS, WHITE, WIDTH
from src.classes.User import User, UserException
from src.lib.Logo import showLogo
from src.lib.textBox import draw_text_box


def mainPage(
    screen: pygame.Surface, mainClock: pygame.time.Clock, username: User
) -> str:
    mouseInWelcomeTextBox = False
    mouseInStartTextBox = False
    mouseInRankingTextBox = False
    mouseInQuitTextBox = False
    while True:
        screen.fill(WHITE)
        showLogo(screen, 0, 100)
        welcomeTextBox = draw_text_box(
            screen,
            mess="Welcome " + username + " !",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=350,
            textBoxMidX=WIDTH / 2,
        )
        startTextBox = draw_text_box(
            screen,
            mess="START",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=450,
            textBoxMidX=WIDTH / 2,
        )
        rankingTextBox = draw_text_box(
            screen,
            mess="Ranking List",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=550,
            textBoxMidX=WIDTH / 2,
        )
        quitTextBox = draw_text_box(
            screen,
            mess="Back",
            fontSize=25,
            textBoxHeight=50,
            textBoxWidth=300,
            textBoxMidY=650,
            textBoxMidX=WIDTH / 2,
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                if welcomeTextBox.collidepoint(mouse_position):
                    mouseInWelcomeTextBox = True
                else:
                    mouseInWelcomeTextBox = False

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
                if welcomeTextBox:
                    pass  # showUserMess()
                if mouseInStartTextBox:
                    return "start"
                if mouseInRankingTextBox:
                    return "rankin"
                if mouseInQuitTextBox:
                    return "back"
        if mouseInWelcomeTextBox:
            welcomeTextBox = draw_text_box(
                screen,
                mess="Welcome " + username + " !",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=350,
                textBoxMidX=WIDTH / 2,
                textColor=WHITE,
                textBoxSideWidth=0,
            )
        if mouseInStartTextBox:
            startTextBox = draw_text_box(
                screen,
                mess="START",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=450,
                textBoxMidX=WIDTH / 2,
                textColor=WHITE,
                textBoxSideWidth=0,
            )
        if mouseInRankingTextBox:
            rankingTextBox = draw_text_box(
                screen,
                mess="Ranking List",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=550,
                textBoxMidX=WIDTH / 2,
                textColor=WHITE,
                textBoxSideWidth=0,
            )
        if mouseInQuitTextBox:
            quitTextBox = draw_text_box(
                screen,
                mess="Back",
                fontSize=25,
                textBoxHeight=50,
                textBoxWidth=300,
                textBoxMidY=650,
                textBoxMidX=WIDTH / 2,
                textColor=WHITE,
                textBoxSideWidth=0,
            )
        pygame.display.flip()
        mainClock.tick(FPS)
