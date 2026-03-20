# schema + inference: 

from rdflib import Graph, RDF, RDFS

g = Graph()

print("Loading schema.ttl...")
g.parse("schema.ttl", format="turtle")

print("Loading starwars4.ttl...")
g.parse("starwars4.ttl", format="turtle")

print(f"Combined graph has {len(g)} triples\n")

inferred = set()

for s, p, o in g:
    for _, _, domain_class in g.triples((p, RDFS.domain, None)):
        if (s, RDF.type, domain_class) not in g:
            inferred.add((s, RDF.type, domain_class))

    for _, _, range_class in g.triples((p, RDFS.range, None)):
        if str(range_class) != str(RDFS.Literal) and (o, RDF.type, range_class) not in g:
            inferred.add((o, RDF.type, range_class))

for s, _, c in g.triples((None, RDF.type, None)):
    for _, _, super_c in g.triples((c, RDFS.subClassOf, None)):
        if (s, RDF.type, super_c) not in g:
            inferred.add((s, RDF.type, super_c))

print("Inferred rdf:type statements:")
for triple in inferred:
    print(triple)

g.serialize(destination="combined_graph.ttl", format="turtle")
print("\nSaved combined_graph.ttl")
