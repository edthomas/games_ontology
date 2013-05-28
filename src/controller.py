import sys
from PyQt4 import QtCore, QtGui

#from debug import Debugar

from games_model import Games_Model
#from interface import Ui_GamesOntology
import interface


import rdflib
import rdfextras

class Controller(object):
	
    def __init__(self, filename="../querys/ontology.rdf"):
        self.window = interface.Ui_GamesOntology(self)
        self.window.show()
        
        
        
        rdfextras.registerplugins()
        self.g = rdflib.Graph()
        self.g.parse("../querys/ontology.rdf")
        
        self.model = Games_Model()

        
        
    def get_pergunta(self):
        inputa = self.window.lineEdit.text()
        option = str(self.window.comboBox.currentText())
        print option
        
        if option == '1':
            self.model.get_jogadores_por_partida(str(inputa), self.g)
            
        elif option == '2':
            self.model.get_regras_jogo(str(inputa), self.g)
            
        elif option == '3':        
            #self.lineEdit
            self.window.lineEdit.setEnabled(False)
            self.model.listar_competitivos(self.g)
        
        #~ elif option == '4':
            #~ 
        #~ elif option == '5':
            #~ 
        #~ elif option == '6':
            #~ 
        #~ elif option == '7':
            #~ 
        #~ elif option == '8':
            #~ 
        #~ elif option == '9':
            #~ 
        #~ elif option == '10':    
            #~ 
        #~ elif option == '11':     
            
        self.window.lineEdit.setEnabled(True)
        self.window.lineEdit.setText('')
        #self.model.get_regras_jogo(str(inputa), self.g)
        

    def load_gui(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    control = Controller()
    
    sys.exit(app.exec_())
