from datetime import datetime

class GetTime(object):
	
	def __init__(self):
		now = datetime.now()
		self.hora = now.hour
		self.minuto = now.minute
		self.segundo = now.second
		self.day	=	now.day
		self.mes	=	now.month
		self.year	=	now.year

	def horaminuto(self):
		
		horaminuto = 	(str(self.hora).zfill(2) +":"+ 
						str(self.minuto).zfill(2) ) 
						
		return horaminuto

	def sominuto(self):
		
		minutos = str(self.minuto).zfill(2)			
		return minutos

	def sohora(self):
		
		sohora = str(self.hora).zfill(2)			
		return sohora

	def completa(self):
		date = (str(self.year).zfill(4)+"_"+
				str(self.mes).zfill(2)+"_"+
				str(self.day).zfill(2)+"-"+
				str(self.hora).zfill(2)+"-"+
				str(self.minuto).zfill(2))
		return date
	

