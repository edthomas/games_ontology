# -*- coding: utf-8 -*-
#from Model import Model

import rdflib
import rdfextras


class Games_Model(object):
    
    
    def get_jogadores_por_partida(self, partida, g):
        result = g.query("""
prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
select ?jogadores ?nome
where {d:"""+partida+""" d:temJogadores ?jogadores.
       ?jogadores d:temNome ?nome}
""")    
        self.print_resultis(result)     
        return result
        
    def get_regras_jogo(self, jogo, g):
        results = g.query("""
prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
select ?regras
where {d:"""+jogo+""" d:temRegras ?regras}
""") 
        self.print_resultis(results)     
        return results
        
        
    def listar_competitivos(self, g):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select  ?j
        where
        {
        ?classes rdfs:subClassOf d:Jogos.
        ?j  rdf:type   ?classes.
        ?j d:ehCompetitivo true
        }""")
        
        self.print_resultis(result)     
        return result
        
    
    def get_aparatos(self, jogo, g):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?aparatos
        where {d:"""+jogo+""" d:temAparatos ?aparatos} 
        """) 
        
        self.print_resultis(result)     
        return result
    
    def get_nome_jogo(self, jogo, g):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?nome
        where {d:"""+jogo+""" d:temNome ?nome}
        """)
        
        self.print_resultis(result)     
        return result
    
    def get_num_jogadores_partida(self, partida, g):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?jogadores
        where {d:"""+partida+""" d:temJogadores ?jogadores} 
        """) 
        #self.print_resultis(result)
        print len(result)     
        return len(result)
        
        
    def get_objetivos_jogo(self, jogo, g):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?objetivos
        where {d:"""+jogo+""" d:temObjetivos ?objetivos} 
        """)
        
        self.print_resultis(result)     
        return result
        
        
    def get_vencedor_partida(self, partida, g):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select ?nome
        where {d:"""+partida+""" d:temVencedor ?vencedor.
        ?vencedor d:temNome ?nome} 
        """)
        
        self.print_resultis(result)     
        return result
        
    def get_maior_vencedor(self, g):
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select  ?j
        where {
        ?p a ?Partida.
        ?p d:temVencedor ?j.
        ?j d:temNome ?nome.}
        """)
        
        self.print_resultis(result)     
        return result

    def get_partidas_jogo(self, jogo, g):
        #~ result = g.query("""
#~ prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
#~ select  ?p
#~ where {
#~ ?p a ?Partida.
#~ ?p d:temJogo ?j.
#~ ?j d:temNome """+nome_jogo+""".}
#~ """)
        result = g.query("""
        prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
        select  ?p
        where {
        ?p a ?Partida.
        ?p d:temJogo ?j.
        ?j d:temNome "jogo de xadrez".}
        """)
        
        self.print_resultis(result)     
        return result
        
    def print_resultis(self,r):
        #~ print r(0).toPython()
        for item in r:
            print item[0].toPython()
    
    
		
		
		
