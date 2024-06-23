import tkinter as tk
from queue import Queue
#from images import *
#from src.lib.DataBaseFunc import *
def backgame(root:tk.Tk,threadQueue:Queue):
    threadQueue.put(("continue"))
    root.destroy()
    return True
def escgame(root:tk.Tk,threadQueue:Queue):
    threadQueue.put(("esc"))
    root.destroy()
    return True

def pasueMain(threadQueue:Queue):
    root = tk.Tk()
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    height=200
    width=400
    scw=root.winfo_screenwidth()
    sch=root.winfo_screenheight()
    rsize =f'{width}x{height}+{round((scw-width)/2)}+{(round((sch-height)/2))}'
    root.geometry(rsize)
    root.resizable(width=False,height=False)

    canvas = tk.Canvas(root, width=400, height=200)
    canvas.pack()
    img = tk.PhotoImage(file="images/background.png")
    canvas.create_image(0, 0, anchor="nw", image=img)

    menu = tk.Label(root, text='暂 停',bg='blue',font=('宋体', 40))
    menu.place(x=120, y=20)


    b1 = tk.Button(root, text='返回游戏',font="Any 25",bg='red',command=lambda:backgame(root,threadQueue))
    b1.place(x=40,y=110)
    b2 = tk.Button(root, text='退出游戏',font="Any 25",bg='green',command=lambda:escgame(root,threadQueue))
    b2.place(x=200,y=110)
    root.mainloop()