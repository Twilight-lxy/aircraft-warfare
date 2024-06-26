import tkinter as tk

from src.classes.User import User
def update():
    return True
def back():
    return True
def changePassword(user:User):
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
    lambdapassword.place(x=15,y=60)
    repassword = tk.Label(root,text='再次输入新密码：',font=('宋体',16))
    repassword.place(x=0,y=100)
    username=tk.StringVar(root,value='')
    password=tk.StringVar(root,value='')
    repassword=tk.StringVar(root,value='')
    e_name=tk.Entry(root,width=25,textvariable=username)
    e_name.place(x=120,y=25)
    e_pwd=tk.Entry(root,width=25,show='*',textvariable=password)
    e_pwd.place(x=120,y=65)
    repwd=tk.Entry(root,width=25,show='*',textvariable=password)
    repwd.place(x=160,y=105)
    b2=tk.Button(root,text='返回',command=back)
    b2.place(x=120,y=145)
    b1=tk.Button(root,text='提交',command=update)
    b1.place(x=220,y=145)
    root.mainloop()