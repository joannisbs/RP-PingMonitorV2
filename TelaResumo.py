# -*- coding: utf-8 -*-

from Tkinter import *


#from Thread import *
from VariaveisGlobais import * 
from TestFuncions import *


class TelaMonitor(object):

	def __init__(self,root):

		self.Create_containers(root)
		self.Create_daods()




	def Create_daods(self):
		self.msgStaus = Label (self.ContainerStatus,text = "Servico")
		self.msgStaus["height"] = 1
		self.msgStaus.grid(row=0,column=0)


		self.botaoStatus                    = Button(self.ContainerStatus)
		self.botaoStatus     ["text"]       = Controle.StatusWord
		self.botaoStatus     ["background"] = Controle.Status
		self.botaoStatus     ["height"]     = 1
		self.botaoStatus     ["width"]      = 15
		self.botaoStatus.bind("<Button-1>",self.Inicia)
		self.botaoStatus.grid(row=0,column=1)



		self.msgInformativaON = Label (self.ContainerStatus,text = "On-Line : ")
		self.msgInformativaON["height"] = 1
		self.msgInformativaON.grid(row=0,column=2)

		self.msgStatusON = Label (self.ContainerStatus,text =str(Controle.TotalON))
		self.msgStatusON["height"] = 1
		self.msgStatusON.grid(row=0,column=3)

		self.msgInformativaTotal = Label (self.ContainerStatus,text = "Total : ")
		self.msgInformativaTotal["height"] = 1
		self.msgInformativaTotal.grid(row=0,column=4)

		self.msgStatusTotal = Label (self.ContainerStatus,text = str(Controle.TotalRelogios))
		self.msgStatusTotal["height"] = 1
		self.msgStatusTotal.grid(row=0,column=5)

	def Create_containers(self,root):


		self.ContainerStatus              = Frame (root)
		self.ContainerStatus.grid                 (row=0, sticky = "N")



	def update(self):


		self.msgStatusON.configure										(text=str(Controle.TotalON))
		self.msgStatusTotal.configure									(text=str(Controle.TotalRelogios))


	def IniciaThreadTela1(self):
			
		#ThreadloopBuilding().start()
		#ThreadloopCasaCristo().start()
		#ThreadloopBestInClass().start()
		#ThreadloopIsoRadio().start()
		#ThreadloopLaser().start()
		#ThreadloopGravex().start()
		#ThreadloopGrupoNk().start()
		#hreadloopLotten().start()
		#ThreadloopElRio().start()
		#ThreadloopSBCP().start()
		#ThreadloopPredman().start()
		#ThreadloopOlimpark().start()
		CriaTreads()

	def Inicia(self,event):
		if self.botaoStatus["background"]=="red":
			self.botaoStatus["background"] = "green"

			self.botaoStatus["text"] = "Rodando"
			Controle.StatusWord = "Rodando"
			Controle.Status = "green"
			Controle.Stop = False
			#loopthread.doemon = True
			self.IniciaThreadTela1()



		else:
			self.botaoStatus["text"] = "Parado"
			self.botaoStatus["background"] = "red"
			Controle.StatusWord = "Parado"
			Controle.Status = "red"
			Controle.Stop = True


