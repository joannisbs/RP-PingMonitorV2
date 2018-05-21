# -*- coding: utf-8 -*-

from VariaveisGlobais import * 
from Tkinter import *


class Scream1:

	def __init__(self,root):

		self.Init_List()
		self.Create_container_geral(root)
		self.Create_container_colunas(root)
		self.Create_emps()
		self.Create_reps()


	def Init_List(self):
		self.Container_Empresa	= []
		self.MsgName 			= []
		self.botaoAtencao 		= []
		self.botaoContage		= []
		self.MsgHora 			= []
		self.ContainerColuna 	= []
		self.Container_Empresa 	= []
		self.ButtonList			= []
		self.ButtonListR		= []
		self.listrow 			= []



	def Create_container_geral(self,root):


		self.Containerpai = Frame 	(root,bg="black")

		self.Containerpai.grid   	(row=0, 
										column= 0,
										sticky = N + S + E + W)


		self.ContainerRelogios = Frame 	(self.Containerpai,bg="black")

		self.ContainerRelogios.grid   	(row=0, 
										column= 0,
										padx=3,
										pady=5,
										sticky = N + S + E + W)



	def Create_container_colunas(self,root):

		#Cria os containers de cada empresa.
		
		for coluna in range (11):

			#Inicializção de variaveis, 
			#criando a lista com os espaços necessários

			self.ContainerColuna.append(coluna)

			
			self.ContainerColuna[coluna] = Frame (self.ContainerRelogios,
																bg="black")

			self.ContainerColuna[coluna].grid	(
												row=0,
												column=coluna+1,
												pady=5, 
												padx=1, 
												columnspan=1, 
												sticky="N")




	def Create_emps(self):

		id_emp_scream1 = 0
		for item in  range (len(Var.Lista.Empresas)):
			if Var.Lista.Empresas[item][2] == 1:
				Var.Lista.Empresas[item][8] = id_emp_scream1
				self.Create_emp(item)
				id_emp_scream1 = id_emp_scream1 + 1
 



	def Create_emp(self,id_emp):
		
		self.Container_Empresa.append 	("")
		self.MsgName.append				("")
		self.botaoAtencao.append 		("")
		self.botaoContage.append 		("")
		self.MsgHora.append 			("")
		self.listrow.append 			(0)


		name_emp 			= Var.Lista.Empresas[id_emp][1]
		Coluna_container	= Var.Lista.Empresas[id_emp][3]
		Linha_container		= Var.Lista.Empresas[id_emp][4]
		id_emp_scream 		= Var.Lista.Empresas[id_emp][8]


		


		self.Container_Empresa[id_emp_scream]	= Frame(
									self.ContainerColuna[Coluna_container],
									bg="black")


		self.Container_Empresa[id_emp_scream].grid(
									row=Linha_container,
									column=0,
									pady=0, 
									padx=2, 
									columnspan=1, 
									sticky="N")



		self.MsgName[id_emp_scream]				= Label (
									self.Container_Empresa[id_emp_scream],
									text = name_emp,
									font="arialblack 12 bold",
									bg="black",
									fg="white")

		self.MsgName[id_emp_scream].grid(
									row=0,
									column=0,
									sticky = "N")


			


		self.botaoAtencao[id_emp_scream]  		= Button( 
									self.Container_Empresa[id_emp_scream],
									font="arial 11 bold" , 
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text='A',
									bg="green3",
									width=2,
									height=1)

		self.botaoAtencao[id_emp_scream].grid (
									row=0,
									column=1,
									sticky = "N")





		
		self.botaoContage[id_emp_scream] 		= Button (
									self.Container_Empresa[id_emp_scream],
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

			
		self.botaoContage[id_emp_scream].grid (
									row=1,
									column=1,
									pady=1,
									sticky = "N")






			
		self.MsgHora[id_emp_scream] 				= Label (
									self.Container_Empresa[id_emp_scream],
									text = "Hora 00:00",
									font="arial 11 bold",
									bg="black",
									fg="white")
																			
		self.MsgHora[id_emp_scream].grid (
									row=1,
									column=0,
									pady=3.5, 
									sticky = "N")




	def Create_reps(self):

		id_rep = 0
		for item in  range (len(Var.Lista.Relogios)):
			id_emp 	= Var.Lista.Relogios[item][1]
			

			if Var.Lista.Empresas[id_emp-1][2] == 1:
				Var.Lista.Relogios[item][9] = id_rep
				self.Create_rep(item)
				
				id_rep = id_rep + 1

		
		for item in  range (len(Var.Lista.Empresas)):
			if Var.Lista.Empresas[item][2] == 1:
				idd = Var.Lista.Empresas[item][8]
				Var.Lista.Empresas[item][10] = self.listrow[idd]




	def Create_rep(self,id_rep):


		self.ButtonList.append 		("")
		self.ButtonListR.append 	("")
		
		id_emp 				= int(Var.Lista.Relogios[id_rep][1])-1
		name_rep			= Var.Lista.Relogios[id_rep][2]
		coontainer_emp		= Var.Lista.Empresas[id_emp][8]
		
		buton_id			= Var.Lista.Relogios[id_rep][9]



		self.ButtonList[buton_id] = Button(
									self.Container_Empresa[coontainer_emp],
									font="arial 11 bold" ,  
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text=name_rep,
									width = 12,
									height = 1,
									bg = "white")

		self.ButtonList[buton_id].grid       (row=self.listrow[coontainer_emp]+2, 
														column=0, sticky = "N")

				
		self.ButtonListR[buton_id]= Button(
									self.Container_Empresa[coontainer_emp],
									font="arial 11 bold" ,  
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text="R",
									width = 2,
									height = 1,
									bg = "white")

		self.ButtonListR[buton_id].grid       (
									row=self.listrow[coontainer_emp]+2, 
								 	column=1, 
								 	sticky = "N")



		self.listrow[coontainer_emp] = self.listrow[coontainer_emp] + 1



	def update(self,index_rep):

		Id_scream 	= Var.Lista.Relogios[index_rep][9]
		Case_color	= Var.Lista.Relogios[index_rep][10]

		if Case_color == 1:
			self.ButtonList[Id_scream].config 	(bg = "red",fg = "white")
			self.ButtonListR[Id_scream].config 	(bg = "red",fg = "white")
		if Case_color == 2:
			self.ButtonList[Id_scream].config 	(bg = "green3",fg = "black")
			self.ButtonListR[Id_scream].config 	(bg = "DarkOrange1",fg = "black")
		if Case_color == 3:
			self.ButtonList[Id_scream].config 	(bg = "green3",fg = "black")
			self.ButtonListR[Id_scream].config 	(bg = "green3",fg = "black")
		if Case_color == 4:
			self.ButtonList[Id_scream].config 	(bg = "cyan",fg = "black")
			










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






			
			self.MsgHora[Id_empresa] = Label 	(self.Container_Empresa[Id_empresa],
									text = "Hora 00:00",
									font="arial 11 bold",
									bg="black",
									fg="white")
																			
			self.MsgHora[Id_empresa].grid 		(row=1,
									column=0,
									pady=3.5, 
									sticky = "N")

			


	def Create_Relogios(self,root):
		self.botaoModulo 	= []
		self.botaoRelogio 	= []
		Var.Lista1.Cor 		= []
		Var.Lista1.ON		= []
		Var.Lista1.Total	= []
		Var.Lista1.Hora 	= []
		Var.Lista1.Atencao 	= []

		Quant_Empresas = len(Var.Lista1.empresas)
		for indexempresas in range (Quant_Empresas):
			Var.Lista1.ON.append(0)
			Var.Lista1.Atencao.append("green3")
			Var.Lista1.Hora.append('')
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

				

								
				corrow.append(["yellow","yellow","green3"])
				botaorow.append(button)
				botaoRrow.append(buttonR)

			self.botaoModulo.append(botaorow)
			self.botaoRelogio.append(botaoRrow)
			Var.Lista1.Cor.append(corrow)


	def updateasa(self,empresa,relogio):

		self.botaoModulo[empresa][relogio].configure(bg= Var.Lista1.Cor[empresa][relogio][0])
		self.botaoRelogio[empresa][relogio].configure(bg= Var.Lista1.Cor[empresa][relogio][1])
		#self.botaoAtencao[empresa].configure(bg= Var.Lista1.Atencao[empresa])

	def updateContage(self,empresa):

		self.botaoContage[empresa].configure(text=
								(str(Var.Lista1.ON[empresa]) + "/" +  
									str(Var.Lista1.Total[empresa])))
		self.botaoAtencao[empresa].configure(bg= Var.Lista1.Atencao[empresa])


	def updateHora(self,empresa):
		hora = "Hora: " + Var.Lista1.Hora[empresa]
		self.MsgHora[empresa].configure(text=hora)