# -*- encoding: utf-8 -*-
from Model import Model

import rdflib
import rdfextras


class Games_Model(object):
    
    
    def get_jogadores_por_partida(self, partida):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?jogadores ?nome
        where {d:partida_cacheta d:temJogadores ?jogadores.
        ?jogadores d:temNome ?nome}
        """)
    
        return result
        
    def get_regras_jogo(self, jogo):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?regras
        where {d:damas d:temRegras ?regras} 
        """)
        
        return result
        
        
    def listar_competitivos(self):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select  ?j ?r
        where
        {
        ?classes rdfs:subClassOf d:Jogos.
        ?j  rdf:type   ?classes.
        ?j d:ehCompetitivo true
        }""")
        
        return result
        
    
    def get_aparatos(self, jogo):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?aparatos
        where {d:jogo d:temAparatos ?aparatos} 
        """) 
        
        return result
    
    def get_nome_jogo(self):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?nome
        where {d:damas d:temNome ?nome}
        select ?nome
        where {d:damas d:temNome ?nome}""")
        
        return result
    


		
		
		
		
