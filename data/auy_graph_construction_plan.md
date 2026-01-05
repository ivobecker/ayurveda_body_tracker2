(:Prakriti { type })
(:TraitType { name, category })
(:TraitValue { value })
(:User { id })
(:UserResponse { score })   // optional, for weighting


(:Prakriti)-[:HAS_TRAIT]->(:TraitValue)
(:TraitValue)-[:OF_TYPE]->(:TraitType)

(:User)-[:HAS_RESPONSE]->(:TraitValue)


["thin", "variable", "restless", "dry"]


# Kern-Domänen (Node Types) #


### Mensch & Konstitution
Person
Prakriti
Vikriti
Dosha

(Person)-[:HAS_PRAKRITI]->(Prakriti)
(Person)-[:HAS_VIKRITI]->(Vikriti)
(Person)-[:HAS_SYMPTOM]->(Symptom)

(Prakriti)-[:DOMINATED_BY {weight}]->(Dosha)
(Vikriti)-[:IMBALANCED_BY {severity}]->(Dosha)

### Substanzen & Ernährung
Ingredient
Recipe
DietPlan


### Ayurvedische Prinzipien
Rasa     (Geschmack)
Guna     (Eigenschaft)
Virya    (Energie)
Vipaka   (Verdauungseffekt)
Karma    (therapeutische Wirkung)   

(Ingredient)-[:HAS_RASA]->(Rasa)
(Ingredient)-[:HAS_GUNA]->(Guna)
(Ingredient)-[:HAS_VIRYA]->(Virya)
(Ingredient)-[:HAS_VIPAKA]->(Vipaka)
(Ingredient)-[:HAS_KARMA]->(Karma)

(Rasa)-[:BALANCES]->(Dosha)
(Rasa)-[:AGGRAVATES]->(Dosha)

(Guna)-[:BALANCES]->(Dosha)
(Guna)-[:AGGRAVATES]->(Dosha)

(Virya)-[:BALANCES]->(Dosha)
(Vipaka)-[:AFFECTS]->(Dosha)

### Gesundheit und Therapie
Symptom
Disease
Therapy
BodySystem

(Recipe)-[:CONTAINS]->(Ingredient)
(Therapy)-[:USES]->(Ingredient)
(Therapy)-[:TARGETS]->(Dosha)

## Textuelles UML-Modell
Person
 ├─ HAS_PRAKRITI → Prakriti
 │                 └─ DOMINATED_BY → Dosha
 ├─ HAS_VIKRITI → Vikriti
 │                 └─ IMBALANCED_BY → Dosha
 └─ HAS_SYMPTOM → Symptom

Ingredient
 ├─ HAS_RASA → Rasa
 │             ├─ BALANCES → Dosha
 │             └─ AGGRAVATES → Dosha
 ├─ HAS_GUNA → Guna
 ├─ HAS_VIRYA → Virya
 ├─ HAS_VIPAKA → Vipaka
 └─ HAS_KARMA → Karma

Therapy
 ├─ USES → Ingredient
 └─ TARGETS → Dosha



## Cypher: Match User to Prakriti
MATCH (u:User {id: $user_id})-[:HAS_RESPONSE]->(tv:TraitValue)
MATCH (p:Prakriti)-[:HAS_TRAIT]->(tv)
RETURN p.type AS prakriti, COUNT(tv) AS score
ORDER BY score DESC;


| Prakriti | TraitType  | TraitValue |
| -------- | ---------- | ---------- |
| Vata     | body_frame | thin       |
| Vata     | metabolism | variable   |
| Pitta    | metabolism | strong     |
| Kapha    | metabolism | slow       |
