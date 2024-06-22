from queue import Queue
import tkinter as tk
import tkinter.messagebox
from src.lib.DataBaseFunc import *
def logic(username,password,root:tk.Tk,threadQueue:Queue):
    user=User(username,password)
    if checkLogin(user):
        tk.messagebox.showinfo(title='信息',message='登录成功！')
        threadQueue.put(("logined",username))
        root.destroy()
    else:
        tk.messagebox.showinfo(title='错误',message='账户与密码不符！')
def submit(username,password,repassword,root:tk.Tk,froot:tk.Tk,threadQueue:Queue):
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
    root.overrideredirect(True) 
    scw = root.winfo_screenwidth()
    sch = root.winfo_screenheight()
    height = 150
    width = 300
    rsize = f'{width}x{height}+{round((scw - width) / 2)}+{(round((sch - height) / 2))}'
    root.geometry(rsize)
    root.resizable(width=False, height=False)
    lambdaUsername = tk.Label(root, text='账号:', font=('宋体', 10))
    lambdaUsername.place(x=20, y=20)
    lambdapassword = tk.Label(root, text='密码：', font=('宋体', 10))
    lambdapassword.place(x=20, y=50)
    lambdarepassword = tk.Label(root, text='再次输入密码：', font=('宋体', 10))
    lambdarepassword.place(x=0, y=80)
    username = tk.StringVar(root, value='')
    password = tk.StringVar(root, value='')
    repassword = tk.StringVar(root, value='')
    e_name = tk.Entry(root, width=20, textvariable=username)
    e_name.place(x=100, y=20)
    e_pwd = tk.Entry(root, width=20, show='*', textvariable=password)
    e_pwd.place(x=100, y=50)
    repwd = tk.Entry(root, width=20, show='*', textvariable=repassword)
    repwd.place(x=100, y=80)
    b1 = tk.Button(root, text='提交', command=lambda: submit(e_name.get(),e_pwd.get(),repwd.get(),root,froot,threadQueue))
    b1.place(x=100, y=110)
    b2 = tk.Button(root, text='返回', command=lambda: getLoginMess(threadQueue,root))
    b2.place(x=180, y=110)
    root.mainloop()
def getLoginMess(threadQueue:Queue,root:tk.Tk=None) -> None:
    if(root!=None):
        root.destroy()
    username = str()
    root = tk.Tk()
    root.overrideredirect(True) 
    scw=root.winfo_screenwidth()
    sch=root.winfo_screenheight()
    height=150
    width=300
    rsize =f'{width}x{height}+{round((scw-width)/2)}+{(round((sch-height)/2))}'
    root.geometry(rsize)
    root.resizable(width=False,height=False)
    lambdaUsername = tk.Label(root,text='账号:',font=('宋体',14))
    lambdaUsername.place(x=20,y=20)
    lambdapassword = tk.Label(root,text='密码：',font=('宋体',14))
    lambdapassword.place(x=20,y=60)
    username=tk.StringVar(root,value='')
    password=tk.StringVar(root,value='')
    e_name=tk.Entry(root,width=20,textvariable=username)
    e_name.place(x=100,y=20)
    e_pwd=tk.Entry(root,width=20,show='*',textvariable=password)
    e_pwd.place(x=100,y=60)
    b1=tk.Button(root,text='登录',command=lambda: logic(e_name.get(),e_pwd.get(),root,threadQueue))
    b1.place(x=100,y=100)
    b2=tk.Button(root,text='注册',command=lambda: register(root,threadQueue))
    b2.place(x=180,y=100)
    root.mainloop()
    # threadQueue.put(("logined",username))
        