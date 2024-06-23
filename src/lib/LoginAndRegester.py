from queue import Queue
import tkinter as tk
import tkinter.messagebox
from src.lib.DataBaseFunc import *
def logic(username,password,root:tk.Tk,threadQueue:Queue):
    if username==''or password=='':
        tk.messagebox.showinfo(title='信息',message='账号或密码为空！')
        return
    user=User(username,password)
    if checkLogin(user):
        tk.messagebox.showinfo(title='信息',message='登录成功！')
        threadQueue.put(("logined",username))
        root.destroy()
    else:
        tk.messagebox.showinfo(title='错误',message='账户与密码不符！')
def submit(username,password,repassword,root:tk.Tk,froot:tk.Tk,threadQueue:Queue):
    if username==''or password=='':
        tk.messagebox.showinfo(title='信息',message='账号或密码为空！')
        return
    user=User(username,password)
    if(userInsert(user) and password == repassword):
        tk.messagebox.showinfo(title='信息',message='注册成功！')
        root.destroy()
        getLoginMess(threadQueue)
    else:
        tk.messagebox.showinfo(title='错误',message='注册失败！')
def register(froot:tk.Tk,threadQueue:Queue):
    froot.destroy()
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    scw = root.winfo_screenwidth()
    sch = root.winfo_screenheight()
    height = 200
    width = 400
    rsize = f'{width}x{height}+{round((scw - width) / 2)}+{(round((sch - height) / 2))}'
    root.geometry(rsize)
    root.resizable(width=False, height=False)
    lambdaUsername = tk.Label(root, text='账号:', font=('宋体', 16))
    lambdaUsername.place(x=25, y=20)
    lambdapassword = tk.Label(root, text='密码：', font=('宋体', 16))
    lambdapassword.place(x=25, y=70)
    lambdarepassword = tk.Label(root, text='再次输入密码：', font=('宋体', 16))
    lambdarepassword.place(x=0, y=120)
    username = tk.StringVar(root, value='')
    password = tk.StringVar(root, value='')
    repassword = tk.StringVar(root, value='')
    e_name = tk.Entry(root, width=30, textvariable=username)
    e_name.place(x=100, y=25)
    e_pwd = tk.Entry(root, width=30, show='*', textvariable=password)
    e_pwd.place(x=100, y=75)
    repwd = tk.Entry(root, width=25, show='*', textvariable=repassword)
    repwd.place(x=140, y=125)
    b1 = tk.Button(root, text='提交',width=10,command=lambda: submit(e_name.get(),e_pwd.get(),repwd.get(),root,froot,threadQueue))
    b1.place(x=80, y=160)
    b2 = tk.Button(root, text='返回', width=10,command=lambda: getLoginMess(threadQueue,root))
    b2.place(x=200, y=160)
    root.mainloop()
def getLoginMess(threadQueue:Queue,root:tk.Tk=None) -> None:
    if(root!=None):
        root.destroy()
    username = str()
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    # root.overrideredirect(True) 
    scw=root.winfo_screenwidth()
    sch=root.winfo_screenheight()
    height=200
    width=400
    rsize =f'{width}x{height}+{round((scw-width)/2)}+{(round((sch-height)/2))}'
    root.geometry(rsize)
    root.resizable(width=False,height=False)
    lambdaUsername = tk.Label(root,text='账号:',font=('宋体',18))
    lambdaUsername.place(x=25,y=20)
    lambdapassword = tk.Label(root,text='密码：',font=('宋体',18))
    lambdapassword.place(x=25,y=80)
    username=tk.StringVar(root,value='')
    password=tk.StringVar(root,value='')
    e_name=tk.Entry(root,width=30,textvariable=username)
    e_name.place(x=100,y=30)
    e_pwd=tk.Entry(root,width=30,show='*',textvariable=password)
    e_pwd.place(x=100,y=90)
    b1=tk.Button(root,text='登录',width=10,command=lambda: logic(e_name.get(),e_pwd.get(),root,threadQueue))
    b1.place(x=80,y=140)
    b2=tk.Button(root,text='注册',width=10,command=lambda: register(root,threadQueue))
    b2.place(x=200,y=140)
    root.mainloop()
    # threadQueue.put(("logined",username))
        