# -*- coding: utf-8 -*-

from VariaveisGlobais import * 
from Tkinter import *
from Popups import PopupRel

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
		self.ButtonListR[buton_id].bind  ("<Button-1>",lambda e: PopupRel(id_rep))

		self.ButtonListR[buton_id].grid       (
									row=self.listrow[coontainer_emp]+2, 
								 	column=1, 
								 	sticky = "N")



		self.listrow[coontainer_emp] = self.listrow[coontainer_emp] + 1

       			







	def update(self,index_rep):

		id_emp 		=  Var.Lista.Relogios[index_rep][1]
		Id_scream 	= Var.Lista.Relogios[index_rep][9]
		Case_color	= Var.Lista.Relogios[index_rep][10]

		if Case_color == 1:
			self.ButtonList[Id_scream].config 	(bg = "red",fg = "white")
			self.ButtonListR[Id_scream].config 	(bg = "red",fg = "white")
			Var.Lista.Relogios[index_rep][7] = False
		if Case_color == 2:
			self.ButtonList[Id_scream].config 	(bg = "green3",fg = "black")
			self.ButtonListR[Id_scream].config 	(bg = "DarkOrange1",fg = "black")
			Var.Lista.Relogios[index_rep][7] = False
		if Case_color == 3:
			self.ButtonList[Id_scream].config 	(bg = "green3",fg = "black")
			self.ButtonListR[Id_scream].config 	(bg = "green3",fg = "black")

			Var.Lista.Relogios[index_rep][7] = True
		if Case_color == 4:
			self.ButtonList[Id_scream].config 	(bg = "cyan",fg = "black")
			
		if Case_color == 5:
			self.ButtonList[Id_scream].config 	(bg = "red",fg = "cyan")


		if Case_color != 4:
			qnt_on = 0
			for item in  range (len(Var.Lista.Relogios)):
				if id_emp == Var.Lista.Relogios[item][1]:
					if Var.Lista.Relogios[item][7] == True:
						qnt_on = qnt_on + 1

			for item in  range (len(Var.Lista.Empresas)):
				if Var.Lista.Empresas[item][0] == id_emp:
					index_empp 	= item
					Id_scream 	= Var.Lista.Empresas[item][8]
					total_rep 	= Var.Lista.Empresas[item][10]
					break

			
			self.botaoContage[Id_scream].config (text= str(qnt_on)
										 + "/" + str(total_rep))

			Telas.GUI_Monitor.updateContage(index_empp,qnt_on)





	def updHora(self, emp_index):
		Id_scream 	= Var.Lista.Empresas[emp_index][8]
		hora 		= Var.Lista.Empresas[emp_index][9]

		self.MsgHora[Id_scream].config (text = hora)