# -*- coding: utf-8 -*-

from Tkinter import *


#from Thread import *
from VariaveisGlobais import * 
from TestFuncions import *
from LeBanco import Mysqldb

import sys
import os


class Monitor:

	def __init__(self,root):

		self.MenuBar(root)
		self.IniciaList()
		self.Create_containers(root)
		self.Create_emps()



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

	def Create_containers(self,root):
		self.ContainerStatus              = Frame (root,bg="black")
		self.ContainerStatus.grid                 (row=0, sticky = "N")

		self.ContaineParte2				= Frame(root,bg="black")
		self.ContaineParte2.grid                 (row=1, sticky = "N")

		self.ContaineEmpresas1			= Frame(self.ContaineParte2,bg="black")
		self.ContaineEmpresas1.grid                 (row=0, column=0, sticky = "N")

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


		name_emp 			= Var.Lista.Empresas[id_emp][1]
		On_Line_rep			= 00
		total_rep 			= Var.Lista.Empresas[id_emp][10]
		Var.Lista.Empresas[id_emp][12] = id_emp


		if 60 > id_emp > 29:
			coluna = 5
			row_line = id_emp - 30
		elif id_emp > 59:
			coluna = 10
			row_line = id_emp - 60
		else:
			coluna = 0
			row_line = id_emp

		



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



		self.MsgContage 		= Label (
									self.ContaineEmpresas1,
									text = " On-Line: " ,
									font="arial 12",
									bg="black",
									fg="white",
									highlightbackground="black",
									activebackground="black",
									activeforeground="white",
									
									bd=0,
									height = 1)

			
		self.MsgContage.grid (
									row=row_line,
									column=coluna+2,
									pady=1)

		
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
									column=coluna+3,
									pady=1)


		self.MsgContagetot[id_emp] 		= Label (
									self.ContaineEmpresas1,
									text = " - " + (str(total_rep)).zfill(2),
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
									column=coluna+4,
									pady=3)



			
	def updateContage(self,index_empp,qnt_On):


		
		Id_scream 	= Var.Lista.Empresas[index_empp][12]
	
		
		self.MsgContageON[Id_scream].config ( text= (str(qnt_On)).zfill(2))

