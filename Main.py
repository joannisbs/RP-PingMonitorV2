# -*- coding: utf-8 -*-
# instal matplotlib
# instal mysql.connector







from VariaveisGlobais import * 
from Tkinter import *
from TelaRelogio1 import Scream1
from TelaRelogio2 import Scream2
from TelaResumo import Monitor
import time
import tkMessageBox as messagebox
from TestFuncions import Servico

from LeBanco import Mysqldb



telas = 0
def main():


	
	db = Mysqldb()
	db.connect()
	db.CarregarEmpresas()
	db.CarregarRelogios()
	db.close()

	#LeBanco.leBanco()
	Telas.root = Tk()

	ScremInit(Telas.root)


	Telas.root.wm_withdraw()


#Relo1.mainloop()
	Telas.root.mainloop()




 


def on_closing():
	if messagebox.askokcancel("Quit","Quer realmente sair?"):
		serv = Servico()
		serv.Stop()
		Telas.GUI_Monitor.close()
		print "closing"
		try:
			Controle.db.close()
		
		except:
			pass
			
		time.sleep(2)
		Telas.root.quit()
		for x in range (5):
			print x
			time.sleep(1)
		
		time.sleep(1)
		Telas.root.destroy()


class ScremInit:
	def __init__(self,root):
		lable1 = Label(Telas.root, text = "REAL PONTO - LOADING...")
		lable1.grid(row=0,pady=5,padx=20)
		time.sleep(1)



		self.Inicia_Scream1()
		self.Inicia_Scream2()
		self.Inicia_Monitor()
		time.sleep(2)
		serv = Servico()
		serv.Start()









	def Inicia_Scream1(self):

		self.state = False
		self.Relo1 = Toplevel(master=None)
		self.Relo1.geometry('1950x950')
		self.Relo1.bind('<F11>',self.togglefull1)
		self.Relo1.update()
		self.Relo1.grid_rowconfigure(0,weight=1)
		self.Relo1.grid_columnconfigure(0,weight=1)
		self.Relo1.resizable(True,True)
		self.Relo1.configure(background="black")		
		#Relo1.geometry(Relo1.geometry())
		self.Relo1.title("Monitor Relogios 1")
		self.Relo1.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Tela1 = Scream1(self.Relo1)

	def Inicia_Scream2(self):

		self.Relo2 = Toplevel(master=None)
		self.Relo2.geometry('1950x950')
		self.state2 = False
		self.Relo2.bind('<F11>',self.togglefull2)
		self.Relo2.update()
		self.Relo2.grid_rowconfigure(0,weight=1)
		self.Relo2.grid_columnconfigure(0,weight=1)
		self.Relo2.resizable(True,True)
		self.Relo2.configure(background="black")		
		#self.Relo2.geometry(self.Relo2.geometry())
		self.Relo2.title("Monitor Relogios 2")
		self.Relo2.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Tela2 = Scream2(self.Relo2)


	def Inicia_Monitor(self):


		self.telaMonitor = Toplevel(master=None)
		self.telaMonitor.geometry('1950x950')
		self.state3 = False
		self.telaMonitor.bind('<F11>',self.togglefull3)
		self.telaMonitor.update()
		#self.telaMonitor.grid_rowconfigure(0,weight=1)
		#self.telaMonitor.grid_columnconfigure(0,weight=1)
		self.telaMonitor.resizable(True,True)
		self.telaMonitor.configure(background="black")
		self.telaMonitor.title("Monitoramento e Controle")
		self.telaMonitor.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Monitor = Monitor(self.telaMonitor)
	

	def togglefull1(self,event):
		self.state = not self.state
		self.Relo1.attributes("-fullscreen",self.state)

	def togglefull2(self,event):
		self.state2 = not self.state2
		self.Relo2.attributes("-fullscreen",self.state2)


	def togglefull3(self,event):
		self.state3 = not self.state3
		self.telaMonitor.attributes("-fullscreen",self.state3)


class Iniciooo:

	def __init__(self,root):
		lable1 = Label(Telas.root, text = "LOAGING...")
		lable1.grid(row=0,pady=5,padx=20)
		self.state = False
		self.Relo1 = Toplevel(master=None)
		self.Relo1.geometry('1950x950')
		self.Relo1.bind('<F11>',self.togglefull1)
		self.Relo1.update()
		self.Relo1.grid_rowconfigure(0,weight=1)
		self.Relo1.grid_columnconfigure(0,weight=1)
		self.Relo1.resizable(True,True)
		self.Relo1.configure(background="black")		
		#Relo1.geometry(Relo1.geometry())
		self.Relo1.title("Monitor Relogios 1")
		self.Relo1.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Tela1 = TelaRelogio1(self.Relo1)


		self.Relo2 = Toplevel(master=None)
		self.Relo2.geometry('1950x950')
		self.state2 = False
		self.Relo2.bind('<F11>',self.togglefull2)
		self.Relo2.update()
		self.Relo2.grid_rowconfigure(0,weight=1)
		self.Relo2.grid_columnconfigure(0,weight=1)
		self.Relo2.resizable(True,True)
		self.Relo2.configure(background="black")		
		#self.Relo2.geometry(self.Relo2.geometry())
		self.Relo2.title("Monitor Relogios 2")
		self.Relo2.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Tela2 = TelaRelogio2(self.Relo2)

		
		
		Monitor = Toplevel(master=None)
		Monitor.title("Monitoramento e Controle")
		Monitor.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Monitor = TelaMonitor(Monitor)
	
		lable1 = Label(Telas.root, text = "ENCERRANDO")
		lable1.grid(row=0,pady=5,padx=20)


		
	def togglefull1(self,event):
		self.state = not self.state
		self.Relo1.attributes("-fullscreen",self.state)

	def togglefull2(self,event):
		self.state2 = not self.state2
		self.Relo2.attributes("-fullscreen",self.state2)













main()