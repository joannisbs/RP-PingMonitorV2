from Tkinter import *
from VariaveisGlobais import * 
import ttk

def PopupRel(id_rep):

	def on_check_clik():
		Var.Lista.Relogios[id_rep][11] = True
		show.destroy()

		



	show = Tk()
	show.wm_title("Relogio")

	id_emp 			= Var.Lista.Relogios[id_rep][1]
	Name_rep		= Var.Lista.Relogios[id_rep][2]
	IP_rep			= Var.Lista.Relogios[id_rep][3]
	Porta_rep		= Var.Lista.Relogios[id_rep][4]
	Modelo_rep		= Var.Lista.Relogios[id_rep][5]
	Numero_rep		= Var.Lista.Relogios[id_rep][6]
	#Stado			= Var.Lista.Relogios[id_rep][7]
	#Hora			= Var.Lista.Relogios[id_rep][8]
	Quant_Empresas = len(Var.Lista.Empresas)
	for indexempresas in range (Quant_Empresas):
		if id_emp == Var.Lista.Empresas[indexempresas][0]:
			Index_emp = indexempresas
			break

	name_emp		= Var.Lista.Empresas[Index_emp][1]

	lable1 = Label(show, text = "Empresa: "  + name_emp)
	lable1.grid(row=0,pady=5,padx=20)

	lable1 = Label(show, text = "Unidade: "  + Name_rep)
	lable1.grid(row=1,pady=5,padx=20)

	lable = Label(show, text = "IP: " + IP_rep)
	lable.grid(row=2,pady=5,padx=20)

	#lable2 = Label(show, text = "Porta Testada: "  + Porta_rep)
	#lable2.grid(row=3,pady=5,padx=20)

	#lable3 = Label(show, text = "Numero do Rep: " + Numero_rep)
	#lable3.grid(row=4,pady=5,padx=20)
	var = IntVar()
	Checkbutton(show,text="Deseja abrir Popup ao ficar On-Line?",variable=var,command=on_check_clik).grid(row=5)


	botaos = Button(show, text="Ok", command=show.destroy)
	botaos.grid(row=6,pady=5,padx=20)

def PopupRep():

	def ok():

		name = var2.get()
		#print name

		for item in  range (len(Var.Lista.Relogios)):
			if Var.Lista.Relogios[item][2]==name:
				id_rep = Var.Lista.Relogios[item][0]

		Controle.db.get_history(id_rep)

	def selct():
		name = var.get()
		listrep = []
		for item in  range (len(Var.Lista.Empresas)):
			if Var.Lista.Empresas[item][1]==name:
				ids =  Var.Lista.Empresas[item][0]

		for item in  range (len(Var.Lista.Relogios)):
			if Var.Lista.Relogios[item][1]==ids:
				listrep.append(Var.Lista.Relogios[item][2])

		option2['values']=listrep

	def selct2():
		name = var2.get()
		print name

	show = Tk()
	show.wm_title("Historico Rep")

	var = StringVar(show)
	var.set('RP TESTE')
	var2 = StringVar(show)
	var2.set('RP TESTE')
	listemp = []
	for item in  range (len(Var.Lista.Empresas)):
		listemp.append(Var.Lista.Empresas[item][1])

	option = ttk.Combobox( show,textvariable = var, values = listemp)
	option.bind("<<ComboboxSelected>>",lambda event:selct())
	option.pack()

	option2 = ttk.Combobox( show,textvariable = var2, values = listemp)
	option2.bind("<<ComboboxSelected>>",lambda event:selct2())
	option2.pack()


	botaos = Button(show, text="Ok", command=ok)
	botaos.pack()


