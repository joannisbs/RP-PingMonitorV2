# -*- coding: utf-8 -*-
from VariaveisGlobais import * 

import mysql.connector
from VariaveisGlobais import * 
import sys


def leBanco():


	listaping = open("Lista_Empresas.csv","r")
	
	empresas = listaping.readlines()[1:]

	listaping.close()

	Var.Lista1.empresas = []
	Var.Lista2.empresas = []

	Var.Lista1.relogios = [[]for _ in range (len(empresas))]
	Var.Lista2.relogios = [[]for _ in range (len(empresas))]
	

	for line in empresas:

		word              = line.split(",")
		if word[0]=="1":
			Var.Lista1.empresas.append((word)[1:])
			#Var.Lista1.relogios.append(word[1])

		if word[0]=="2":
			Var.Lista2.empresas.append((word)[1:])


		#Var.Lista1.relogios.append("null")
	
	

	listarel = open("lista_relogio.csv","r")

	relogios = listarel.readlines()[1:]

	listarel.close()

	Quant_Empresas = len(Var.Lista1.empresas)


	Controle.TotalRelogios = len(relogios)

	for line in relogios:

		word              = line.split(",")
		#Var.Lista1.relogios.append(word)
		Tela				=int(word[0])
		if int(Tela) == 1 :
			Id_empresa			= int(word[1])
			Var.Lista1.relogios[Id_empresa].append(word[1:])

		if int(Tela) == 2 :
			Id_empresa			= int(word[1])
			Var.Lista2.relogios[Id_empresa].append(word[1:])
	


		

		

	

class Mysqldb:

	def __init__(self):
		pass

	def connect(self):
		print "trying connect to database with hos t= 192.168.0.150 , user = ping "
		try:
			db = mysql.connector.connect(host="192.168.0.150",user="ping",password='realponto102030',db="db_ping")
			self.connection = db
			self.cursor = db.cursor()

			print "connection has been established with successful"
		except:
			print "error conection with db"


	def close(self):
		self.cursor.close()
		self.connection.close()
		print "connection has closed"


	def CarregarEmpresas(self):

		Var.Lista.Empresas = []
		


		self.cursor.execute("SELECT COUNT(*) FROM db_ping.tbl_emp")
		count = self.cursor.fetchone()
		numtotal = int(count[0])


		self.cursor.execute("SELECT * FROM db_ping.tbl_emp")
		num = 1
		#print len(self.cursor.fetchall())
		print "loading company list "
		for row in self.cursor.fetchall():
			row = list(row + ("0",))
			Var.Lista.Empresas.append(row)
			sys.stdout.write( "\r{0}%".format((num*100)/numtotal) )
			sys.stdout.flush()

			num = num + 1
		print " Its Done!\ncompany list load successful"

	def CarregarRelogios(self):
		Var.Lista.Relogios = []

		self.cursor.execute("SELECT COUNT(*) FROM db_ping.tbl_rep")
		count = self.cursor.fetchone()
		numtotal = int(count[0])


		self.cursor.execute("SELECT * FROM db_ping.tbl_rep")
		num = 1
		#print len(self.cursor.fetchall())
		print "loading rep list "
		for row in self.cursor.fetchall():
			row = list(row + ("0",))
			Var.Lista.Relogios.append(row)
			sys.stdout.write( "\r{0}%".format((num*100)/numtotal) )
			sys.stdout.flush()

			num = num + 1
		print " Its Done!\nrep list load successful"