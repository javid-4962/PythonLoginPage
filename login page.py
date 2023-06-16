from tkinter import *
from tkinter import messagebox
import ast 

root = Tk()
root.title('LOGIN')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username =user.get()
    password=code.get()

    file = open('datasheet.json','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())

    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='Hello You are in App console!',bg='#fff',font=('Cambria',40,'bold')).pack(expand=True)
        
        screen.mainloop()
    else:
        messagebox.showerror('Invalid',"invalid username or password")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def signup_command():
    window = Toplevel(root)
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
    
    def signup():
        username=user.get()
        password=code.get()
        cpassword=conform.get()
    
        if password == cpassword:
            try:
                file=open("datasheet.json",'r+')
                d=file.read()
                r=ast.literal_eval(d)
    
                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()
                file=open('datasheet.json','w')
                w=file.write(str(r))
    
                messagebox.showinfo('Signup','Sucessfully sign up')
            except:
                file=open('datasheet.json','w')
                pp = str({"Usrname":"password"})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid','Both Password should match')
    
    
    def sign():
        window.destroy()
    
    
    img = PhotoImage(file='signupbg2.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=130)
    
    
    frame=Frame(window,width=350,height=390,bg='white')
    frame.place(x=400,y=50)
    
    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    
    
    #----------------------------------------------------------------------------   ---
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='': 
            user.insert(0,'User name')
    
    user = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'User name')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    
    Frame(frame,height=2,width=295,bg='black').place(x=25,y=107)
    #----------------------------------------------------------------------------   ----
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        pas=code.get()
        if pas=='': 
            code.insert(0,'Password')
    
    code = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    
    Frame(frame,height=2,width=295,bg='black').place(x=25,y=177)
    #----------------------------------------------------------------------------   ----
    def on_enter(e):
        conform.delete(0,'end')
    def on_leave(e):
        cpas=conform.get()
        if cpas=='': 
            conform.insert(0,'Conform Password')
    
    conform = Entry(frame,width=35,fg='black',border=0,bg='white',font= ('Microsoft YaHei UI Light',11))
    conform.place(x=30,y=220)
    conform.insert(0,'Conform Password')
    conform.bind('<FocusIn>',on_enter)
    conform.bind('<FocusOut>',on_leave)
    
    Frame(frame,height=2,width=295,bg='black').place(x=25,y=247)
    #----------------------------------------------------------------------------   ----
    Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,   command=signup).place(x= 35,y= 280)
    label=Label(frame,text='I have an account',fg='black',bg='white',font=  ('Microsoft YaHei UI Light',9))
    label.place(x=90,y=340)
    
    signin = Button(frame,width=6,text='Sign In',border=0,bg='white',   cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)
    
    window.mainloop()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

img = PhotoImage(file='loginbg2.png')
Label(root, image= img, bg ='white',height=300,width=300).place(x=50, y=50)

frame = Frame(root, width=300, height = 300, bg="white")
frame.place(x=400,y=70)

heading = Label(frame, text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#-----------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='': 
        user.insert(0,'User name')

user = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'User name')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,height=2,width=295,bg='black').place(x=25,y=107)
#-----------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    pas=code.get()
    if pas=='':
        code.insert(0,'Password')

code = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,height=2,width=295,bg='black').place(x=25,y=177)
#-----------------------------------------------------------------------------------------------

Button(frame,width=39,pady=10,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin,cursor='hand2').place(x=30,y=200)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)


sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)



root.mainloop()
