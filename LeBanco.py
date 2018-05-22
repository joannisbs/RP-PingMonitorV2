# -*- coding: utf-8 -*-
from VariaveisGlobais import * 

import mysql.connector
from VariaveisGlobais import * 
import sys



	

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
		Var.Lista.Empresas = "oi"
		Var.Lista.Empresas = []
		lista = []


		self.cursor.execute("SELECT COUNT(*) FROM db_ping.tbl_emp")
		count = self.cursor.fetchone()
		numtotal = int(count[0])


		self.cursor.execute("SELECT * FROM db_ping.tbl_emp")
		num = 1
		#print len(self.cursor.fetchall())
		print "loading company list "
		for row in self.cursor.fetchall():
			row = list(row + ("0","0","0"))
			lista.append(row)
			sys.stdout.write( "\r{0}%".format((num*100)/numtotal) )
			sys.stdout.flush()

			num = num + 1
		print " Its Done!\ncompany list load successful"
		Var.Lista.Empresas = lista


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
			row = list(row + ("0","0",False,))
			Var.Lista.Relogios.append(row)
			sys.stdout.write( "\r{0}%".format((num*100)/numtotal) )
			sys.stdout.flush()
			#print " ",row[0], " ", row[1], " ", row[2], " ", row[3] ," ", row[4]

			num = num + 1
		print " Its Done!\nrep list load successful"