// Prakriti
LOAD CSV WITH HEADERS FROM 'file:///prakriti.csv' AS row
CREATE (:Prakriti {type: row.type});

// Trait Types
LOAD CSV WITH HEADERS FROM 'file:///trait_types.csv' AS row
CREATE (:TraitType {name: row.name, category: row.category});

// Trait Values
LOAD CSV WITH HEADERS FROM 'file:///trait_values.csv' AS row
MATCH (tt:TraitType {name: row.type})
CREATE (tv:TraitValue {value: row.value})
CREATE (tv)-[:OF_TYPE]->(tt);

// Prakriti → TraitValue
LOAD CSV WITH HEADERS FROM 'file:///prakriti_traits.csv' AS row
MATCH (p:Prakriti {type: row.prakriti})
MATCH (tv:TraitValue {value: row.value})
CREATE (p)-[:HAS_TRAIT]->(tv);
