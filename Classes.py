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
		
		time = str(self.minuto).zfill(2)			
		return time

	def sohora(self):
		
		time = str(self.hora).zfill(2)			
		return time

	def sosegundo(self):
		
		time = str(self.segundo).zfill(2)			
		return time

	def completa(self):
		date = (str(self.year).zfill(4)+"_"+
				str(self.mes).zfill(2)+"_"+
				str(self.day).zfill(2)+"-"+
				str(self.hora).zfill(2)+"-"+
				str(self.minuto).zfill(2))
		return date

	def completedb(self):
		#[18_06_04]10h12
		date = ("["+str(self.year)[2]+
					str(self.year)[3]+"_"+
				str(self.mes).zfill(2)+"_"+
				str(self.day).zfill(2)+"]"+
				str(self.hora).zfill(2)+"h"+
				str(self.minuto).zfill(2))
		return date



	def comp_dia(self):
		date = (str(self.mes).zfill(2)+"/"+
				str(self.day).zfill(2)+"-"+
				str(self.hora).zfill(2)+":"+
				str(self.minuto).zfill(2))
		return date
