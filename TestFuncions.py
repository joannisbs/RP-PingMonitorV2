import socket
import os
import shutil
import threading
import time
import sys

from Classes import *
from VariaveisGlobais import * 


class StopThread(StopIteration):
	pass
threading.SystemExit = SystemExit, StopThread

class Threads(threading.Thread):
	def stop(self):
		self.__stop = True


	def _bootstrap(self, stop_thread=False):
		
		
		self.__stop = False
		sys.settrace(self.__trace)
		super()._bootstrap()

	def __trace(self, frame, event, arg):
		if self.__stop:
			raise StopThread()
		return self.__trace





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
		if Controle.Stop : return 5
		try:
			if Controle.Stop : return 5
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


class Servico:

	def __init__(self):
		pass

	def Start(self):
		print "start service"
		self.principal = Threads(target=Loop)
		self.principal.start()
		self.principal = Threads(target=Loop2)
		self.principal.start()

	def Stop(self):
		Controle.Roda = False
		Controle.Stop = True
		self.principal.stop()
		time.sleep(2)
		print "stop service"
		return True

def Loop():
	Controle.Roda = True
	volta = 0
	while Controle.Roda:

		if volta > 0:
			pass
		else:
			qnt_rep = len(Var.Lista.Relogios)
			for index_rep in range (qnt_rep):
				RT = Threads(target=TestaRelo,kwargs={'Rp_index':index_rep})
				RT.start()
		time.sleep(1)
		volta = volta + 1
		if volta > 450:
			volta = 0
		if Controle.Stop : break

def Loop2():
	Controle.Roda = True
	volta = 0
	#while Controle.Roda:

	if volta > 0:
		pass
	else:
		qnt_emp = len(Var.Lista.Empresas)
		for index_emp in range (qnt_emp):
			RT = Threads(target=TestaEmp,kwargs={'Emp_index':index_emp})
			RT.start()
		time.sleep(1)
		#volta = volta + 1
		#if volta > 200:
			#volta = 0
		#if Controle.Stop : break

def TestaEmp(Emp_index):
	id_emp 		= Var.Lista.Empresas[Emp_index][0]
	tela 		= Var.Lista.Empresas[Emp_index][2]
	Quant_Rep 	= len(Var.Lista.Relogios)
	relos 		= 0

	for rep in range (Quant_Rep):
		if Controle.Stop : break
		if Var.Lista.Relogios[rep][1] == id_emp:
			IP_rep			= Var.Lista.Relogios[rep][3]
			Porta_rep		= Var.Lista.Relogios[rep][4]
			Var.Lista.Relogios[rep][10] = 4
			if Controle.Stop : break
			#pinta de azul
			if tela == 1:
				Telas.GUI_Tela1.update(rep)
			elif tela == 2: 
				Telas.GUI_Tela2.update(rep)
			#testa:
			if Controle.Stop : break
			Var.Lista.Relogios[rep][10] =TestaPorta(IP_rep,Porta_rep)
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
		RT = Threads(target=TestaEmp,kwargs={'Emp_index':Emp_index})
		RT.start()





def TestaRelo(Rp_index):
	id_emp 			= Var.Lista.Relogios[Rp_index][1]
	IP_rep			= Var.Lista.Relogios[Rp_index][3]
	Porta_rep		= Var.Lista.Relogios[Rp_index][4]
	Index_emp = 0
	Quant_Empresas = len(Var.Lista.Empresas)
	for indexempresas in range (Quant_Empresas):
		if id_emp == Var.Lista.Empresas[indexempresas][0]:
			Index_emp = indexempresas
			break

	tela 		= Var.Lista.Empresas[Index_emp][2]

	resultado = TestaPorta(IP_rep,Porta_rep)
	

	if resultado == 1:
		for value in range(30):
			
			resultado = TestaPorta(IP_rep,Porta_rep)
			
			if resultado != 1:
				break

	if Var.Lista.Relogios[Rp_index][10] != 4:
		if Var.Lista.Relogios[Rp_index][10] == 3:
			if Var.Lista.Relogios[Rp_index][11]:
				pass #SHOW POPUP
		Var.Lista.Relogios[Rp_index][10] = resultado
		if tela == 1:
			Telas.GUI_Tela1.update(Rp_index)
		elif tela == 2: 
			Telas.GUI_Tela2.update(Rp_index)



	



def LoppTest(Thread_index):
	id_emp 		= Var.Lista.Empresas[Thread_index][0]
	tela 		= Var.Lista.Empresas[Thread_index][2]
	Quant_Rep 	= len(Var.Lista.Relogios)
	relos 		= 0
	while(True):
		for rep in range (Quant_Rep):
			if Controle.Stop : break
			if Var.Lista.Relogios[rep][1] == id_emp:
				IP_rep			= Var.Lista.Relogios[rep][3]
				Porta_rep		= Var.Lista.Relogios[rep][4]
				Var.Lista.Relogios[rep][10] = 4
				if Controle.Stop : break
				#pinta de azul
				if tela == 1:
					Telas.GUI_Tela1.update(rep)
				elif tela == 2: 
					Telas.GUI_Tela2.update(rep)

				#testa:
				if Controle.Stop : break
				Var.Lista.Relogios[rep][10] =TestaPorta(IP_rep,Porta_rep)
				relos = relos + 1
				if tela == 1:
					Telas.GUI_Tela1.update(rep)
				elif tela == 2: 
					Telas.GUI_Tela2.update(rep)
				time.sleep(2)

			if Controle.Stop : break

		if Controle.Stop : break
		DelayFunction(relos)
		relos = 0

	print "thread ",Thread_index," stopped!"
	Controle.listTheads[Thread_index] = False

