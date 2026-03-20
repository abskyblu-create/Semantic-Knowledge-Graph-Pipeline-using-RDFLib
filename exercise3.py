from rdflib import Graph, Namespace

g = Graph()

EX = Namespace("http://sample/")
PROP = Namespace("http://sample/prop/")

g.bind("ex", EX)
g.bind("prop", PROP)

print("Loading starwars4.ttl...")
g.parse("starwars4.ttl", format="turtle")

print("Saving Turtle with prefixes...")
g.serialize(destination="starwars4_with_prefixes.ttl", format="turtle")

print("Done.")
