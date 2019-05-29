SELECT MIN(a.x - b.x) AS shortest
FROM point a, point b
WHERE a.x > b.x;

SELECT MIN(ABS(a.x- b.x)) AS shortest
FROM point a
JOIN point b
ON a.x != b.x