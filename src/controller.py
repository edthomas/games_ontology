# -*- coding: utf-8 -*-
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
        self.listapergunta = ['','Quem são os jogadores de uma determinada partida?','Quais são as regras de determinado jogo?',
        'Quais são os jogos competitivos?','Quais são os aparatos para se jogar determinado jogo?',
        'Qual o tipo de um determinado jogo?','Qual o número de jogadores de determinada partida?','Quais os objetivos de um determinado jogo?',
        'Qual o vencedor de determinada partida?','Quem venceu mais partidas?','Quais as partidas de um determinado jogo.']
        
        self.model = Games_Model()

        
        
    def get_pergunta(self):
        inputa = self.window.lineEdit.text()
        option = str(self.window.comboBox.currentText())
           
        
        print option
        
        #~ if self.window.comboBox.currentIndexChanged() != -1 :
            #~ print 'lkjlkjklj'
        if option == '1':
            #~ self.window.label.setText(self.listapergunta[1])
            self.model.get_jogadores_por_partida(str(inputa), self.g)
            
        elif option == '2':
            self.model.get_regras_jogo(str(inputa), self.g)
            
        elif option == '3':        
            #self.lineEdit
            self.window.lineEdit.setEnabled(False)
            self.model.listar_competitivos(self.g)
        
        elif option == '4':
            self.model.get_aparatos(str(inputa), self.g)
            
        elif option == '5':
            self.model.get_nome_jogo(str(inputa), self.g)
            
        elif option == '6':
            self.model.get_num_jogadores_partida(str(inputa), self.g)
            
        elif option == '7':
            self.model.get_objetivos_jogo(str(inputa), self.g)
            
        elif option == '8':
            self.model.get_vencedor_partida(str(inputa), self.g)
            
        elif option == '9':
            self.model.get_maior_vencedor(self.g)
            
        elif option == '10':    
            self.model.get_partidas_jogo(str(inputa), self.g)
            
        self.window.lineEdit.setEnabled(True)
        self.window.lineEdit.setText('')
        #self.model.get_regras_jogo(str(inputa), self.g)
        

    def load_gui(self):
        pass
    
    def change_text(self):
        option = str(self.window.comboBox.currentText())
        if option == '1':
            self.window.label.setText(self.listapergunta[1])
        if option == '2':
            self.window.label.setText(self.listapergunta[2])
        if option == '3':
            self.window.label.setText(self.listapergunta[3])
        if option == '4':
            self.window.label.setText(self.listapergunta[4])
        if option == '5':
            self.window.label.setText(self.listapergunta[5])
        if option == '6':
            self.window.label.setText(self.listapergunta[6])
        if option == '7':
            self.window.label.setText(self.listapergunta[7])
        if option == '8':
            self.window.label.setText(self.listapergunta[8])
        if option == '9':
            self.window.label.setText(self.listapergunta[9])
        if option == '10':
            self.window.label.setText(self.listapergunta[10])

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    control = Controller()
    
    sys.exit(app.exec_())
