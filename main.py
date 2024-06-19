from concurrent.futures import thread
import threading
from queue import Queue
import time
import pygame
from src.lib.Constants import WINDOWS_SIZE,WIDTH,WHITE
import src.lib.LoadResource
import traceback
import src.lib.Logo
import src.lib.textBox
from src.classes.ResourceDict import ResourceDict

def initGame():
    global screen
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    pygame.display.set_caption("飞机大战")
    loadResourceThreading = threading.Thread(target=loadresource, name="loadresource", args=("loadresource",threadQueue))
    loadResourceThreading.daemon = True
    loadResourceThreading.start()
    mess,per=("load","0")
    while True:
        screen.fill(WHITE)
        src.lib.Logo.showLogo(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if(mess=="loaded"):
            src.lib.textBox.draw_text_box(screen,mess="loading is complete!",fontSize=25,textBoxHeight=50,textBoxWidth=300,textBoxMidY=500,textBoxMidX=WIDTH/2)
            pygame.display.flip()
            break
        else:
            src.lib.textBox.draw_text_box(screen,mess="loading..."+per+"%",fontSize=25,textBoxHeight=50,textBoxWidth=200,textBoxMidY=500,textBoxMidX=WIDTH/2)
        pygame.display.flip()
        (mess,per)=threadQueue.get(True,20)
    loadResourceThreading.join()
    time.sleep(1)
    screen.fill(WHITE)
    src.lib.Logo.showLogo(screen)
    pygame.display.flip()

        
def loadresource(name:str,queue:Queue):
    global soundResourceDict
    queue.put(("loading","0"))
    pygame.mixer.music.load("sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    queue.put(("loading","10"))
    background = pygame.image.load("images/background.png").convert()
    queue.put(("loading","20"))
    soundResourceDict = src.lib.LoadResource.loadSoundResource()
    queue.put(("loading","100"))
    queue.put(("loaded","100"))

def main():
    global screen
    global soundResourceDict
    global threadQueue
    threadQueue = Queue()
    initGame()

    while True:
        for event in pygame.event.get(): # 获取用户事件
            if event.type == pygame.QUIT: # 如果事件为关闭窗口
                # 退出pygame
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_pos()
            
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
