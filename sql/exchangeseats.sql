# Write your MySQL query statement below
select
if(id < (select count(*) from seat), if(id mod 2=0, id-1, id+1), if(id mod 2=0, id-1, id)) as id, student
from seat
order by id asc;


SELECT
    (CASE WHEN id%2=0 THEN id-1 
     WHEN id%2=1 AND id<(select max(id) FROM seat) THEN id+1 
    ELSE id
    END) as id
    ,student
FROM seat
ORDER BY id;