import tkinter as tk
def update():
    return True
root = tk.Tk()
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
b1=tk.Button(root,text='提交',command=update)
b1.place(x=200,y=140)
root.mainloop()