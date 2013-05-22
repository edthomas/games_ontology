#!/usr/bin/python2
import rdflib
import rdfextras

rdfextras.registerplugins()

g = rdflib.Graph()
g.parse("../querys/ontology.rdf")

#~ results = g.query("""
#~ prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
#~ select ?aparatos
#~ where {d:damas d:temAparatos ?aparatos} 
#~ """)

def get_aparatos(jogo):
    results = g.query("""
prefix d: <http://ontokem.egc.ufsc.br/ontologia#>
select ?aparatos
where {d:"""+jogo+""" d:temAparatos ?aparatos} 
""") 
    for r in results:
        print r


get_aparatos('damas')
