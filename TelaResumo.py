# -*- coding: utf-8 -*-

from Tkinter import *


#from Thread import *
from VariaveisGlobais import * 
from TestFuncions import *
from LeBanco import Mysqldb
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 


import sys
import os


class Monitor:

	def __init__(self,root):

		self.MenuBar(root)
		self.IniciaList()
		self.Calc_Op()
		self.Create_containers(root)

		self.Create_Status()
		self.Create_emps()

		#self.Create_Graph()
		self.Create_Graphs()

	def Create_Graphs(self):
		self.Create_GraphTotal()
		#self.Create_GraphToOp()





	def Create_GraphTotal(self):
		


		fig = plt.figure(figsize=(12,6),facecolor="black")


		ax = plt.subplot(2,2,1)
		plt.ylim(0,100)

		#count = (len(self.list_n))
		#plt.xlim(self.list_n[0],self.list_n[count-1])

		plt.plot(0,0,"yellow", linewidth=1.0)		
		#plt.xticks(self.listl_n,self.list_x)
		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine na ultima hora",color="white")
		plt.grid( color='gray', linewidth=0.5)



		ax = plt.subplot(2,2,3)

		#count = (len(self.list_n))
		#plt.xlim(self.list_n[0],self.list_n[count-1])
		plt.ylim(0,100)
		plt.plot(0,0,"green", linewidth=1.0)
		plt.plot(0,0,"blue", linewidth=1.0)	
		plt.plot(0,0,"red", linewidth=1.0)	
		plt.plot(0,0,"orange", linewidth=1.0)	
		plt.plot(0,0,"purple", linewidth=1.0)		

		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		#plt.xticks(self.listl_n,self.list_x)
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine na ultima hora",color="white")
		plt.grid( color='gray', linewidth=0.5)


		ax = plt.subplot(2,2,2)
		plt.ylim(0,100)

		#count = (len(self.listhnum))
		#plt.xlim(self.listhnum[0],self.listhnum[count-1])

		plt.plot(0,0,"yellow", linewidth=1.0)		
		#plt.xticks(self.listhlabelnum,self.listhlabel)
		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine nas ultimas 24 hora",color="white")
		plt.grid( color='gray', linewidth=0.5)



		ax = plt.subplot(2,2,4)

		#count = (len(self.listhnum))
		#plt.xlim(self.listhnum[0],self.listhnum[count-1])
		plt.ylim(0,100)
		plt.plot(0,0,"green", linewidth=1.0)
		plt.plot(0,0,"blue", linewidth=1.0)	
		plt.plot(0,0,"red", linewidth=1.0)	
		plt.plot(0,0,"orange", linewidth=1.0)	
		plt.plot(0,0,"purple", linewidth=1.0)		

		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		#plt.xticks(self.listhlabelnum,self.listhlabel)
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine nas ultimas 24 hora",color="white")
		plt.grid( color='gray', linewidth=0.5)


		self.canvas = FigureCanvasTkAgg(fig,master = self.ContainerGrafc)
		self.canvas.get_tk_widget().grid(row=0,column = 0)
		self.canvas.draw()

	def Calc_Op(self):
		self.total_vivo   = 0
		self.total_claro   = 0
		self.total_porto   = 0
		self.total_oi     = 0
		self.total_4G     = 0
	
		for item in  range (len(Var.Lista.Relogios)):
			ips = Var.Lista.Relogios[item][3]
			if ips[0:5] == "10.26":
				Var.Lista.Relogios[item][13] = 1
				self.total_vivo = self.total_vivo + 1
		
			elif ips[0:6] == "172.40":
				Var.Lista.Relogios[item][13] = 2
				self.total_claro = self.total_claro + 1
		
			elif ips[0:6] == "10.115":
				Var.Lista.Relogios[item][13] = 3
				self.total_porto = self.total_porto + 1
		
			elif ips[0:5] == "10.50":
				Var.Lista.Relogios[item][13] = 4
				self.total_oi = self.total_oi + 1
		
			elif ips[0] != "1":
				Var.Lista.Relogios[item][13] = 5
				self.total_4G = self.total_4G + 1
		

	def Create_Status(self):


		Ttotal = len(Var.Lista.Relogios)


		self.MsgContageONTotal 		= Label (
									self.ContainerStatus,
									text = " On-Line: " ,
									font="arialblack 21 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContageONTotal.grid (
									row=0,
									column=0,
									pady=1)


		self.MsgContONTotal 		= Label (
									self.ContainerStatus,
									text = "000" ,
									font="arialblack 21 bold",
									bg="black",
									fg="green3",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContONTotal.grid (
									row=0,
									column=1,
									pady=1)


		self.MsgContageTotal 		= Label (
									self.ContainerStatus,
									text = "Total: " ,
									font="arialblack 21 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContageTotal.grid (
									row=0,
									column=3,
									pady=1)


		self.MsgContTotal 		= Label (
									self.ContainerStatus,
									text = str(Ttotal).zfill(4) ,
									font="arialblack 21 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContTotal.grid (
									row=0,
									column=4,
									pady=1)


		self.MesPercents 		= Label (
									self.ContainerStatus,
									text = " 0%" ,
									font="arialblack 21 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MesPercents.grid (
									row=0,
									column=2,
									pady=1)

		separate 		= Label (
									self.ContainerStatus,
									text = "|" ,
									font="arialblack 30 bold",
									bg="black",
									fg="yellow",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		separate.grid (
									row=0,
									column=5,
									pady=1)



		MsgVivo 					= Label (
									self.ContainerStatus,
									text = " Vivo " ,
									font="arialblack 18 bold",
									bg="black",
									fg="green",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MsgVivo.grid (
									row=0,
									column=6,
									pady=1)

		self.MesVivoCountOn 			= Label (
									self.ContainerStatus,
									text = "000" ,
									font="arialblack 18 bold",
									bg="black",
									fg="green3",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MesVivoCountOn.grid (
									row=0,
									column=8,
									pady=1)


		MesVivoCount 			= Label (
									self.ContainerStatus,
									text = "-"+str(self.total_vivo).zfill(3)+" " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MesVivoCount.grid (
									row=0,
									column=9,
									pady=1)




		self.MesVivoPerc 			= Label (
									self.ContainerStatus,
									text = "00% " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MesVivoPerc.grid (
									row=0,
									column=7,
									pady=1)



		separate 		= Label (
									self.ContainerStatus,
									text = "|" ,
									font="arialblack 30 bold",
									bg="black",
									fg="yellow",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		separate.grid (
									row=0,
									column=10,
									pady=1)


		MsgClaro 					= Label (
									self.ContainerStatus,
									text = " Claro " ,
									font="arialblack 18 bold",
									bg="black",
									fg="red",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MsgClaro.grid (
									row=0,
									column=11,
									pady=1)


		self.MsgClaroCountOn 			= Label (
									self.ContainerStatus,
									text = "000" ,
									font="arialblack 18 bold",
									bg="black",
									fg="green3",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgClaroCountOn.grid (
									row=0,
									column=13,
									pady=1)


		MsgClaroCount 			= Label (
									self.ContainerStatus,
									text = "-"+str(self.total_claro).zfill(3)+" " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MsgClaroCount.grid (
									row=0,
									column=14,
									pady=1)


		self.MsgClaroPerc 			= Label (
									self.ContainerStatus,
									text = "00% " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgClaroPerc.grid (
									row=0,
									column=12,
									pady=1)


		separate 		= Label (
									self.ContainerStatus,
									text = "|" ,
									font="arialblack 30 bold",
									bg="black",
									fg="yellow",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		separate.grid (
									row=0,
									column=15,
									pady=1)



		MsgPorto 					= Label (
									self.ContainerStatus,
									text = " Porto " ,
									font="arialblack 18 bold",
									bg="black",
									fg="blue",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MsgPorto.grid (
									row=0,
									column=16,
									pady=1)


		self.MsgPortoCountOn 			= Label (
									self.ContainerStatus,
									text = "000" ,
									font="arialblack 18 bold",
									bg="black",
									fg="green3",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgPortoCountOn.grid (
									row=0,
									column=18,
									pady=1)


		MsgPortoCount 			= Label (
									self.ContainerStatus,
									text = "-"+str(self.total_porto).zfill(3)+" " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MsgPortoCount.grid (
									row=0,
									column=19,
									pady=1)


		self.MsgPortoPerc 			= Label (
									self.ContainerStatus,
									text = "00% " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgPortoPerc.grid (
									row=0,
									column=17,
									pady=1)


		separate 		= Label (
									self.ContainerStatus,
									text = "|" ,
									font="arialblack 30 bold",
									bg="black",
									fg="yellow",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		separate.grid (
									row=0,
									column=20,
									pady=1)



		MsgOi 					= Label (
									self.ContainerStatus,
									text = " Oi " ,
									font="arialblack 18 bold",
									bg="black",
									fg="orange",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MsgOi.grid (
									row=0,
									column=21,
									pady=1)


		self.MsgOiCountOn 			= Label (
									self.ContainerStatus,
									text = "000" ,
									font="arialblack 18 bold",
									bg="black",
									fg="green3",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgOiCountOn.grid (
									row=0,
									column=23,
									pady=1)

		MsgOiCount 			= Label (
									self.ContainerStatus,
									text = "-"+str(self.total_oi).zfill(3)+" ",
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		MsgOiCount.grid (
									row=0,
									column=24,
									pady=1)


		self.MsgOiPerc 			= Label (
									self.ContainerStatus,
									text = "00% " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgOiPerc.grid (
									row=0,
									column=22,
									pady=1)


		separate 		= Label (
									self.ContainerStatus,
									text = "|" ,
									font="arialblack 30 bold",
									bg="black",
									fg="yellow",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		separate.grid (
									row=0,
									column=25,
									pady=1)



		Msg4G 					= Label (
									self.ContainerStatus,
									text = " 4G " ,
									font="arialblack 18 bold",
									bg="black",
									fg="purple",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		Msg4G.grid (
									row=0,
									column=26,
									pady=1)


		self.Msg4GCountOn 			= Label (
									self.ContainerStatus,
									text = "000" ,
									font="arialblack 18 bold",
									bg="black",
									fg="green3",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.Msg4GCountOn.grid (
									row=0,
									column=28,
									pady=1)

		self.Msg4GCount 			= Label (
									self.ContainerStatus,
									text = "-"+str(self.total_4G).zfill(3)+" " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.Msg4GCount.grid (
									row=0,
									column=29,
									pady=1)


		self.Msg4GPerc 			= Label (
									self.ContainerStatus,
									text = "00% " ,
									font="arialblack 18 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.Msg4GPerc.grid (
									row=0,
									column=27,
									pady=1)



	def MenuBar(self,root):
		menubar 			= Menu(root)
		root.configure(menu = menubar)
		menuReports 		= Menu(menubar)
		menuDatabase	 	= Menu(menubar)
		menuAbout			= Menu(menubar)

		menubar.add_cascade(label = 'Relatórios',menu=menuReports)
		menubar.add_cascade(label = 'Database',menu=menuDatabase)
		menubar.add_cascade(label = 'Sobre',menu=menuAbout)

		menuDatabase.add_command(label="AtualizarDB", command=self.AtualizarDatabase)

	def IniciaList(self):
		self.MsgName 		=[]
		self.botaoAtencao 	=[]
		self.MsgContageON 	=[]
		self.MsgContagetot 	=[]
		self.graphTot = GraphOn()

	def Create_containers(self,root):
		self.ContainerStatus           	 	= Frame (root,bg="black")
		self.ContainerStatus.grid                 (row=0, sticky = N + W + E)

		self.ContainerDiv             		= Frame (root,bg="yellow")
		self.ContainerDiv.grid                 (row=1, sticky = N + W + E)

		self.ContainerDiv2              	= Frame (self.ContainerDiv,bg="yellow")
		self.ContainerDiv2.grid                 (row=1,pady=1, sticky = N + W + E)

		self.ContaineParte2					= Frame(root,bg="black")
		self.ContaineParte2.grid                 (row=2,sticky = N + W + E + S)

		self.ContaineEmpresas1				= Frame(self.ContaineParte2,bg="black")
		self.ContaineEmpresas1.grid                 (row=0,pady=2, column=0, sticky = "N")

		self.Containesep					= Frame(self.ContaineParte2,bg="yellow")
		self.Containesep.grid                 (row=0,padx=2, column=1, sticky = "N")

		self.ContainerGrafc					= Frame(self.ContaineParte2,bg="blue")
		self.ContainerGrafc.grid                 (row=0,padx=2, column=2, sticky = N + W + E + S)

	def AtualizarDatabase(self):
		
		serv = Servico()
		serv.Stop()

		time.sleep(15)
		Telas.root.destroy()

		python = sys.executable
		os.execl(python, python, * sys.argv)




	def Create_emps(self):

		
		for item in  range (len(Var.Lista.Empresas)):
			self.Create_emp(item)



	def Create_emp(self,id_emp):
		
		self.MsgName.append				("")
		self.botaoAtencao.append 		("")
		self.MsgContageON.append		("")
		self.MsgContagetot.append 		("")

		qnt = (len(Var.Lista.Empresas)+1)/3
		

		name_emp 			= Var.Lista.Empresas[id_emp][1]
		On_Line_rep			= 00
		total_rep 			= Var.Lista.Empresas[id_emp][10]
		Var.Lista.Empresas[id_emp][12] = id_emp



		if (qnt*2 ) > id_emp >= (qnt):
			coluna = 4
			row_line = id_emp - (qnt)  + 1
		elif id_emp >= (qnt*2):
			coluna = 8
			row_line = id_emp - (qnt*2 ) + 1
		else:
			coluna = 0
			row_line = id_emp + 1

		

		if row_line == 1:

			self.MsgCabName				= Label (
									self.ContaineEmpresas1,
									text = "Empresa",
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									width=15)

			self.MsgCabName.grid(
									row=0,
									column=coluna)




			self.MsgCabOn 		= Label (
									self.ContaineEmpresas1,
									text = "On" ,
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1,
									width=5)

			
			self.MsgCabOn.grid (
									row=0,
									column=coluna+2,
									pady=3)


			self.MsgCabTot 		= Label (
									self.ContaineEmpresas1,
									text = "Total" ,
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
			self.MsgCabTot.grid (
									row=0,
									column=coluna+3,
									pady=1)





		self.MsgName[id_emp]				= Label (
									self.ContaineEmpresas1,
									text = name_emp,
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									width=15)

		self.MsgName[id_emp].grid(
									row=row_line,
									column=coluna)


			


		self.botaoAtencao[id_emp]  		= Button( 
									self.ContaineEmpresas1,
									font="arial 11 bold" , 
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									text='OK',
									bg="green3",
									width=2,
									height=1)

		self.botaoAtencao[id_emp].grid (
									row=row_line,
									column=coluna+1,
									sticky = "N")





		
		self.MsgContageON[id_emp] 		= Label (
									self.ContaineEmpresas1,
									text = (str(On_Line_rep)).zfill(2),
									font="arialblack 12 bold",
									bg="black",
									fg="yellow",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContageON[id_emp].grid (
									row=row_line,
									column=coluna+2,
									pady=1)


		self.MsgContagetot[id_emp] 		= Label (
									self.ContaineEmpresas1,
									text = (str(total_rep)).zfill(2),
									font="arialblack 12 bold",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContagetot[id_emp].grid (
									row=row_line,
									column=coluna+3,
									pady=3)



			
	def updateContage(self,index_empp,qnt_On):


		
		Id_scream 	= Var.Lista.Empresas[index_empp][12]
	
		
		self.MsgContageON[Id_scream].config ( text= (str(qnt_On)).zfill(2))





		qnt_On_tot 		= 0
		qnt_On_vivo 	= 0
		qnt_On_claro 	= 0
		qnt_On_porto 	= 0
		qnt_On_oi 		= 0
		qnt_On_4G 	 	= 0
		for item in  range (len(Var.Lista.Relogios)):
			if Var.Lista.Relogios[item][7] == True:
				qnt_On_tot = qnt_On_tot + 1

				if Var.Lista.Relogios[item][13] == 1:
					qnt_On_vivo = qnt_On_vivo + 1

				elif Var.Lista.Relogios[item][13] == 2:
					qnt_On_claro = qnt_On_claro + 1

				elif Var.Lista.Relogios[item][13] == 3:
					qnt_On_porto = qnt_On_porto + 1

				elif Var.Lista.Relogios[item][13] == 4:
					qnt_On_oi = qnt_On_oi + 1

				elif Var.Lista.Relogios[item][13] == 5:
					qnt_On_4G = qnt_On_4G + 1

		self.MsgContONTotal.config(text =  str(qnt_On_tot).zfill(4))
		percentt = ((qnt_On_tot*100)/len(Var.Lista.Relogios))
		self.MesPercents.config(text = "  " + str(percentt).zfill(2) + "% ") 



		self.MesVivoCountOn.config(text =str(qnt_On_vivo).zfill(3) )
		self.MsgClaroCountOn.config(text =str(qnt_On_claro).zfill(3) )
		self.MsgPortoCountOn.config(text =str(qnt_On_porto).zfill(3) )
		self.MsgOiCountOn.config(text =str(qnt_On_oi).zfill(3) )
		self.Msg4GCountOn.config(text =str(qnt_On_4G).zfill(3) )

		percentv = ((qnt_On_vivo*100)/self.total_vivo)
		self.MesVivoPerc.config(text =str(percentv).zfill(2) + "% " )

		percentc = ((qnt_On_claro*100)/self.total_claro)
		self.MsgClaroPerc.config(text =str(percentc).zfill(2) + "% " )

		percentp = ((qnt_On_porto*100)/self.total_porto )
		self.MsgPortoPerc.config(text =str(percentp).zfill(2) + "% " )

		percento = ((qnt_On_oi*100)//self.total_oi )
		self.MsgOiPerc.config(text =str(percento).zfill(2) + "% " )

		percentg = ((qnt_On_4G*100)//self.total_4G )
		self.Msg4GPerc.config(text =str(percentg).zfill(2) + "% " )

		self.graphTot.insertmin(percentt,percentv,percentc,percentp,percento,percentg)

	def updateGraphtot(self):
		
		self.listl_n = Var.Lista.graphOn_n		
		self.list_n = Var.Lista.graphOn_n
		self.list_x = Var.Lista.graphOn_x
		self.list_y = Var.Lista.graphOn_y

		self.listv_y = Var.Lista.graphVivo_y
		self.listc_y = Var.Lista.graphClaro_y
		self.listp_y = Var.Lista.graphPorto_y
		self.listo_y = Var.Lista.graphOI_y
		self.listg_y = Var.Lista.graph4G_y


		self.listhlabel	= Var.Lista.graphHLabel
		self.listhnum = Var.Lista.graphHnum
		self.listhlabelnum = self.listhnum
		self.listt_h = Var.Lista.graphH_t

		self.listv_h = Var.Lista.graphH_v
		self.listc_h = Var.Lista.graphH_c
		self.listp_h = Var.Lista.graphH_p
		self.listo_h = Var.Lista.graphH_o
		self.listg_h = Var.Lista.graphH_g



		if len(Var.Lista.graphHnum)>23:

			self.listhnum = Var.Lista.graphHnum[-24:]
			self.listhlabel = Var.Lista.graphHLabel[-24:]
			
			self.listt_h = Var.Lista.graphH_t[-24:]

			self.listv_h = Var.Lista.graphH_v[-24:]
			self.listc_h = Var.Lista.graphH_c[-24:]
			self.listp_h = Var.Lista.graphH_p[-24:]
			self.listo_h = Var.Lista.graphH_o[-24:]
			self.listg_h = Var.Lista.graphH_g[-24:]

			Var.Lista.graphOn_n = Var.Lista.graphOn_n[-24:]
			Var.Lista.graphOn_x = Var.Lista.graphOn_x[-24:]
			Var.Lista.graphOn_y = Var.Lista.graphOn_y[-24:]
			

			Var.Lista.graphVivo_y = Var.Lista.graphVivo_y[-23:]
			Var.Lista.graphClaro_y = Var.Lista.graphClaro_y[-23:]
			Var.Lista.graphPorto_y = Var.Lista.graphPorto_y[-23:]
			Var.Lista.graphOI_y = Var.Lista.graphOI_y[-23:]
			Var.Lista.graph4G_y = Var.Lista.graph4G_y[-23:]


			self.listhlabelnum = self.listhnum[::4]
			self.listhlabel = self.listhlabel[::4]

		elif 24>len(Var.Lista.graphHnum)>17:
					
			self.listhlabelnum = self.listhnum[::4]
			self.listhlabel = self.listhlabel[::4]

		elif 18>len(Var.Lista.graphHnum)>11:
					
			self.listhlabelnum = self.listhnum[::3]
			self.listhlabel = self.listhlabel[::3]

		elif 12>len(Var.Lista.graphHnum)>5:
					
			self.listhlabelnum = self.listhnum[::2]
			self.listhlabel = self.listhlabel[::2]

		else:
			self.listhlabelnum = self.listhnum
			self.listhlabel = self.listhlabel





		if len(Var.Lista.graphOn_n)>60:
			print "case more 62"

			self.list_n = Var.Lista.graphOn_n[-61:]
			self.list_x = Var.Lista.graphOn_x[-61:]
			self.list_y = Var.Lista.graphOn_y[-61:]

			self.listv_y = Var.Lista.graphVivo_y[-61:]
			self.listc_y = Var.Lista.graphClaro_y[-61:]
			self.listp_y = Var.Lista.graphPorto_y[-61:]
			self.listo_y = Var.Lista.graphOI_y[-61:]
			self.listg_y = Var.Lista.graph4G_y[-61:]

			Var.Lista.graphOn_n = Var.Lista.graphOn_n[-61:]
			Var.Lista.graphOn_x = Var.Lista.graphOn_x[-61:]
			Var.Lista.graphOn_y = Var.Lista.graphOn_y[-61:]
			

			Var.Lista.graphVivo_y = Var.Lista.graphVivo_y[-60:]
			Var.Lista.graphClaro_y = Var.Lista.graphClaro_y[-60:]
			Var.Lista.graphPorto_y = Var.Lista.graphPorto_y[-60:]
			Var.Lista.graphOI_y = Var.Lista.graphOI_y[-60:]
			Var.Lista.graph4G_y = Var.Lista.graph4G_y[-60:]


			self.listl_n = self.list_n[::10]
			self.list_x = self.list_x[::10]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])
	

		elif 61>len(Var.Lista.graphOn_n)>56:
			
			print "case more 56"

			



			self.listl_n = self.list_n[::9]
			self.list_x = self.list_x[::9]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])
	

		elif 57 > len(Var.Lista.graphOn_n)>49:
			
			print "case more 49"


			

			self.listl_n = self.list_n[::8]
			self.list_x = self.list_x[::8]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])


		elif 50 > len(Var.Lista.graphOn_n)>42:
			print "case more 42"
		



			self.listl_n = self.list_n[::7]
			self.list_x = self.list_x[::7]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])


		elif 43 > len(Var.Lista.graphOn_n)>35:
			print "case more 35"



	


			self.listl_n = self.list_n[::6]
			self.list_x = self.list_x[::6]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])


		elif 36 > len(Var.Lista.graphOn_n)>28:
			print "case more 28"


			self.listl_n = self.list_n[::5]
			self.list_x = self.list_x[::5]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])



		elif 29 > len(Var.Lista.graphOn_n)>21:
			print "case more 21"


			self.listl_n = self.list_n[::4]
			self.list_x = self.list_x[::4]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])

		
		elif 22 > len(Var.Lista.graphOn_n)>14:
			print "case more 14"


			self.listl_n = self.list_n[::3]
			self.list_x = self.list_x[::3]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])


		elif 15 > len(Var.Lista.graphOn_n) > 7:
			print "case more 7"


			self.listl_n = self.list_n[::2]
			self.list_x = self.list_x[::2]
			#self.listl_n.append(self.list_n[-1:])
			#self.list_x.append(self.list_x[-1:])



		else:
			print "case =("

			self.listl_n =self.list_n
			#self.list_x = list_x
			#self.listl_n.append(list_n[-1:])
			#self.list_x.append(list_x[-1:])

		


		self.updategraphcsgeneric()


	def updateGraphtotOp(self):
				
		self.graph2.cla()	
		
		self.graph2.set_ylim(0,100)

		#self.pltgra2.marker('+')
		

		#self.graph1.tick_params(axis='x', colors= 'white')
		#self.graph1.tick_params(axis='y', colors= 'white')

		self.graph2.grid( color='gray', linestyle='--', linewidth=0.5)
		
		#self.graph1.set_axis_bgcolor("black")

		#self.graph1.spines['left'].set_color('white')
		#self.graph1.spines['right'].set_color('white')	
		#self.graph1.spines['top'].set_color('white')
		#self.graph1.spines['bottom'].set_color('white')

		self.graph2.set_ylabel("Valores em Porcentagem %",color="white")
		self.graph2.set_title("OnLine na ultima hora",color="white")


		if len(Var.Lista.graphOn_n)>63:
			


			listv_n = Var.Lista.graphVivo_n[-63:]
			listv_x = Var.Lista.graphVivo_y[-63:]
			listv_y = Var.Lista.graphVivo_x[-63:]

			#listp_n = Var.Lista.graphPorto_n[-63:]
			#listp_x = Var.Lista.graphPorto_x[-63:]
			listp_y = Var.Lista.graphPorto_y[-63:]

			#listc_n = Var.Lista.graphClaro_n[-63:]
			#listc_x = Var.Lista.graphClaro_x[-63:]
			listc_y = Var.Lista.graphClaro_y[-63:]

			#listo_n = Var.Lista.graphOI_n[-63:]
			#listo_x = Var.Lista.graphOI_x[-63:]
			listo_y = Var.Lista.graphOI_y[-63:]

			#listg_n = Var.Lista.graph4G_n[-63:]
			#listg_x = Var.Lista.graph4G_x[-63:]
			listg_y = Var.Lista.graph4G_y[-63:]


			#Var.Lista.graphVivo_n = Var.Lista.graphVivo_n[-63:]
			#Var.Lista.graphVivo_x = Var.Lista.graphVivo_y[-63:]
			Var.Lista.graphVivo_y = Var.Lista.graphVivo_x[-63:]

			#Var.Lista.graphPorto_n = Var.Lista.graphPorto_n[-63:]
			#Var.Lista.graphPorto_x = Var.Lista.graphPorto_x[-63:]
			Var.Lista.graphPorto_y = Var.Lista.graphPorto_y[-63:]

			#Var.Lista.graphClaro_n = Var.Lista.graphClaro_n[-63:]
			#Var.Lista.graphClaro_x = Var.Lista.graphClaro_x[-63:]
			Var.Lista.graphClaro_y = Var.Lista.graphClaro_y[-63:]

			#Var.Lista.graphOI_n = Var.Lista.graphOI_n[-63:]
			#Var.Lista.graphOI_x = Var.Lista.graphOI_x[-63:]
			Var.Lista.graphOI_y = Var.Lista.graphOI_y[-63:]

			#Var.Lista.graph4G_n = Var.Lista.graph4G_n[-63:]
			#Var.Lista.graph4G_x = Var.Lista.graph4G_x[-63:]
			Var.Lista.graph4G_y = Var.Lista.graph4G_y[-63:]


			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::9],listv_x[::9])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])






		elif 56 > len(Var.Lista.graphOn_n)>49:
			
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::8],listv_y[::8])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

		elif 50 > len(Var.Lista.graphOn_n)>42:
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::7],listv_y[::7])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])


		elif 43 > len(Var.Lista.graphOn_n)>35:
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::86],listv_y[::6])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

		elif 36 > len(Var.Lista.graphOn_n)>28:
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::5],listv_y[::5])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])



		elif 29 > len(Var.Lista.graphOn_n)>21:
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::4],listv_y[::4])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

		
		elif 22 > len(Var.Lista.graphOn_n)>14:
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::3],listv_y[::3])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])
		


		elif 15 > len(Var.Lista.graphOn_n) > 7:
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n[::2],listv_y[::2])

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])
		


		else:
			
			listv_n = Var.Lista.graphVivo_n
			listv_x = Var.Lista.graphVivo_y
			listv_y = Var.Lista.graphVivo_x

			#listp_n = Var.Lista.graphPorto_n
			#listp_x = Var.Lista.graphPorto_x
			listp_y = Var.Lista.graphPorto_y

			#listc_n = Var.Lista.graphClaro_n
			#listc_x = Var.Lista.graphClaro_x
			listc_y = Var.Lista.graphClaro_y

			#listo_n = Var.Lista.graphOI_n
			#listo_x = Var.Lista.graphOI_x
			listo_y = Var.Lista.graphOI_y

			#listg_n = Var.Lista.graph4G_n
			#listg_x = Var.Lista.graph4G_x
			listg_y = Var.Lista.graph4G_y

			

			self.pltgra2.plot(listv_n,listv_y,"green3", linewidth=1.0)
			self.pltgra2.xticks(listv_n,listv_y)

			self.pltgra2.plot(listv_n,listp_y,"blue", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],listp_x[::9])

			self.pltgra2.plot(listv_n,listc_y,"red", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listo_y,"orange", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])

			self.pltgra2.plot(listv_n,listg_y,"purple", linewidth=1.0)
			#self.pltgra2.xticks(listv_n[::9],list_x[::9])


		self.canvas2.draw()

	def close(self):
		plt.close()



	def updategraphcsgeneric(self):
		print "aqui"

		plt.cla()	
		
		fig = plt.figure(figsize=(12,6),facecolor="black")


		ax = plt.subplot(2,2,1)
		plt.ylim(0,100)

		count = (len(self.list_n))
		plt.xlim(self.list_n[0],self.list_n[count-1])

		plt.plot(self.list_n,self.list_y,"yellow", linewidth=1.0)		
		plt.xticks(self.listl_n,self.list_x)
		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine na ultima hora",color="white")
		plt.grid( color='gray', linewidth=0.5)



		ax = plt.subplot(2,2,3)

		count = (len(self.list_n))
		plt.xlim(self.list_n[0],self.list_n[count-1])
		plt.ylim(0,100)
		plt.plot(self.list_n,self.listv_y,"green", linewidth=1.0)
		plt.plot(self.list_n,self.listp_y,"blue", linewidth=1.0)	
		plt.plot(self.list_n,self.listc_y,"red", linewidth=1.0)	
		plt.plot(self.list_n,self.listo_y,"orange", linewidth=1.0)	
		plt.plot(self.list_n,self.listg_y,"purple", linewidth=1.0)		

		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		plt.xticks(self.listl_n,self.list_x)
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine na ultima hora",color="white")
		plt.grid( color='gray', linewidth=0.5)


		ax = plt.subplot(2,2,2)
		plt.ylim(0,100)

		count = (len(self.listhnum))
		plt.xlim(self.listhnum[0],self.listhnum[count-1])

		plt.plot(self.listhnum,self.listt_h,"yellow", linewidth=1.0)		
		plt.xticks(self.listhlabelnum,self.listhlabel)
		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine nas ultimas 24 hora",color="white")
		plt.grid( color='gray', linewidth=0.5)



		ax = plt.subplot(2,2,4)

		count = (len(self.listhnum))
		plt.xlim(self.listhnum[0],self.listhnum[count-1])
		plt.ylim(0,100)
		plt.plot(self.listhnum,self.listv_h,"green", linewidth=1.0)
		plt.plot(self.listhnum,self.listp_h,"blue", linewidth=1.0)	
		plt.plot(self.listhnum,self.listc_h,"red", linewidth=1.0)	
		plt.plot(self.listhnum,self.listo_h,"orange", linewidth=1.0)	
		plt.plot(self.listhnum,self.listg_h,"purple", linewidth=1.0)		

		ax.set_axis_bgcolor("black")
		ax.spines['left'].set_color('white')
		ax.spines['right'].set_color('white')	
		ax.spines['top'].set_color('white')
		ax.spines['bottom'].set_color('white')
		plt.xticks(self.listhlabelnum,self.listhlabel)
		plt.tick_params(axis='x', colors= 'white')
		plt.tick_params(axis='y', colors= 'white')
		plt.ylabel("Valores em Porcentagem %",color="white")
		plt.title("OnLine nas ultimas 24 hora",color="white")
		plt.grid( color='gray', linewidth=0.5)


		self.canvas = FigureCanvasTkAgg(fig,master = self.ContainerGrafc)
		self.canvas.get_tk_widget().grid(row=0,column = 0)
		self.canvas.draw()