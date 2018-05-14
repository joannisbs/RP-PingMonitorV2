from datetime import datetime


class GetTime(object):
	
	def __init__(self):
		now = datetime.now()
		self.hora = now.hour
		self.minuto = now.minute
		self.segundo = now.second

	def horaminuto(self):
		
		horaminuto = 	(str(self.hora).zfill(2) +":"+ 
						str(self.minuto).zfill(2) ) 
						
		return horaminuto
