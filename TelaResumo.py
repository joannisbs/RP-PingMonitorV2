# -*- coding: utf-8 -*-

from Tkinter import *


#from Thread import *
from VariaveisGlobais import * 
from TestFuncions import *


class TelaMonitor(object):

	def __init__(self,root):

		self.Create_containers(root)
		self.Create_daods()
		self.Create_ButoesEmpresas()
		self.Create_ButoesEmpresas2()



	def Create_ButoesEmpresas(self):
		self.MsgName= Label (
											self.ContaineEmpresas1,
											text = "Tela 1 :",
											font="arialblack 12 bold",
											bg="black",
											fg="white")

		self.MsgName.grid 	(row=0,
											column=0,columnspan=4,
											sticky = "N")


		self.botaoAtencao =[]
		self.MsgTotal =[]
		self.MsgNames =[]
		self.MsgON =[]


		Quant_Empresas = len(Var.Lista1.empresas)
		for index in range (Quant_Empresas):

			self.botaoAtencao.append 		(" ")
			self.MsgTotal.append 			(" ")
			self.MsgNames.append 			(" ")
			self.MsgON.append 	(" ")

			Id_empresa			= int(Var.Lista1.empresas[index][0])


			Nome_empresa	 	= Var.Lista1.empresas[index][1] 
	




			
			self.MsgNames[Id_empresa]= Label (
											self.ContaineEmpresas1,
											text = Nome_empresa,
											font="arialblack 12 bold",
											bg="black",
											fg="white")

			self.MsgNames[Id_empresa].grid 	(row=index+1,
											column=0,
											sticky = "N")


			








			self.botaoAtencao[Id_empresa]  = Button( 
											self.ContaineEmpresas1,
											font="arial 11 bold" , 
											highlightbackground="black",
											activebackground="black",
											activeforeground="white",
											text='A',
											bg="green3",
											width=2,
											height=1)

			self.botaoAtencao[Id_empresa].grid  (row=index+1,
												column=1,
												sticky = "N")









			
			self.MsgON[Id_empresa] = Label 	(
											self.ContaineEmpresas1,
									text = "ON: X",
									font="arial 11 bold",
									bg="black",
									fg="white")
																			
			self.MsgON[Id_empresa].grid 		(row=index+1,
									column=2,
									pady=3.5, 
									sticky = "N")



			
			self.MsgTotal[Id_empresa] = Label 	(
											self.ContaineEmpresas1,
									text = "Total: ",
									font="arial 11 bold",
									bg="black",
									fg="white")
																			
			self.MsgTotal[Id_empresa].grid 		(row=index+1,
									column=3,
									pady=3.5, 
									sticky = "N")



	def Create_ButoesEmpresas2(self):
		self.MsgName2= Label (
											self.ContaineEmpresas2,
											text = "Tela 2 :",
											font="arialblack 12 bold",
											bg="black",
											fg="white")

		self.MsgName2.grid 	(row=0,
											column=0,columnspan=4,
											sticky = "N")


		self.botaoAtencao2 =[]
		self.MsgTotal2 =[]
		self.MsgNames2 =[]
		self.MsgON2 =[]


		Quant_Empresas = len(Var.Lista2.empresas)
		for index in range (Quant_Empresas):

			self.botaoAtencao2.append 		(" ")
			self.MsgTotal2.append 			(" ")
			self.MsgNames2.append 			(" ")
			self.MsgON2.append 	(" ")

			Id_empresa			= int(Var.Lista2.empresas[index][0])


			Nome_empresa	 	= Var.Lista2.empresas[index][1] 
	




			
			self.MsgNames2[Id_empresa]= Label (
											self.ContaineEmpresas2,
											text = Nome_empresa,
											font="arialblack 12 bold",
											bg="black",
											fg="white")

			self.MsgNames2[Id_empresa].grid 	(row=index+1,
											column=0,
											sticky = "N")


			








			self.botaoAtencao2[Id_empresa]  = Button( 
											self.ContaineEmpresas2,
											font="arial 11 bold" , 
											highlightbackground="black",
											activebackground="black",
											activeforeground="white",
											text='A',
											bg="green3",
											width=2,
											height=1)

			self.botaoAtencao2[Id_empresa].grid  (row=index+1,
												column=1,
												sticky = "N")









			
			self.MsgON2[Id_empresa] = Label 	(
											self.ContaineEmpresas2,
									text = "ON: X",
									font="arial 11 bold",
									bg="black",
									fg="white")
																			
			self.MsgON2[Id_empresa].grid 		(row=index+1,
									column=2,
									pady=3.5, 
									sticky = "N")



			
			self.MsgTotal2[Id_empresa] = Label 	(
											self.ContaineEmpresas2,
									text = "Total: ",
									font="arial 11 bold",
									bg="black",
									fg="white")
																			
			self.MsgTotal2[Id_empresa].grid 		(row=index+1,
									column=3,
									pady=3.5, 
									sticky = "N")






	def Create_daods(self):
		self.msgStaus = Label (self.ContainerStatus,text = "Servico",
									font="arial 12 bold",
									bg="black",
									fg="white")
		self.msgStaus["height"] = 1
		self.msgStaus.grid(row=0,column=0)


		self.botaoStatus                    = Button(self.ContainerStatus)
		self.botaoStatus     ["text"]       = Controle.StatusWord
		self.botaoStatus     ["background"] = Controle.Status
		self.botaoStatus     ["height"]     = 1
		self.botaoStatus     ["width"]      = 15
		self.botaoStatus.bind("<Button-1>",self.Inicia)
		self.botaoStatus.grid(row=0,column=1)



		self.msgInformativaON = Label (self.ContainerStatus,text = "On-Line : ",
									font="arial 12 bold",
									bg="black",
									fg="white")
		self.msgInformativaON["height"] = 1
		self.msgInformativaON.grid(row=0,column=2)

		self.msgStatusON = Label (self.ContainerStatus,text =str(Controle.TotalON),
									font="arial 12 bold",
									bg="black",
									fg="white")
		self.msgStatusON["height"] = 1
		self.msgStatusON.grid(row=0,column=3)

		self.msgInformativaTotal = Label (self.ContainerStatus,text = "Total : ",
									font="arial 12 bold",
									bg="black",
									fg="white")
		self.msgInformativaTotal["height"] = 1
		self.msgInformativaTotal.grid(row=0,column=4)

		self.msgStatusTotal = Label (self.ContainerStatus,text = str(Controle.TotalRelogios),
									font="arial 12 bold",
									bg="black",
									fg="white")
		self.msgStatusTotal["height"] = 1
		self.msgStatusTotal.grid(row=0,column=5)

	def Create_containers(self,root):


		self.ContainerStatus              = Frame (root,bg="black")
		self.ContainerStatus.grid                 (row=0, sticky = "N")

		self.ContaineParte2				= Frame(root,bg="black")
		self.ContaineParte2.grid                 (row=1, sticky = "N")

		self.ContaineEmpresas1			= Frame(self.ContaineParte2,bg="black")
		self.ContaineEmpresas1.grid                 (row=0, column=0, sticky = "N")

		self.ContaineEmpresas2			= Frame(self.ContaineParte2,bg="black")
		self.ContaineEmpresas2.grid                 (row=0, column=1, sticky = "N")

	def update(self):


		self.msgStatusON.configure										(text=str(Controle.TotalON))
		self.msgStatusTotal.configure									(text=str(Controle.TotalRelogios))


	def IniciaThreadTela1(self):
			
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

	def UpdateContage1(self,empresa):
		self.MsgON[empresa].configure(text="  ON: " +
								str(Var.Lista1.ON[empresa]))

		self.MsgTotal[empresa].configure(text="  Total: "	+					  
									str(Var.Lista1.Total[empresa]))
		
		Controle.TotalON1 = 0
		Controle.TotalON2 = 0
		Controle.TotalON  = 0
		Quant_Empresas = len(Var.Lista1.empresas)
		for index in range (Quant_Empresas):
			Controle.TotalON1 = Controle.TotalON1 + Var.Lista1.ON[index]
		Quant_Empresas = len(Var.Lista2.empresas)
		for index in range (Quant_Empresas):
			Controle.TotalON2 = Controle.TotalON2 + Var.Lista2.ON[index]

		Controle.TotalON = Controle.TotalON1 + Controle.TotalON2
		self.msgStatusON.configure(text=str(Controle.TotalON))
		self.botaoAtencao[empresa].configure(bg= Var.Lista1.Atencao[empresa])

	def UpdateContage2(self,empresa):
		self.MsgON2[empresa].configure(text="  ON: " +
								str(Var.Lista2.ON[empresa]))

		self.MsgTotal2[empresa].configure(text="  Total: "	+					  
									str(Var.Lista2.Total[empresa]))

		Controle.TotalON1 = 0
		Controle.TotalON2 = 0
		Controle.TotalON  = 0
		Quant_Empresas = len(Var.Lista1.empresas)
		for index in range (Quant_Empresas):
			Controle.TotalON1 = Controle.TotalON1 + Var.Lista1.ON[index]
		Quant_Empresas = len(Var.Lista2.empresas)
		for index in range (Quant_Empresas):
			Controle.TotalON2 = Controle.TotalON2 + Var.Lista2.ON[index]

		Controle.TotalON = Controle.TotalON1 + Controle.TotalON2

		self.msgStatusON.configure(text=str(Controle.TotalON))
		self.botaoAtencao2[empresa].configure(bg= Var.Lista2.Atencao[empresa])

