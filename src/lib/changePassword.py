import tkinter as tk
def update():
    return True
root = tk.Tk()
root.title('修改密码')
scw=root.winfo_screenwidth()
sch=root.winfo_screenheight()
height=150
width=300
rsize =f'{width}x{height}+{round((scw-width)/2)}+{(round((sch-height)/2))}'
root.geometry(rsize)
root.resizable(width=False,height=False)
lambdaUsername = tk.Label(root,text='旧密码:',font=('宋体',14))
lambdaUsername.place(x=20,y=20)
lambdapassword = tk.Label(root,text='新密码：',font=('宋体',14))
lambdapassword.place(x=20,y=60)
username=tk.StringVar(root,value='')
password=tk.StringVar(root,value='')
e_name=tk.Entry(root,width=20,textvariable=username)
e_name.place(x=100,y=20)
e_pwd=tk.Entry(root,width=20,show='*',textvariable=password)
e_pwd.place(x=100,y=60)
b1=tk.Button(root,text='提交',command=update)
b1.place(x=150,y=100)
root.mainloop()