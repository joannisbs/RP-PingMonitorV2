# -*- coding: utf-8 -*-

from VariaveisGlobais import * 
from Tkinter import *
from TelaRelogio1 import *
from TelaRelogio2 import *
from TelaResumo import *
import tkMessageBox as messagebox

import LeBanco



def main():

	LeBanco.leBanco()
	Telas.root = Tk()

	Iniciooo(Telas.root)


	Telas.root.wm_withdraw()


#Relo1.mainloop()
	Telas.root.mainloop()



def on_closing():
	if messagebox.askokcancel("Quit","Quer realmente sair?"):
		#Controle.Stop = True
		#Telas.root.deiconify()


		#time.sleep(5)


		#while Flag.quit is False:
		#	pass
		Telas.root.destroy()


class Iniciooo:

	def __init__(self,root):
		lable1 = Label(Telas.root, text = "LOAGING...")
		lable1.grid(row=0,pady=5,padx=20)

		Relo1 = Toplevel(master=None)
		Relo1.geometry('1950x950')
		Relo1.update()
		Relo1.grid_rowconfigure(0,weight=1)
		Relo1.grid_columnconfigure(0,weight=1)
		Relo1.resizable(True,True)
		Relo1.configure(background="black")		
		#Relo1.geometry(Relo1.geometry())
		Relo1.title("Monitor Relogios 1")
		Relo1.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Tela1 = TelaRelogio1(Relo1)


		Relo2 = Toplevel(master=None)
		Relo2.geometry('1950x950')
		Relo2.update()
		Relo2.grid_rowconfigure(0,weight=1)
		Relo2.grid_columnconfigure(0,weight=1)
		Relo2.resizable(True,True)
		Relo2.configure(background="black")		
		#Relo2.geometry(Relo2.geometry())
		Relo2.title("Monitor Relogios 2")
		Relo2.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Tela2 = TelaRelogio2(Relo2)

		
		
		Monitor = Toplevel(master=None)
		Monitor.title("Monitoramento e Controle")
		Monitor.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Monitor = TelaMonitor(Monitor)
	
		lable1 = Label(Telas.root, text = "ENCERRANDO")
		lable1.grid(row=0,pady=5,padx=20)


















main()