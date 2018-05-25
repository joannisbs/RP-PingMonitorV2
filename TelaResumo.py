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
		self.Calc_Op()
		self.Create_containers(root)

		self.Create_Status()
		self.Create_emps()


	def Calc_Op(self):
		self.total_vivo 	= 0
		self.total_claro 	= 0
		self.total_porto 	= 0
		self.total_oi 		= 0
		self.total_4G 		= 0

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
									text = " |" ,
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
									fg="white",
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
									fg="white",
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
									fg="white",
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
									fg="white",
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
									fg="white",
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

	def Create_containers(self,root):
		self.ContainerStatus              = Frame (root,bg="black")
		self.ContainerStatus.grid                 (row=0, sticky = N + W + E)

		self.ContainerDiv              = Frame (root,bg="yellow")
		self.ContainerDiv.grid                 (row=1, sticky = N + W + E)

		self.ContainerDiv2              = Frame (self.ContainerDiv,bg="yellow")
		self.ContainerDiv2.grid                 (row=1,pady=1, sticky = N + W + E)

		self.ContaineParte2				= Frame(root,bg="black")
		self.ContaineParte2.grid                 (row=2,sticky = N + W + E + S)

		self.ContaineEmpresas1			= Frame(self.ContaineParte2,bg="black")
		self.ContaineEmpresas1.grid                 (row=0,pady=2, column=0, sticky = "N")

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
			coluna = 4
			row_line = id_emp - 30 + 1
		elif id_emp > 59:
			coluna = 8
			row_line = id_emp - 60 + 1
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
		percent = ((qnt_On_tot*100)/len(Var.Lista.Relogios))
		self.MesPercents.config(text = "  " + str(percent).zfill(2) + "%") 

		self.MesVivoCountOn.config(text =str(qnt_On_vivo).zfill(3) )
		self.MsgClaroCountOn.config(text =str(qnt_On_claro).zfill(3) )
		self.MsgPortoCountOn.config(text =str(qnt_On_porto).zfill(3) )
		self.MsgOiCountOn.config(text =str(qnt_On_oi).zfill(3) )
		self.Msg4GCountOn.config(text =str(qnt_On_4G).zfill(3) )

		percent = ((qnt_On_vivo*100)/self.total_vivo)
		self.MesVivoPerc.config(text =str(percent).zfill(2) + "% " )

		percent = ((qnt_On_claro*100)/self.total_claro)
		self.MsgClaroPerc.config(text =str(percent).zfill(2) + "% " )

		percent = ((qnt_On_porto*100)/self.total_porto )
		self.MsgPortoPerc.config(text =str(percent).zfill(2) + "% " )

		percent = ((qnt_On_oi*100)//self.total_oi )
		self.MsgOiPerc.config(text =str(percent).zfill(2) + "% " )

		percent = ((qnt_On_4G*100)//self.total_4G )
		self.Msg4GPerc.config(text =str(percent).zfill(2) + "% " )
