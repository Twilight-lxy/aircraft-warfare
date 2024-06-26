import tkinter as tk
from queue import Queue


def restart(root: tk.Tk, threadQueue: Queue):
    threadQueue.put(("continue"))
    root.destroy()
    return True


def escgame(root: tk.Tk, threadQueue: Queue):
    threadQueue.put(("esc"))
    root.destroy()
    return True


def gameoverWindow(gameScore, threadQueue: Queue):
    root = tk.Tk()
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    height = 200
    width = 400
    scw = root.winfo_screenwidth()
    sch = root.winfo_screenheight()
    rsize = f"{width}x{height}+{round((scw-width)/2)}+{(round((sch-height)/2))}"
    root.geometry(rsize)
    root.resizable(width=False, height=False)

    menu = tk.Label(root, text="游戏结束", font="Any 30")
    menu.place(x=120, y=0)
    score = tk.Label(root, text="分数:" + str(gameScore), font="Any 25")
    score.place(x=120, y=60)
    b1 = tk.Button(
        root, text="重新开始", font="Any 25", command=lambda: restart(root, threadQueue)
    )
    b1.place(x=40, y=110)
    b2 = tk.Button(
        root, text="退出游戏", font="Any 25", command=lambda: escgame(root, threadQueue)
    )
    b2.place(x=200, y=110)
    root.mainloop()
