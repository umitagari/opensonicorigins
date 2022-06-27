import tkinter
import os
import tkinter as tk
from tkinter import Tk, PhotoImage, Label
from tkinter import *

ventana = tkinter.Tk()
ventana.geometry("1080x680")
ventana.title("Open Sonic Origins")
ventana.resizable(0,0)
imagen = PhotoImage(file = "sonicfondo.png")
background = Label(image = imagen)
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

originsicon = PhotoImage(file = "Sonic_Origins_Logo.png")
iconoorigins = tkinter.Button(ventana, text = "Sonic 1", image=originsicon, borderwidth=10)
iconoorigins.place(x=370, y=47)

label = Label(ventana, text="a masterpiece made by reimu (dj sorrow)#0666")
label.pack(anchor=CENTER)
label.config(fg="white", bg="grey", font=("Verdana",10))


def s1():
	sonic1 = os.system('sonic1.bin')

def s2():
	sonic2 = os.system('sonic2.bin')

def s3():
	sonic3 = os.system('sonic2.bin')

def scd():
	soniccd = os.system('soniccd.iso')

s1btn = PhotoImage(file = "sonic1ico.png")
s2btn = PhotoImage(file = "sonic2ico.png")
s3btn = PhotoImage(file = "sonic3ico.png")
scdbtn = PhotoImage(file = "soniccdico.png")
boton1 = tkinter.Button(ventana, text = "Sonic 1", command = s1, image=s1btn, borderwidth=10)
boton2 = tkinter.Button(ventana, text = "Sonic 2", command = s2, image=s2btn, borderwidth=10)
boton3 = tkinter.Button(ventana, text = "Sonic 3", command = s3, image=s3btn, borderwidth=10)
boton4 = tkinter.Button(ventana, text = "Sonic CD", command = scd, image=scdbtn, borderwidth=10)

boton1.place(x=340, y=500)
boton2.place(x=440, y=500)
boton3.place(x=540, y=500)
boton4.place(x=640, y=500)

ventana.mainloop()