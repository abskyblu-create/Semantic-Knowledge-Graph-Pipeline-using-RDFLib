# RDF format conversion:

from rdflib import Graph

g = Graph()

print("Loading starwars4.nt...")
g.parse("starwars4.nt", format="nt")
print(f"Loaded {len(g)} triples")

print("Creating Turtle...")
g.serialize(destination="starwars4.ttl", format="turtle")

print("Creating RDF/XML...")
g.serialize(destination="starwars4.rdf", format="xml")

print("Creating JSON-LD...")
g.serialize(destination="starwars4.json", format="json-ld")

print("Done.")
