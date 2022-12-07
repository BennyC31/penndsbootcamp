select count(*) from station s ;
select * from station s;

select *
from station s
;

SELECT s.station,s.name, COUNT(m.station) AS cnt
FROM station s
JOIN measurement m  ON s.station  = m.station 
GROUP BY s.station 
order by cnt desc;

select m.station, min(tobs) , max(tobs), AVG(tobs) , count(tobs)
from measurement m 
where m.station = 'USC00519281';

SELECT m1.date 
from measurement m1 
WHERE m1.station = 'USC00519281'
order by m1.date DESC limit 1;


select m.date,m.tobs from measurement m where date > (select date((SELECT m1.date 
from measurement m1 
WHERE m1.station = 'USC00519281'
order by m1.date DESC limit 1),'-1 year','-1 day'));


select m.date,m.tobs from measurement m where date > (select date((SELECT m1.date 
from measurement m1 
WHERE m1.station = 'USC00519281'
order by m1.date DESC limit 1),'-1 year','-1 day'));

select m.date,m.tobs from measurement m where date > (select date((SELECT m1.date 
from measurement m1 
WHERE m1.station = 'USC00519397' 
order by m1.date DESC limit 1),'-1 year','-1 day'));



