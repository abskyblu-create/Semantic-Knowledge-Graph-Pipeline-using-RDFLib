# rule-based reasoning:


from rdflib import Graph, URIRef

g = Graph()
g.parse("schema.ttl", format="turtle")
g.parse("starwars4.ttl", format="turtle")

hasFriend = URIRef("http://sample/prop/hasFriend")
hasEnemy = URIRef("http://sample/prop/hasEnemy")
hasSister = URIRef("http://sample/prop/hasSister")
hasBrother = URIRef("http://sample/prop/hasBrother")
isFatherOf = URIRef("http://sample/prop/isFatherOf")

inferred = []

for s, p, o in list(g.triples((None, hasFriend, None))):
    if (o, hasFriend, s) not in g:
        g.add((o, hasFriend, s))
        inferred.append((o, hasFriend, s))

friends = list(g.triples((None, hasFriend, None)))
for a, _, b in friends:
    for x, _, c in friends:
        if b == x and a != c and (a, hasFriend, c) not in g:
            g.add((a, hasFriend, c))
            inferred.append((a, hasFriend, c))

for s, _, o in list(g.triples((None, hasSister, None))):
    if (o, hasBrother, s) not in g:
        g.add((o, hasBrother, s))
        inferred.append((o, hasBrother, s))

for s, _, o in list(g.triples((None, hasBrother, None))):
    if (o, hasSister, s) not in g:
        g.add((o, hasSister, s))
        inferred.append((o, hasSister, s))

for a, _, b in list(g.triples((None, hasFriend, None))):
    for x, _, c in list(g.triples((None, hasEnemy, None))):
        if b == x and (a, hasEnemy, c) not in g:
            g.add((a, hasEnemy, c))
            inferred.append((a, hasEnemy, c))

for a, _, sib in list(g.triples((None, hasBrother, None))):
    for father, _, child in list(g.triples((None, isFatherOf, None))):
        if sib == child and (father, isFatherOf, a) not in g:
            g.add((father, isFatherOf, a))
            inferred.append((father, isFatherOf, a))

for a, _, sib in list(g.triples((None, hasSister, None))):
    for father, _, child in list(g.triples((None, isFatherOf, None))):
        if sib == child and (father, isFatherOf, a) not in g:
            g.add((father, isFatherOf, a))
            inferred.append((father, isFatherOf, a))

print("Three inferred triples:")
for t in inferred[:3]:
    print(t)

g.serialize(destination="final_complete_graph.rdf", format="xml")
print("Saved final_complete_graph.rdf")
