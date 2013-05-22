# -*- encoding: utf-8 -*-
from Model import Model

import rdflib
import rdfextras


class Games_Model(object):
    
    
    def get_jogadores_por_partida(self, partida):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?jogadores ?nome
        where {d:"""+partida+"""+d:temJogadores ?jogadores.
        ?jogadores d:temNome ?nome}
        """)
    
        return result
        
    def get_regras_jogo(self, jogo):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?regras
        where {d:"""+jogo+"""d:temRegras ?regras} 
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
        where {d:"""+jogo+""" d:temAparatos ?aparatos} 
        """) 
        
        return result
    
    def get_nome_jogo(self, jogo):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?nome
        where {d:"""+jogo+""" d:temNome ?nome}
        """)
        
        return result
    
    def get_num_jogadores_partida(self, partida):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select (count(?jogadores) as ?count)
        where {d:"""+partida+""" d:temJogadores ?jogadores} 
        """)
        
        return result
        
        
    def get_objetivos_jogo(self, jogo):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?objetivos
        where {d:"""+jogo+""" d:temObjetivos ?objetivos} 
        """)
        
        return result
        
        
    def get_vencedor_partida(self, partida):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        where {d:"""+partida"""+ d:temVencedor ?vencedor.
        ?vencedor d:temNome ?nome} 
        """)
        
        
    def get_maior_vencedor(self, nome_jogador):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select  ?j
        where {
        ?p a ?Partida.
        ?p d:temVencedor ?j.
        ?j d:temNome """+nome_jogador+""".}
        """)
        
        return result

    def get_partidas_jogo(self, nome_jogo):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select  ?p
        where {
        ?p a ?Partida.
        ?p d:temJogo ?j.
        ?j d:temNome """+nome_jogo+""".}
        """)
        
        return result
        
        
    
		
		
		
		
