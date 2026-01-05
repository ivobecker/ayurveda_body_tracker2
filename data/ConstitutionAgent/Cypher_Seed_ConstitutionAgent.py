CREATE (:Prakriti {type: 'Vata'});
CREATE (:Prakriti {type: 'Pitta'});
CREATE (:Prakriti {type: 'Kapha'});


CREATE (:Trait {name: 'body_frame', value: 'thin'});
CREATE (:Trait {name: 'body_frame', value: 'medium'});
CREATE (:Trait {name: 'body_frame', value: 'large'});

CREATE (:Trait {name: 'metabolism', value: 'variable'});
CREATE (:Trait {name: 'metabolism', value: 'strong'});
CREATE (:Trait {name: 'metabolism', value: 'slow'});

CREATE (:Trait {name: 'appetite', value: 'irregular'});
CREATE (:Trait {name: 'appetite', value: 'intense'});
CREATE (:Trait {name: 'appetite', value: 'stable'});

CREATE (:Trait {name: 'skin', value: 'dry'});
CREATE (:Trait {name: 'skin', value: 'warm'});
CREATE (:Trait {name: 'skin', value: 'oily'});

CREATE (:Trait {name: 'mind', value: 'restless'});
CREATE (:Trait {name: 'mind', value: 'sharp'});
CREATE (:Trait {name: 'mind', value: 'calm'});


MATCH (p:Prakriti {type: 'Vata'}), (t:Trait)
WHERE (t.name = 'body_frame' AND t.value = 'thin')
   OR (t.name = 'metabolism' AND t.value = 'variable')
   OR (t.name = 'appetite' AND t.value = 'irregular')
   OR (t.name = 'skin' AND t.value = 'dry')
   OR (t.name = 'mind' AND t.value = 'restless')
CREATE (p)-[:HAS_TRAIT]->(t);

MATCH (p:Prakriti {type: 'Pitta'}), (t:Trait)
WHERE (t.name = 'body_frame' AND t.value = 'medium')
   OR (t.name = 'metabolism' AND t.value = 'strong')
   OR (t.name = 'appetite' AND t.value = 'intense')
   OR (t.name = 'skin' AND t.value = 'warm')
   OR (t.name = 'mind' AND t.value = 'sharp')
CREATE (p)-[:HAS_TRAIT]->(t);


MATCH (p:Prakriti {type: 'Kapha'}), (t:Trait)
WHERE (t.name = 'body_frame' AND t.value = 'large')
   OR (t.name = 'metabolism' AND t.value = 'slow')
   OR (t.name = 'appetite' AND t.value = 'stable')
   OR (t.name = 'skin' AND t.value = 'oily')
   OR (t.name = 'mind' AND t.value = 'calm')
CREATE (p)-[:HAS_TRAIT]->(t);