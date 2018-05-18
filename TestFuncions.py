import socket
import os
import shutil
import threading
import time

from Classes import *
from VariaveisGlobais import * 


def DelayFunction(qntd_relos):
	if qntd_relos < 3:
		time.sleep(120)
	elif qntd_relos < 7:
		time.sleep(60)

	time.sleep(30)



def TestaPorta(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#print ip + " porta = " + port
	#print "Test Ping"
	if TestaPing(ip):

		try:
			s.connect((ip,int(port)))		
			s.close()
			return 3

		except:
			return 2

	else:
		return 1

def TestaPing(ip):
	resposta = os.system("ping " + ip + " -c 4 > logping.txt")
	if resposta == 0 :
		#print "ping ok"
		return True
	else:
		#print "Falha ping"
		return False


def CriaTreads():
	Quant_Empresas = len(Var.Lista.Empresas)
	for indexempresas in range (Quant_Empresas):
			t = threading.Thread(target=LoppTest,kwargs={'Thread_index':indexempresas})
			t.start()
			print "Criado!", indexempresas
	



def LoppTest(Thread_index):
	id_emp 		= Var.Lista.Empresas[Thread_index][0]
	tela 		= Var.Lista.Empresas[Thread_index][2]
	Quant_Rep 	= len(Var.Lista.Relogios)
	relos 		= 0
	while(True):
		for rep in range (Quant_Rep):
			if Var.Lista.Relogios[rep][1] == id_emp:
				IP_rep			= Var.Lista.Relogios[rep][3]
				Porta_rep		= Var.Lista.Relogios[rep][4]
				Var.Lista.Relogios[rep][10] = 4
				#pinta de azul
				if tela == 1:
					Telas.GUI_Tela1.update(rep)
				elif tela == 2: 
					Telas.GUI_Tela2.update(rep)

				#testa:
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






			
def AtualizaCor(empresa,relogio,result):
	if result == 1:
		Var.Lista1.Cor[empresa][relogio][0] 	= "firebrick1"
		Var.Lista1.Cor[empresa][relogio][1]  	= "firebrick1"
	elif result == 2:
		Var.Lista1.Cor[empresa][relogio][0]   	= "green3"
		Var.Lista1.Cor[empresa][relogio][1] 	= "chocolate1"
		Var.Lista1.Atencao[empresa]				= "red"
		Var.Lista1.Cor[empresa][relogio][2]		= True
	elif result == 3:
		Var.Lista1.Cor[empresa][relogio][0]   	= "green3"
		Var.Lista1.Cor[empresa][relogio][1]	 	= "green3"
		Var.Lista1.Cor[empresa][relogio][2]		= False
	elif result == 4:
		Var.Lista1.Cor[empresa][relogio][0]   	= "cyan"
		#Var.Lista1.Cor[empresa][relogio][1] 	= "cyan"
		#Var.Lista1.Cor[empresa][relogio][2]		= "green3"
	else:
		Var.Lista1.Cor[empresa][relogio][0]   	= "pink"
		Var.Lista1.Cor[empresa][relogio][1] 	= "pink"

	Telas.GUI_Tela1 .update(empresa,relogio)

def AtualizaCor2(empresa,relogio,result):
	if result == 1:
		Var.Lista2.Cor[empresa][relogio][0] 	= "firebrick1"
		Var.Lista2.Cor[empresa][relogio][1]  	= "firebrick1"
	elif result == 2:
		Var.Lista2.Cor[empresa][relogio][0]   	= "green3"
		Var.Lista2.Cor[empresa][relogio][1] 	= "chocolate1"
		Var.Lista2.Atencao[empresa]				= "red"
		Var.Lista2.Cor[empresa][relogio][2]		= True
	elif result == 3:
		Var.Lista2.Cor[empresa][relogio][0]   	= "green3"
		Var.Lista2.Cor[empresa][relogio][1]	 	= "green3"
		Var.Lista2.Cor[empresa][relogio][2]		= False
	elif result == 4:
		Var.Lista2.Cor[empresa][relogio][0]   	= "cyan"
		#Var.Lista2.Cor[empresa][relogio][1] 	= "cyan"
		#Var.Lista2.Cor[empresa][relogio][2]		= "green3"
	else:
		Var.Lista2.Cor[empresa][relogio][0]   	= "pink"
		Var.Lista2.Cor[empresa][relogio][1] 	= "pink"

	Telas.GUI_Tela2 .update(empresa,relogio)





def TestRoutine2(indexempresas_lido):
	while(1):
		Var.Lista2.Hora[indexempresas_lido] = GetTime().horaminuto()
		Telas.GUI_Tela2 .updateHora(indexempresas_lido)
		for indexrelogios in range (len(Var.Lista2.relogios[indexempresas_lido])):
			IP  	= Var.Lista2.relogios[indexempresas_lido][indexrelogios][3]
			Porta 	= Var.Lista2.relogios[indexempresas_lido][indexrelogios][4]
			testa = 4
			AtualizaCor2(indexempresas_lido,indexrelogios,int(testa))
			testa = TestaPorta(IP,Porta)
			AtualizaCor2(indexempresas_lido,indexrelogios,int(testa))
			Var.Lista2.ON[indexempresas_lido] = 0
			FlagCount2 = False
			for indexrelogios2 in range (len(Var.Lista2.relogios[indexempresas_lido])):
				if Var.Lista2.Cor[indexempresas_lido][indexrelogios2][1]	 	== "green3":
					Var.Lista2.ON[indexempresas_lido] = Var.Lista2.ON[indexempresas_lido] + 1

					if Controle.Stop : break

					if Var.Lista2.Cor[indexempresas_lido][indexrelogios2][2]:
						 FlagCount2= True

			Telas.GUI_Tela2.updateContage(indexempresas_lido)
			Telas.GUI_Monitor.UpdateContage2(indexempresas_lido)
			if FlagCount2:
				Var.Lista2.Atencao[indexempresas_lido] = "green3"

			if Controle.Stop : break
		if Controle.Stop : break
		DelayFunction(indexempresas_lido)
		if Controle.Stop : break


def TestRoutine1(indexempresas_lido):
	while(1):
		Var.Lista1.Hora[indexempresas_lido] = GetTime().horaminuto()
		Telas.GUI_Tela1 .updateHora(indexempresas_lido)
		for indexrelogios in range (len(Var.Lista1.relogios[indexempresas_lido])):
			IP  	= Var.Lista1.relogios[indexempresas_lido][indexrelogios][3]
			Porta 	= Var.Lista1.relogios[indexempresas_lido][indexrelogios][4]
			testa = 4
			AtualizaCor(indexempresas_lido,indexrelogios,int(testa))
			testa = TestaPorta(IP,Porta)
			AtualizaCor(indexempresas_lido,indexrelogios,int(testa))
			Var.Lista1.ON[indexempresas_lido] = 0
			FlagCount = False
			for indexrelogios2 in range (len(Var.Lista1.relogios[indexempresas_lido])):
				if Var.Lista1.Cor[indexempresas_lido][indexrelogios2][1]	 	== "green3":
					Var.Lista1.ON[indexempresas_lido] = Var.Lista1.ON[indexempresas_lido] + 1

					if Controle.Stop : break

					if Var.Lista1.Cor[indexempresas_lido][indexrelogios2][2]:
						 FlagCount= True

			Telas.GUI_Tela1.updateContage(indexempresas_lido)
			Telas.GUI_Monitor.UpdateContage1(indexempresas_lido)
			if FlagCount:
				Var.Lista1.Atencao[indexempresas_lido] = "green3"

			if Controle.Stop : break
		if Controle.Stop : break
		DelayFunction(indexempresas_lido)
		if Controle.Stop : break

