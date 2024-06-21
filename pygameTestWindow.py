import pygame
from src.lib.Constants import *
import traceback
import src.lib.textBox
from src.lib.LoginAndRegester import *
from queue import Queue
screen = None
def init():
    global screen 
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    pygame.display.set_caption("PygamTest")

def main():
    # clock = pygame.time.Clock()
    # global screen
    # init()
    # screen.fill(WHITE)
    # loadevent = pygame.event.Event(pygame.USEREVENT,tip="load")
    # pygame.event.post(loadevent)

    # pygame.event.set_timer(event, 500)
    # src.lib.textBox.draw_text_box(screen,mess="test",textBoxWidth=100)
    # pygame.display.flip()
    # loadflag=0
    # while True:
    #     for event in pygame.event.get(): # 获取用户事件
    #         if event.type == pygame.QUIT: # 如果事件为关闭窗口
    #             # 退出pygame
    #             pygame.quit()
    #         if event.type == pygame.KEYDOWN:
    #             pygame.event.post(loadevent)
    #         if event.type == pygame.USEREVENT and event.tip=="load" and loadflag == 0:
    #             print(1)
    #             loadflag=1
    #             y=100
    #             while True:
    #                 for event in pygame.event.get():
    #                     if event.type == pygame.QUIT: # 如果事件为关闭窗口
    #                         # 退出pygame
    #                         pygame.quit()
    #                     print(y)
    #                     if event.type == pygame.USEREVENT and event.dict=="loadfinish":
    #                         loadflag=2
    #                         break
    #                     y+=1
    #                     src.lib.textBox.draw_text_box(screen,mess="test",textBoxWidth=100,textBoxMidX=200,textBoxMidY=y)
    #                     pygame.display.flip()
    #                     clock.tick(1)
    #     clock.tick(30)
    #     pygame.display.flip()
    queue = Queue()
    getLoginMess(queue)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()

    

    
    
    
    