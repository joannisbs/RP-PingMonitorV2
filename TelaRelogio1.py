# -*- coding: utf-8 -*-

from VariaveisGlobais import * 
from Tkinter import *

class TelaRelogio1(object):


	def __init__(self,root):


		#Inicializando as listas com conteúdo vazio.
		self.ContainerColuna 	= []
		self.Container_Empresa 	= []
		self.MsgName 			= []
		self.botaoAtencao 		= []
		self.botaoContage 		= []
		self.MsgHora 			= []
		self.botaoModulo		= []


		#Cria Container Principal que abrigara os demais containers. 
		self.Create_container 			(root)

		#Cria os containers das empresas. 
		self.Create_container_empresas	(root)

		#Cria O cabeçalho das empresas,
		#Como labels Atention button and time label 
		self.Create_Labels_And_Commun_Mensages(root)


		self.Create_Relogios(root)


	def Create_container(self,root):

		self.ContainerRelogios = Frame 	(root,bg="black")

		self.ContainerRelogios.grid   	(row=0, 
										column= 0,
										sticky = N + S + E + W)
		

	def Create_container_empresas(self,root):

		#Cria os containers de cada empresa.
		for coluna in range (10):

			#Inicializção de variaveis, 
			#criando a lista com os espaços necessários

			self.ContainerColuna.append(coluna)

			
			self.ContainerColuna[coluna] = Frame (self.ContainerRelogios,
																bg="black")

			self.ContainerColuna[coluna].grid	(
												row=0,
												column=coluna,
												pady=5, 
												padx=2, 
												columnspan=1, 
												sticky="N")

	def Create_Labels_And_Commun_Mensages(self,root):

		Quant_Empresas = len(Var.Lista1.empresas)
		for index in range (Quant_Empresas):

			self.botaoContage.append 		(" ")
			self.Container_Empresa.append 	(" ")
			self.botaoAtencao.append 		(" ")
			self.MsgHora.append 			(" ")
			self.MsgName.append 			(" ")
			self.Container_Empresa.append 	(" ")


		Quant_Empresas = len(Var.Lista1.empresas)
		for index in range (Quant_Empresas):

			Id_empresa			= int(Var.Lista1.empresas[index][0])

			#Checa se tem Erro de Index Pai, 
			if Id_empresa != index : 
				print "ERRO DE INDEX \n ERROR: 0001"
				Telas.root.destroy()


			Nome_empresa	 	= Var.Lista1.empresas[index][1] 
			Coluna_container    = int(Var.Lista1.empresas[index][2])
			Linha_container   	= int(Var.Lista1.empresas[index][3])


		


			self.Container_Empresa[Id_empresa]	=	Frame(
										self.ContainerColuna[Coluna_container],
										bg="black")


			self.Container_Empresa[Id_empresa].grid(row=Linha_container,
													column=0,
													pady=0, 
													padx=2, 
													columnspan=1, 
													sticky="N")






			
			self.MsgName[Id_empresa]= Label (
											self.Container_Empresa[Id_empresa],
											text = Nome_empresa,
											font="arialblack 12 bold",
											bg="black",
											fg="white")

			self.MsgName[Id_empresa].grid 	(row=0,
											column=0,
											sticky = "N")


			








			self.botaoAtencao[Id_empresa]  = Button( 
											self.Container_Empresa[Id_empresa],
											font="arial 11 bold" , 
											highlightbackground="black",
											activebackground="black",
											activeforeground="white",
											text='A',
											bg="green3",
											width=2,
											height=1)

			self.botaoAtencao[Id_empresa].grid  (row=0,
												column=1,
												sticky = "N")









			
			self.botaoContage[Id_empresa] = Button (
											self.Container_Empresa[Id_empresa],
											text = "00/00",
											font="arial 11 bold",
											bg="black",
											fg="white",
											highlightbackground="black",
											activebackground="black",
											activeforeground="white",
											width=2,
											bd=0,
											height = 1)

			
			self.botaoContage[Id_empresa].grid 		(row=1,
													column=1,
													pady=1,
													sticky = "N")






			
			self.MsgHora = Label 	(self.Container_Empresa[Id_empresa],
									text = "00:00",
									font="arial 11",
									bg="black",
									fg="white")
																			
			self.MsgHora.grid 		(row=1,
									column=0,
									pady=3.5, 
									sticky = "N")

			


	def Create_Relogios(self,root):
		self.botaoModulo 	= []
		self.botaoRelogio 	= []
		Var.Lista1.Cor 		= []
		Var.Lista1.ON		= []
		Var.Lista1.Total	= []

		Quant_Empresas = len(Var.Lista1.empresas)
		for indexempresas in range (Quant_Empresas):
			Var.Lista1.ON.append(0)
			botaorow = []
			botaoRrow = []
			corrow=[]
			Var.Lista1.Total.append(len(Var.Lista1.relogios[indexempresas]))
			for indexrelogios in range (len(Var.Lista1.relogios[indexempresas])):
				Id_emp = int(Var.Lista1.relogios[indexempresas][indexrelogios][0])

				Nome_Relogio	    = Var.Lista1.relogios[indexempresas][indexrelogios][2]
				
				button= Button(
									self.Container_Empresa[Id_emp],
									font="arial 11 bold" ,  
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text=Nome_Relogio,
									width = 12,
									height = 1,
									bg = "yellow")

				button.grid       (row=indexrelogios+2, 
														column=0, sticky = "N")

				
				buttonR= Button(
									self.Container_Empresa[Id_emp],
									font="arial 11 bold" ,  
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text="R",
									width = 2,
									height = 1,
									bg = "yellow")

				buttonR.grid       (row=indexrelogios+2, 
														column=1, sticky = "N")

				

								
				corrow.append(["yellow","yellow"])
				botaorow.append(button)
				botaoRrow.append(buttonR)

			self.botaoModulo.append(botaorow)
			self.botaoRelogio.append(botaoRrow)
			Var.Lista1.Cor.append(corrow)


	def update(self,empresa,relogio):

		self.botaoModulo[empresa][relogio].configure(bg= Var.Lista1.Cor[empresa][relogio][0])
		self.botaoRelogio[empresa][relogio].configure(bg= Var.Lista1.Cor[empresa][relogio][1])


	def updateContage(self,empresa):

		self.botaoContage[empresa].configure(text=
								(str(Var.Lista1.ON[empresa]) + "/" +  
									str(Var.Lista1.Total[empresa])))