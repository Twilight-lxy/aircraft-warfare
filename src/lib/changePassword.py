import multiprocessing
import tkinter as tk

from src.lib.DataBaseFunc import userUpdate
from src.classes.User import User
def update(username:str,password:str,repassword:str,root:tk.Tk,queue:multiprocessing.Queue):

    if username==''or password=='':
        tk.messagebox.showinfo(title='信息',message='账号或密码为空！')
        return
    user=User(username,password)
    if(userUpdate(user) and password == repassword):
        tk.messagebox.showinfo(title='信息',message='修改成功！')
        root.destroy()
        queue.put(("close"))
    else:
        tk.messagebox.showinfo(title='错误',message='修改失败！')
    
def changePassword(queue:multiprocessing.Queue):
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    root.title('修改密码')
    scw=root.winfo_screenwidth()
    sch=root.winfo_screenheight()
    height=200
    width=400
    rsize =f'{width}x{height}+{round((scw-width)/2)}+{(round((sch-height)/2))}'
    root.geometry(rsize)
    root.resizable(width=False,height=False)
    lambdaUsername = tk.Label(root,text='新用户名:',font=('宋体',16))
    lambdaUsername.place(x=10,y=20)
    lambdapassword = tk.Label(root,text='新密码：',font=('宋体',16))
    lambdapassword.place(x=15,y=80)
    username=tk.StringVar(root,value='')
    password=tk.StringVar(root,value='')
    e_name=tk.Entry(root,width=25,textvariable=username)
    e_name.place(x=120,y=25)
    e_pwd=tk.Entry(root,width=25,show='*',textvariable=password)
    e_pwd.place(x=120,y=85)
    b1=tk.Button(root,text='提交',command=lambda: update(e_name.get(),e_pwd.get(),root,queue))
    b1.place(x=200,y=140)
    root.mainloop()