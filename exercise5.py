# graph manipulation:


from rdflib import Graph, URIRef, RDF

g = Graph()

g.parse("schema.ttl", format="turtle")
g.parse("starwars4.ttl", format="turtle")

han = URIRef("http://sample/HanSolo")
leia = URIRef("http://sample/Leia")
loves = URIRef("http://sample/prop/loves")

g.add((han, loves, leia))
g.add((loves, RDF.type, RDF.Property))

g.serialize(destination="final_graph.rdf", format="xml")

print("Saved final_graph.rdf")
