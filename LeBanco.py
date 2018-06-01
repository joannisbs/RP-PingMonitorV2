# -*- coding: utf-8 -*-
from VariaveisGlobais import * 

import mysql.connector
from VariaveisGlobais import * 
import sys



	

class Mysqldb:

	def __init__(self):
		pass

	def connect(self):
		#print "trying connect to database with hos t= 192.168.0.150 , user = ping "
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
		#print "connection has closed"


	def CarregarEmpresas(self):
		Var.Lista.Empresas = "oi"
		Var.Lista.Empresas = []
		lista = []


		self.cursor.execute("SELECT COUNT(*) FROM db_teste.tbl_emp")
		count = self.cursor.fetchone()
		numtotal = int(count[0])


		self.cursor.execute("SELECT * FROM db_teste.tbl_emp")
		num = 1
		#print len(self.cursor.fetchall())
		#print "loading company list "
		for row in self.cursor.fetchall():
			row = list(row + ("0","0","0","0","0",))
			lista.append(row)
			#sys.stdout.write( "\r{0}%".format((num*100)/numtotal) )
			#sys.stdout.flush()

			num = num + 1
		#print " Its Done!\ncompany list load successful"
		Var.Lista.Empresas = lista


	def CarregarRelogios(self):
		Var.Lista.Relogios = []

		self.cursor.execute("SELECT COUNT(*) FROM db_teste.tbl_rep")
		count = self.cursor.fetchone()
		numtotal = int(count[0])


		self.cursor.execute("SELECT * FROM db_teste.tbl_rep")
		num = 1
		#print len(self.cursor.fetchall())
		#print "loading rep list "
		for row in self.cursor.fetchall():
			row = list(row + ("0","0",False,False,0,0,))
			Var.Lista.Relogios.append(row)
			#sys.stdout.write( "\r{0}%".format((num*100)/numtotal) )
			#sys.stdout.flush()
			#print " ",row[0], " ", row[1], " ", row[2], " ", row[3] ," ", row[4]

			num = num + 1
		#print " Its Done!\nrep list load successful"
		
	def insert(self, rep, status, date):
		
		#self.connect()

		#if not Controle.conect:
			#Controle.conect = True
			#self.connect()


		query = ("INSERT INTO db_teste.tbl_events (id_rep, status, dates) VALUES (%s, %s, %s)")
		datos = (rep, status, date)
		#print query,datos
		self.cursor.execute(query,datos)

		self.connection.commit()
		

		#self.close()


		#print rep, status, date

	def get_history(self,id_rep):
		self.cursor.execute("SELECT * FROM db_teste.tbl_events WHERE id_rep = " + str(id_rep) )
		Var.Lista.History = []
		for row in self.cursor.fetchall():
			Var.Lista.History.append(row)
		