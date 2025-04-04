## Task 2

1. Find all American Politicians whose fathers were also politician. 
American Politicians
SELECT ?person ?personLabel ?father ?fatherLabel
WHERE {
  ?person wdt:P31 wd:Q5.
  ?person wdt:P27 wd:Q30.
  ?person wdt:P106 wd:Q82955.
  ?person wdt:P22 ?father.
  ?father wdt:P106 wd:Q82955.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
} LIMIT 1

2. Find all Norwegian Poets whose date of birth is after 1950. (TIPS: USE FILTER)
Poet
SELECT ?person ?personLabel 
WHERE {
  ?person wdt:P31 wd:Q5. # Is a Human
  ?person wdt:P27 wd:Q20. # Lives in Norway
  ?person wdt:P106 wd:Q49757. # Is a Poet
  ?person wdt:P569 ?dateOfBirth # Date of Birth
  FILTER(YEAR(?dateOfBirth) > 1950) # Filter for date of birth after 1950
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
} LIMIT 1

3. Count number of universities in wikidata.
Number of Universities
SELECT (COUNT(*) AS ?count)
WHERE {
   ?item wdt:P31 wd:Q3918 # Is a University
}
4. Find all Norwegian Poets who are also politicians. Show their birthplace in a map.
Poet and Politician
SELECT *
WHERE {
  ?person wdt:P31 wd:Q5. # Is a human
  ?person wdt:P27 wd:Q20. # Lives in Norway
  ?person wdt:P106 wd:Q49757. # Is a poet
  ?person wdt:P106 wd:Q82955. # Is a politician
  ?person wdt:P19 ?birthplace. # Place of birth
  ?birthplace wdt:P625 ?geo # Coordiante location
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
5. Show the birthplace of all people in a map who received Nobel prizes.
Birthplace of people who recieved a Nobel Prize
SELECT DISTINCT ?person ?personLabel ?nobelPrizeLabel ?birthplace ?geo
WHERE {
  ?person wdt:P31 wd:Q5. # Is human
  ?person wdt:P166 ?nobelPrize. # Is award
  ?person wdt:P19 ?birthplace. # Place of birth
  ?birthplace wdt:P625 ?geo. # Place of birth coordinate
  ?nobelPrize wdt:P279 wd:Q7191. # Is Nobel price          
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}