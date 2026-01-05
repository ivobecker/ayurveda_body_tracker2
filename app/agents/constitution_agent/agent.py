from datetime import datetime
from typing import Dict, List
from google.adk.agents import Agent

from agents.constitution_agent.tools import (
    query_constitution_tool,
    store_episode_tool,
)

def create_constitution_agent():
    return Agent(
        name="constitution-agent",
        instructions="You reason over constitutional knowledge stored in a graph.",
        tools=[
            query_constitution_tool,
            store_episode_tool,
        ],
    )

# class ConstitutionAgent:
#     """
#     Google ADK-compatible agent:
#     - Stateless
#     - Deterministic
#     - Explainable

# Responsibility
#   Estimate Prakriti
#   Never modify it later
# Reads 
#     Questionnaire answers
#     Neo4j (:Prakriti)-[:HAS_TRAITS]
# Writes (graphiti)
#     ConstitutionHypothesis(
#     subject=user_id,
#     prakriti="Vata-Pitta",
#     confidence=0.76,
#     source="prakriti_questionnaire_v1"
#     )
# Explanation template
#     “Your constitution is likely Vata-Pitta because traits A, B, C were dominant.”



#     """

#     def __init__(self, neo4j_query_tool, graphiti_store_tool):
#         self.query_neo4j = neo4j_query_tool
#         self.store_fact = graphiti_store_tool

#     def run(self, user_id: str, questionnaire: Dict[str, str]) -> Dict:
#         """
#         Main entry point for the agent
#         """

#         # 1️⃣ Load Prakriti trait definitions from Neo4j
#         prakriti_traits = self._load_prakriti_traits()

#         # 2️⃣ Score questionnaire against traits
#         scores, evidence = self._score_prakriti(prakriti_traits, questionnaire)

#         # 3️⃣ Determine dominant constitution
#         prakriti, confidence = self._determine_prakriti(scores)

#         # 4️⃣ Store hypothesis in graphiti
#         fact = self._build_graphiti_fact(
#             user_id=user_id,
#             prakriti=prakriti,
#             confidence=confidence,
#             evidence=evidence
#         )
#         self.store_fact(fact)

#         # 5️⃣ Return explainable result
#         return {
#             "prakriti": prakriti,
#             "confidence": confidence,
#             "evidence": evidence,
#             "explanation": self._explain(prakriti, evidence)
#         }

#     # ----------------------------
#     # Internal methods
#     # ----------------------------

#     def _load_prakriti_traits(self) -> List[dict]:
#         cypher = """
#         MATCH (p:Prakriti)-[:HAS_TRAIT]->(tv:TraitValue)-[:OF_TYPE]->(tt:TraitType)
#         RETURN p.type AS prakriti, tt.category as trait_type_category, tt.name AS trait_type, tv.value AS trait_value
#         """
#         return self.query_neo4j(cypher, {})

#     def _score_prakriti(self, traits: List[dict], questionnaire: Dict[str, str]):
#         scores = {"Vata": 0, "Pitta": 0, "Kapha": 0}
#         evidence = {"Vata": [], "Pitta": [], "Kapha": []}

#         for row in traits:
#             prakriti = row["prakriti"]
#             traits_category = row["trait_type_category"]   #e.g., "body_frame", "digestion"
#             trait = row["trait_value"] # e.g., "high", "medium", "low"
#             expected_value = row["trait_value"]  

#             if questionnaire.get(trait) == expected_value:
#                 scores[prakriti] += 1
#                 evidence[prakriti].append(trait)

#         return scores, evidence

#     def _determine_prakriti(self, scores: Dict[str, int]):
#         sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

#         top, second = sorted_scores[0], sorted_scores[1]

#         # Dual constitution if close
#         if top[1] - second[1] <= 1:
#             prakriti = f"{top[0]}-{second[0]}"
#             confidence = 0.7
#         else:
#             prakriti = top[0]
#             confidence = min(0.9, 0.6 + 0.1 * top[1])

#         return prakriti, round(confidence, 2)

#     def _build_graphiti_fact(self, user_id, prakriti, confidence, evidence):
#         return {
#             "type": "ConstitutionHypothesis",
#             "subject": user_id,
#             "prakriti": prakriti,
#             "confidence": confidence,
#             "evidence": evidence,
#             "source": "prakriti_questionnaire_v1",
#             "timestamp": datetime.utcnow().isoformat()
#         }

#     def _explain(self, prakriti: str, evidence: Dict[str, List[str]]) -> str:
#         parts = prakriti.split("-")
#         explanations = []

#         for p in parts:
#             traits = ", ".join(evidence[p])
#             explanations.append(f"{p} traits detected: {traits}")

#         return " | ".join(explanations)
