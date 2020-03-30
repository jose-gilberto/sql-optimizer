SELECT tableA.id, tableB.id 
FROM tableA, tableB
WHERE tableA.date = '2000-03-20' 
AND tableA.name LIKE '%Jojo%'