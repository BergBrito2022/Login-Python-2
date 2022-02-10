#importa bibliotecas
from cProfile import label
from cgitb import text
from email.mime import image
import site
from tkinter import *
from tkinter import messagebox
from turtle import left
from tkinter import ttk

#Criar janela
jan = Tk ()
jan.title ('DP systems - acess painel')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width=False, height=False)

# ----- Logo Carregar -----

logo = PhotoImage(file='icones/logo.png')

# ----- widgets -----
LeftFram = Frame(jan, width='200', height='300', bg='MIDNIGHTBLUE', relief='raise')
LeftFram.pack(side=LEFT)

RightFram = Frame(jan, width='395', height='300', bg='MIDNIGHTBLUE', relief='raise')
RightFram.pack(side=RIGHT)

LogoLabel = Label(LeftFram, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place (x=50, y=100)

#----- Criando User ------

UserLabel = Label(RightFram, text='Username', font=('century gothic', 20), bg='MIDNIGHTBLUE',fg='white')
UserLabel.place(x=30, y=89)

UserEntry = ttk.Entry(RightFram, width=30)
UserEntry.place(x=180, y=100)
# ---- Senha ----
PassLabel = Label(RightFram, text='Password', font=('century gothic', 20), bg='MIDNIGHTBLUE',fg='white')
PassLabel.place(x=30, y=140)

PassEntry = ttk.Entry(RightFram, width=30)
PassEntry.place(x=180, y=150)

jan.mainloop()