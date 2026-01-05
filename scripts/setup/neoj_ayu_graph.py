from neo4j import GraphDatabase


doshas = ["Vata", "Pitta", "Kapha"]

rasas = ["süß", "sauer", "salzig", "scharf", "bitter", "herb"]
gunas = ["leicht", "schwer", "ölig", "trocken", "heiß", "kalt"]
viryas = ["heiß", "kühl"]
vipakas = ["süß", "sauer", "scharf"]

ingredients = [
    {
        "name": "Ingwer",
        "rasa": ["scharf"],
        "guna": ["leicht", "heiß"],
        "virya": "heiß",
        "vipaka": "scharf",
        "balances": {"Vata": 0.9, "Kapha": 0.8},
        "aggravates": {"Pitta": 0.7},
        "karma": ["verdauungsfördernd", "wärmend"]
    }
]




driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "evil-pilate-roughly")
)

def setup_ayurveda_graph(tx, data):
    # Doshas
    tx.run("""
        UNWIND $doshas AS d
        MERGE (:Dosha {name: d})
    """, doshas=doshas)



    # Ayurveda Konzepte
    tx.run("""
        UNWIND $rasas AS r MERGE (:Rasa {name: r});
        UNWIND $gunas AS g MERGE (:Guna {name: g});
        UNWIND $viryas AS v MERGE (:Virya {name: v});
        UNWIND $vipakas AS v MERGE (:Vipaka {name: v});
    """, rasas=rasas, gunas=gunas, viryas=viryas, vipakas=vipakas)

    # Ingredients
    for ing in ingredients:
        tx.run("""
            MERGE (i:Ingredient {name: $name})
        """, name=ing["name"])

        for rasa in ing["rasa"]:
            tx.run("""
                MATCH (i:Ingredient {name: $iname})
                MATCH (r:Rasa {name: $rname})
                MERGE (i)-[:HAS_RASA]->(r)
            """, iname=ing["name"], rname=rasa)

        for guna in ing["guna"]:
            tx.run("""
                MATCH (i:Ingredient {name: $iname})
                MATCH (g:Guna {name: $gname})
                MERGE (i)-[:HAS_GUNA]->(g)
            """, iname=ing["name"], gname=guna)

        tx.run("""
            MATCH (i:Ingredient {name: $iname})
            MATCH (v:Virya {name: $vname})
            MERGE (i)-[:HAS_VIRYA]->(v)
        """, iname=ing["name"], vname=ing["virya"])

        tx.run("""
            MATCH (i:Ingredient {name: $iname})
            MATCH (v:Vipaka {name: $vname})
            MERGE (i)-[:HAS_VIPAKA]->(v)
        """, iname=ing["name"], vname=ing["vipaka"])

        for d, strength in ing["balances"].items():
            tx.run("""
                MATCH (i:Ingredient {name: $iname})
                MATCH (d:Dosha {name: $dname})
                MERGE (i)-[:BALANCES {strength: $s}]->(d)
            """, iname=ing["name"], dname=d, s=strength)

        for d, strength in ing["aggravates"].items():
            tx.run("""
                MATCH (i:Ingredient {name: $iname})
                MATCH (d:Dosha {name: $dname})
                MERGE (i)-[:AGGRAVATES {strength: $s}]->(d)
            """, iname=ing["name"], dname=d, s=strength)


#print (setup_ayurveda_graph,ingredients)

with driver.session() as session:
 session.write_transaction(setup_ayurveda_graph, ingredients)
driver.close()
