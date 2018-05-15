# -*- coding: utf-8 -*-
from VariaveisGlobais import * 


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
	


		

		

	