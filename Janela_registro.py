from tkinter import *


def main_screen():
    login_screen = Tk()
    login_screen.geometry("300x250+%d+%d" %
                          ((login_screen.winfo_screenwidth()/2)-150, (login_screen.winfo_screenheight()/2)-125))
    login_screen.title("Login - MoreLife")

    lbl_login_title = Label(text="Login", font=("Arial", 13), width=6, height=2, relief=FLAT)
    lbl_email_ori = Label(text="Email: ")
    ent_email = Entry(font=("Arial", 13))
    lbl_password_ori = Label(text="Senha: ")
    ent_password = Entry(font=("Arial", 13))
    btn_login = Button(text="Login", width=10)
    btn_register = Button(text="Registrar-se", width=10)

    lbl_login_title.place(relx=0.5, y=20, anchor=CENTER)
    lbl_email_ori.place(x=20, y=50)
    ent_email.place(x=65, y=50)
    lbl_password_ori.place(x=20, y=80)
    ent_password.place(x=65, y=80)
    btn_login.place(relx=0.5, y=150, anchor=CENTER)
    btn_register.place(relx=0.5, y=190, anchor=CENTER)

    login_screen.mainloop()


main_screen()
