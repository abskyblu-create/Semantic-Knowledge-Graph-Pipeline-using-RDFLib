# 🚀 Semantic Knowledge Graph Pipeline using RDFLib

## 📌 Project Overview

This project demonstrates how raw data can be transformed into a **semantic knowledge graph** using **RDF (Resource Description Framework)**, enriched with **RDFS schema**, and extended through **rule-based inference**.

The goal is not just to process data, but to make it **understandable, connected, and intelligent** — enabling machines to interpret relationships and derive new knowledge.

---

## 🧠 Core Idea (Understand This First)

Traditional data (like JSON or tables) stores values.
Semantic systems store **meaning + relationships**.

👉 This project converts:

```text
Raw Data → Relationships → Meaning → Knowledge → Intelligence
```

---

## 🔁 Full Pipeline

```text
starwars4.nt        → Raw RDF triples (data)
↓
exercise2.py        → Convert into multiple formats
↓
exercise3.py        → Improve readability using prefixes
↓
schema.ttl          → Define meaning (classes + properties)
↓
exercise4.py        → Combine data + schema → semantic graph
↓
exercise5.py        → Add new relationships dynamically
↓
exercise6.py        → Apply inference rules → new knowledge
↓
final_complete_graph.rdf → Final enriched knowledge graph
```

---

## 📂 File-by-File Explanation

### 🔹 starwars4.nt

* Base dataset in **N-Triples format**
* Each line = one RDF triple

Example:

```text
(Luke, hasFriend, HanSolo)
```

---

### 🔹 exercise2.py — Format Conversion

* Loads RDF data into a graph
* Converts into:

  * Turtle (.ttl)
  * RDF/XML (.rdf)
  * JSON-LD (.json)

📌 Concept:
Same data → different representations

---

### 🔹 exercise3.py — Prefix Optimization

* Introduces namespaces (prefixes)
* Converts long URIs into readable form

Example:

```text
http://sample/Luke → ex:Luke
```

📌 Key Point:
Prefixes improve readability, **not meaning**

---

### 🔹 schema.ttl — Semantic Layer (MOST IMPORTANT)

Defines:

#### ✔ Classes

* Movie
* Creature
* Human, Jedi, Wookie (subclasses)
* Starship

#### ✔ Properties

* hasCharacter
* coPilotOf
* speed

#### ✔ Domain & Range

Defines valid relationships

Example:

```text
hasCharacter → Movie → Creature
```

📌 Meaning:
A movie has characters, and characters are creatures

---

### 🔹 exercise4.py — Schema + Data Integration

* Combines schema and data
* Enables **semantic understanding**
* Applies inference from:

  * domain
  * range
  * subclass

📌 Example:
If Luke is Human → and Human is Creature
👉 Luke is also Creature (inferred)

---

### 🔹 exercise5.py — Graph Manipulation

* Adds new relationship:

```text
HanSolo → loves → Leia
```

* Declares `loves` as RDF property

📌 Concept:
Graphs are **dynamic and extensible**

---

### 🔹 exercise6.py — Rule-Based Inference (CORE INTELLIGENCE)

Applies logic rules:

#### ✔ Symmetric Rule

```text
A friend B → B friend A
```

#### ✔ Transitive Rule

```text
A friend B, B friend C → A friend C
```

#### ✔ Inverse Rule

```text
Sister ↔ Brother
```

#### ✔ Logical Rule

```text
Father of sibling → also father
```

📌 Result:
New knowledge is created automatically

---

### 🔹 final_complete_graph.rdf

👉 Final output

* Contains:

  * Original data
  * Schema relationships
  * Inferred knowledge

📌 This is a **complete knowledge graph**

---

## 🔥 Key Concepts (MASTER THESE)

### 1. RDF (Resource Description Framework)

Represents data as:

```text
Subject → Predicate → Object
```

Example:

```text
Leia → hasFriend → HanSolo
```

---

### 2. Graph vs Table

| Relational DB | RDF Graph    |
| ------------- | ------------ |
| Tables        | Nodes        |
| Rows          | Triples      |
| Joins         | Direct links |

👉 RDF is flexible and relationship-driven

---

### 3. RDFS (Schema)

Adds meaning:

* Classes
* Properties
* Domain & Range
* Hierarchy

---

### 4. Ontology (Advanced Concept)

* More expressive than RDFS
* Defines deeper logic and constraints
* Used in real-world knowledge systems

---

### 5. Inference

👉 Deriving new knowledge from existing data

Example:

```text
Luke is Human
Human is Creature
→ Luke is Creature
```

---

### 6. Explicit vs Implicit Knowledge

| Type     | Meaning           |
| -------- | ----------------- |
| Explicit | Directly written  |
| Implicit | Derived via rules |

---

## 🧪 How to Run the Project

### Step 1: Activate environment

```powershell:

.venv\Scripts\Activate.ps1
```

### Step 2: Run all scripts

```powershell:

python exercise2.py; python exercise3.py; python exercise4.py; python exercise5.py; python exercise6.py
```

---

## ✅ Expected Outputs

* starwars4.ttl
* starwars4.rdf
* starwars4.json
* combined_graph.ttl
* final_graph.rdf
* final_complete_graph.rdf

---

## 🎯 Real-World Applications

* Google Knowledge Graph
* Recommendation systems
* Fraud detection (banking)
* Healthcare data integration
* AI reasoning systems

---

## 🏆 Final Understanding

This project teaches:

✔ Data modeling
✔ Semantic representation
✔ Knowledge graph construction
✔ Logical reasoning
✔ Data interoperability

---

## 🔥 Final One-Line Summary

👉
**“This project transforms raw data into a semantic knowledge graph using RDF, enriches it with schema, and enhances it with inference to derive intelligent relationships.”**

---

## 🚀 Note:

This project is a foundation for:

* Knowledge graphs
* AI reasoning systems
* Semantic web technologies

---
