
import sys
from PyQt4 import QtCore, QtGui
from cd import Cd
from interface import Ui_Mostrador_de_CDs
from debug import Debugar


import rdflib
import rdfextras

class Controller(object):
	
	@Debugar
	def __init__(self, filename="ontology.rdf"):
        
        rdfextras.registerplugins()
        
        g = rdflib.Graph()
        g.parse(filename)
        
		self.bd_cd = Cd()
		self.bd_cd.createDatabase()
		
		self.app = QtGui.QApplication(sys.argv)
		self.Mostrador_de_CDs = QtGui.QMainWindow()
		self.view = Ui_Mostrador_de_CDs()
		self.load_gui()
        
        
        
	
	@Debugar
	def load_gui(self):
		self.view.setupUi(self.Mostrador_de_CDs, self)
		cds = self.bd_cd.select_all()
		self.view.show_all(cds)
		self.Mostrador_de_CDs.show()
		sys.exit(self.app.exec_())

	def insert(self):
		cd = self.view.get_insert()
		
		if cd.is_valid():
			self.bd_cd.save(cd)

			self.view.show_all(self.bd_cd.select_all())
	
	def remove(self):
		id_ = self.view.get_remove()
		if id_ != '':
			self.bd_cd.delete(int(id_))
			
			cds = self.bd_cd.select_all()
			
			self.view.show_all(cds)


if __name__ == "__main__":
	import sys
	cont = Controller()
	cont.load_gui()
