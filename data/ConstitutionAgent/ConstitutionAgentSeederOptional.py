from neo4j import GraphDatabase

class PrakritiSeeder:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def seed(self):
        with self.driver.session() as session:
            session.run("""
            UNWIND ['Vata','Pitta','Kapha'] AS p
            CREATE (:Prakriti {type: p})
            """)

            session.run("""
            UNWIND [
              {name:'body_frame', category:'physical'},
              {name:'metabolism', category:'digestive'},
              {name:'appetite', category:'digestive'},
              {name:'skin', category:'physical'},
              {name:'mind', category:'mental'}
            ] AS tt
            CREATE (:TraitType tt)
            """)

            session.run("""
            UNWIND [
              ['thin','body_frame'], ['medium','body_frame'], ['large','body_frame'],
              ['variable','metabolism'], ['strong','metabolism'], ['slow','metabolism'],
              ['irregular','appetite'], ['intense','appetite'], ['stable','appetite'],
              ['dry','skin'], ['warm','skin'], ['oily','skin'],
              ['restless','mind'], ['sharp','mind'], ['calm','mind']
            ] AS tv
            MATCH (tt:TraitType {name: tv[1]})
            CREATE (v:TraitValue {value: tv[0]})
            CREATE (v)-[:OF_TYPE]->(tt)
            """)

            session.run("""
            UNWIND [
              ['Vata','thin'],['Vata','variable'],['Vata','irregular'],['Vata','dry'],['Vata','restless'],
              ['Pitta','medium'],['Pitta','strong'],['Pitta','intense'],['Pitta','warm'],['Pitta','sharp'],
              ['Kapha','large'],['Kapha','slow'],['Kapha','stable'],['Kapha','oily'],['Kapha','calm']
            ] AS row
            MATCH (p:Prakriti {type: row[0]})
            MATCH (tv:TraitValue {value: row[1]})
            CREATE (p)-[:HAS_TRAIT]->(tv)
            """)

