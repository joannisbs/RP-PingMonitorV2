import socket
import os
import shutil
import threading
import time


from VariaveisGlobais import * 


def DelayFunction():
	pass

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
	Quant_Empresas = len(Var.Lista1.empresas)
	for indexempresas in range (Quant_Empresas):
			t = threading.Thread(target=TestRoutine,kwargs={'indexempresas_lido':indexempresas})
			t.start()

			
def AtualizaCor(empresa,relogio,result):
	if result == 1:
		Var.Lista1.Cor[empresa][relogio][0] 	 	= "firebrick1"
		Var.Lista1.Cor[empresa][relogio][1]  	= "firebrick1"
	elif result == 2:
		Var.Lista1.Cor[empresa][relogio][0]   	= "green3"
		Var.Lista1.Cor[empresa][relogio][1] 		= "chocolate1"
	elif result == 3:
		Var.Lista1.Cor[empresa][relogio][0]   	= "green3"
		Var.Lista1.Cor[empresa][relogio][1]	 	= "green3"
	elif result == 4:
		Var.Lista1.Cor[empresa][relogio][0]   	= "cyan"
		Var.Lista1.Cor[empresa][relogio][1] 		= "cyan"
	else:
		Var.Lista1.Cor[empresa][relogio][0]   	= "pink"
		Var.Lista1.Cor[empresa][relogio][1] 		= "pink"

	Telas.GUI_Tela1 .update(empresa,relogio)



def TestRoutine(indexempresas_lido):
	while(1):

		for indexrelogios in range (len(Var.Lista1.relogios[indexempresas_lido])):
			IP  	= Var.Lista1.relogios[indexempresas_lido][indexrelogios][3]
			Porta 	= Var.Lista1.relogios[indexempresas_lido][indexrelogios][4]
			testa = 4
			AtualizaCor(indexempresas_lido,indexrelogios,int(testa))
			testa = TestaPorta(IP,Porta)
			AtualizaCor(indexempresas_lido,indexrelogios,int(testa))
			if Controle.Stop : break
		if Controle.Stop : break
		DelayFunction()
		if Controle.Stop : break
