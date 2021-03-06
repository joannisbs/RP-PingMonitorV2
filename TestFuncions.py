import socket
import os
import shutil
import threading
import time
import sys

from Classes import *
from VariaveisGlobais import * 
import tkMessageBox as messagebox

from LeBanco import Mysqldb

class StopThread(StopIteration):
	pass
threading.SystemExit = SystemExit, StopThread

class Threads(threading.Thread):
	def stop(self):
		self.__stop = True
		#Controle.db.close()


	def _bootstrap(self, stop_thread=False):
		
		
		self.__stop = False
		sys.settrace(self.__trace)
		super()._bootstrap()

	def __trace(self, frame, event, arg):
		if self.__stop:
			raise StopThread()
		return self.__trace


class GraphOn:
	def __init__(self):
		self.hora = GetTime()
		self.minutos1  = "0"
		self.horinha = '0'

		self.n = 0
		self.num_hor	= 0
		self.datainit = self.hora.completa()

		#ar.Lista.graphHLabel=[]
		#Var.Lista.graphHnum=[]
		#Var.Lista.graphH_t=[]
		
		#Var.Lista.graphH_v =[]
		#Var.Lista.graphH_p =[]
		#Var.Lista.graphH_c =[]
		#Var.Lista.graphH_o =[]
		#Var.Lista.graphH_g =[]

	def insertmin(self,percentt,percentv,percentc,percentp,percento,percentg):

		self.hora2 = GetTime()

		
		if self.hora2.sominuto() != self.minutos1:

			self.minutos1 = self.hora2.sominuto()

			Var.Lista.graphOn_x.append(self.hora2.horaminuto())
			Var.Lista.graphOn_y.append(percentt)
			Var.Lista.graphOn_n.append(self.n)

			
			Var.Lista.graphVivo_y.append(percentv)
			Var.Lista.graphPorto_y.append(percentp)
			Var.Lista.graphClaro_y.append(percentc)
			Var.Lista.graphOI_y.append(percento)
			Var.Lista.graph4G_y.append(percentg)



			data = self.hora2.completa()


			loggeral = open ("LogPercentsTotal"+ self.datainit + ".csv","ab+")
			loggeral.write  (str(self.n)+";"+str(percentt)+";"+ data +" \n")
			loggeral.close
				


			self.n = self.n + 1

			if self.hora2.sohora() != self.horinha:
				ho_dia = self.hora2.horaminuto()
				if self.horinha == '0':
					
					Var.Lista.graphHLabel.append(ho_dia)
					Var.Lista.graphHnum.append(self.num_hor)
					Var.Lista.graphH_t.append(percentt)
					
					Var.Lista.graphH_v.append(percentv)
					Var.Lista.graphH_p.append(percentp)
					Var.Lista.graphH_c.append(percentc)
					Var.Lista.graphH_o.append(percento)
					Var.Lista.graphH_g.append(percentg)

				else:
					Var.Lista.graphHLabel.append(ho_dia)
					Var.Lista.graphHnum.append(self.num_hor)


					soma = 0
					qnt_elements = len(Var.Lista.graphOn_y)
					for item in range (qnt_elements):
						soma = soma + Var.Lista.graphOn_y[item]

					media = soma/qnt_elements

					Var.Lista.graphH_t.append(media)



					soma = 0
					qnt_elements = len(Var.Lista.graphVivo_y)
					for item in range (qnt_elements):
						soma = soma + Var.Lista.graphVivo_y[item]

					media = soma/qnt_elements

					Var.Lista.graphH_v.append(media)



					soma = 0
					qnt_elements = len(Var.Lista.graphPorto_y)
					for item in range (qnt_elements):
						soma = soma + Var.Lista.graphPorto_y[item]

					media = soma/qnt_elements

					Var.Lista.graphH_p.append(media)




					soma = 0
					qnt_elements = len(Var.Lista.graphClaro_y)
					for item in range (qnt_elements):
						soma = soma + Var.Lista.graphClaro_y[item]

					media = soma/qnt_elements

					Var.Lista.graphH_c.append(media)

					soma = 0
					qnt_elements = len(Var.Lista.graphOI_y)
					for item in range (qnt_elements):
						soma = soma + Var.Lista.graphOI_y[item]

					media = soma/qnt_elements

					Var.Lista.graphH_o.append(media)


					soma = 0
					qnt_elements = len(Var.Lista.graph4G_y)
					for item in range (qnt_elements):
						soma = soma + Var.Lista.graph4G_y[item]

					media = soma/qnt_elements

					Var.Lista.graphH_g.append(media)


				self.horinha = self.hora2.sohora()

				self.num_hor = self.num_hor + 1
					
			Telas.GUI_Monitor.updateGraphtot()

class Servico:

	def __init__(self):
		#self.principal = Threads(target=Loop)
		self.principal2 = Threads(target=Loop2)

	def Start(self):
		print "start service"
		Controle.Roda = True
		Controle.Stop = False
		#self.principal.start()
		self.principal2.start()

	def Stop(self):
		Controle.Roda = False
		Controle.Stop = True
		#self.principal.stop()
		self.principal2.stop()
		time.sleep(2)
		print "stop service"
		return True

def DelayFunction(qntd_relos):
	if qntd_relos < 3:
		if Controle.Stop : return 5
		time.sleep(120)
	elif qntd_relos < 7:
		if Controle.Stop : return 5
		time.sleep(60)

	if Controle.Stop : return 5
	time.sleep(30)



def TestaPorta(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#print ip + " porta = " + port
	#print "Test Ping"
	if TestaPing(ip):
		#if Controle.Stop : return 5
		try:
			#if Controle.Stop : return 5
			s.connect((ip,int(port)))		
			s.close()
			return 3

		except:
			return 2

	else:
		return 1



def TestaPing(ip):
	if Controle.Stop : return False
	try:
		resposta = os.system("ping " + ip + " -c 2 -s 0 > logping.txt")
		if resposta == 0 :
			#print "ping ok"
			return True
		else:
			#print "Falha ping"
			return False	
	except:
		return False



def Loop():
	Controle.Roda = True
	volta = 0
	while Controle.Roda:

		if volta > 0:
			pass
		else:
			qnt_rep = len(Var.Lista.Relogios)
			if Controle.Stop : return
			for index_rep in range (qnt_rep):
				RT = Threads(target=TestaRelo,kwargs={'Rp_index':index_rep})
				RT.start()
				if Controle.Stop : return
		time.sleep(1)
		volta = volta + 1
		if volta > 450:
			volta = 0
		if Controle.Stop : break



def Loop2():
	Controle.Roda = True
	volta = 0
	#while Controle.Roda:
	#Controle.db = Mysqldb()
	#Controle.db.connect()
	if volta > 0:
		pass
	else:
		qnt_emp = len(Var.Lista.Empresas)
		for index_emp in range (qnt_emp):
			RT = Threads(target=TestaEmp,kwargs={'Emp_index':index_emp})
			RT.start()
		time.sleep(60)
		RT = Threads(target=GravaBanco)
		RT.start()
		#volta = volta + 1
		#if volta > 200:
			#volta = 0
		#if Controle.Stop : break

def GravaBanco():
	
	try:
		Controle.db = Mysqldb()
		Controle.db.connect()
		
		if len(Var.Lista.events) > 0:
			for row in range (0,len(Var.Lista.events)):
				
				ids = Var.Lista.events[row][0]
				result = Var.Lista.events[row][1]
				date = Var.Lista.events[row][2]
				
				Controle.db.insert(ids, result, date)

			Controle.db.close()
			
			Var.Lista.events = []
	

	except:
		print "erro de conexao"

	if Controle.Stop:return
	time.sleep(60)
	GravaBanco()



def RepOff(Rp_index):

	id_emp 			= Var.Lista.Relogios[Rp_index][1]
	IP_rep			= Var.Lista.Relogios[Rp_index][3]
	Porta_rep		= Var.Lista.Relogios[Rp_index][4]
	name_rep		= Var.Lista.Relogios[Rp_index][2]
	Index_emp = 0
	Quant_Empresas = len(Var.Lista.Empresas)
	for indexempresas in range (Quant_Empresas):
		if id_emp == Var.Lista.Empresas[indexempresas][0]:
			Index_emp = indexempresas
			break

	tela 		= Var.Lista.Empresas[Index_emp][2]
	name		= Var.Lista.Empresas[Index_emp][1]

	while(True):

		if Controle.Stop : return

		resultado = TestaPorta(IP_rep,Porta_rep)
		
		if Controle.Stop : return

		if resultado != 1:
			break
		
		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return

		time.sleep(5)
		
		if Controle.Stop : return



	if Var.Lista.Relogios[Rp_index][10] != 4:
		
		if resultado == 3:
			if (Var.Lista.Relogios[Rp_index][14] != resultado and 
			resultado!= 4 and Var.Lista.Relogios[Rp_index][10]!= "0"
			and Var.Lista.Relogios[Rp_index][10]!= 4):

				Var.Lista.Relogios[Rp_index][14] = resultado
				repins = Var.Lista.Relogios[Rp_index][0]
				timer = GetTime()
				times = timer.completedb()
				value = []
				value.append(repins)
				value.append(resultado)
				value.append(times)
				Var.Lista.events.append(value)
				
				#Controle.db.insert(repins,resultado,times)


		Var.Lista.Relogios[Rp_index][10] = resultado
		
		if Controle.Stop : return

		if tela == 1:
			Telas.GUI_Tela1.update(Rp_index)
		elif tela == 2: 
			Telas.GUI_Tela2.update(Rp_index)
		

		if Var.Lista.Relogios[Rp_index][10] == 3:
			
			
			if Var.Lista.Relogios[Rp_index][11]:
				messagebox.showinfo("Relogio On", 
					"O Relogio " + name_rep +
					"\nDa Empresa " + name +
					 "\nIP:  " + IP_rep + 
					 "\nFicou On-Line!")
				Var.Lista.Relogios[Rp_index][11] = False

				return




def TestaEmp(Emp_index):
	id_emp 		= Var.Lista.Empresas[Emp_index][0]
	tela 		= Var.Lista.Empresas[Emp_index][2]
	name		= Var.Lista.Empresas[Emp_index][1]
	Quant_Rep 	= len(Var.Lista.Relogios)
	relos 		= 0

	for rep in range (Quant_Rep):
		if Controle.Stop : break
		if Var.Lista.Relogios[rep][1] == id_emp:
			IP_rep			= Var.Lista.Relogios[rep][3]
			Porta_rep		= Var.Lista.Relogios[rep][4]
			name_rep		= Var.Lista.Relogios[rep][2]
			teste = Var.Lista.Relogios[rep][10]
			Var.Lista.Relogios[rep][10] = 4
			if Controle.Stop : break
			#pinta de azul
			if tela == 1:
				Telas.GUI_Tela1.update(rep)
			elif tela == 2: 
				Telas.GUI_Tela2.update(rep)
			#testa:
			if Controle.Stop : break
			resultado = TestaPorta(IP_rep,Porta_rep)
			

			if (Var.Lista.Relogios[rep][14] != resultado and 
			 teste!= "0" and Var.Lista.Relogios[rep][14]!= 0):
				#print Var.Lista.Relogios[rep][14]
				#print resultado
				Var.Lista.Relogios[rep][14] = resultado
				#print Var.Lista.Relogios[rep][14]
				repins = Var.Lista.Relogios[rep][0]
				timer = GetTime()
				times = timer.completedb()
				value = []
				value.append(repins)
				value.append(resultado)
				value.append(times)
				Var.Lista.events.append(value)
				#Controle.db.insert(repins,resultado,times)

			if Var.Lista.Relogios[rep][14]== 0:
				Var.Lista.Relogios[rep][14] = resultado
			
			Var.Lista.Relogios[rep][10] = resultado	

			#if Var.Lista.Relogios[rep][10] == 1:
				#if not Var.Lista.Relogios[rep][12]:
					#Var.Lista.Relogios[rep][12] = True
					#RT = Threads(target=RepOff,kwargs={'Rp_index':rep})
					#RT.start()



			if Var.Lista.Relogios[rep][10] == 3:
				if Var.Lista.Relogios[rep][11]:
					messagebox.showinfo("Relogio On", 
						"O Relogio " + name_rep +
						"\nDa Empresa " + name +
						 "\nIP:  " + IP_rep + 
						 "\nFicou On-Line!")
					Var.Lista.Relogios[rep][11] = False
			

			if Controle.Stop : break
			if tela == 1:
				Telas.GUI_Tela1.update(rep)
			elif tela == 2: 
				Telas.GUI_Tela2.update(rep)

		if Controle.Stop : break
		relos = relos + 1
	
	if Controle.Stop : 
		return
	else:

		DelayFunction(relos)
		relos = 0
		if Controle.Stop : return
		hora = GetTime()
		time = hora.horaminuto()
		Var.Lista.Empresas[Emp_index][9] = time
		if tela == 1:
			Telas.GUI_Tela1.updHora(Emp_index)
		elif tela == 2: 
			Telas.GUI_Tela2.updHora(Emp_index)
		RT = Threads(target=TestaEmp,kwargs={'Emp_index':Emp_index})
		RT.start()


def TestaRelo(Rp_index):
	id_emp 			= Var.Lista.Relogios[Rp_index][1]
	IP_rep			= Var.Lista.Relogios[Rp_index][3]
	Porta_rep		= Var.Lista.Relogios[Rp_index][4]
	name_rep		= Var.Lista.Relogios[Rp_index][2]
	Index_emp = 0
	Quant_Empresas = len(Var.Lista.Empresas)
	for indexempresas in range (Quant_Empresas):
		if id_emp == Var.Lista.Empresas[indexempresas][0]:
			Index_emp = indexempresas
			break

	tela 		= Var.Lista.Empresas[Index_emp][2]
	name		= Var.Lista.Empresas[Index_emp][1]
	resultado = TestaPorta(IP_rep,Porta_rep)
	

	if resultado == 1:
		for value in range(30):
			
			resultado = TestaPorta(IP_rep,Porta_rep)
			if Controle.Stop : break
			#if resultado == 3:
			#	if Var.Lista.Relogios[Rp_index][11]:
			#		messagebox.showinfo("Relogio On", 
			#			"O Relogio " + name +
				#		 "\nIP:  " + IP_rep + 
					#	 "\nFicou On-Line!")
					#Var.Lista.Relogios[Rp_index][11] = False
			if resultado != 1:
				break
		if Controle.Stop :return
	if Var.Lista.Relogios[Rp_index][10] != 4:
		
		Var.Lista.Relogios[Rp_index][10] = resultado
		if Controle.Stop : return
		if tela == 1:
			Telas.GUI_Tela1.update(Rp_index)
		elif tela == 2: 
			Telas.GUI_Tela2.update(Rp_index)
		if Var.Lista.Relogios[Rp_index][10] == 3:
			if Var.Lista.Relogios[Rp_index][11]:
				messagebox.showinfo("Relogio On", 
					"O Relogio " + name_rep +
					"\nDa Empresa " + name +
					 "\nIP:  " + IP_rep + 
					 "\nFicou On-Line!")
				Var.Lista.Relogios[Rp_index][11] = False



