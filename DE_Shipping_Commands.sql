-- Run in pgAdmin, DE_Project_One database

-- Find the number of shipments between two specified ports
-- select * from specific_route;
select count(*) from generalhead where new_foreign_port_lading like 
'%Casablanca%' and new_port_unlading like '%Charleston%';


-- get the average number of units per average  
-- sized container (by separated measurements)
select avg(piece_count)::numeric(10,0) as avg_number_of_unit, 
avg(container_height)::numeric(10,0) as avg_container_height,
avg(container_length)::numeric(10,0) as avg_container_length,
avg(container_width)::numeric(10,0) as avg_container_width
from cargodesc inner join container on 
cargodesc.identifier = container.identifier;


-- Returns the 5 largest container sizes (measured in cubic feet)
SELECT distinct(container_length * container_height * container_width) 
AS container_size_by_cubic_feet FROM container 
order by container_size_cubic_feet desc limit 5;


-- Returns the number of shipments of each differently classified 
-- hazardous material in descending order 
select hazmat_classification, count(hazmat_classification) as material_count 
from hazmatclass group by hazmat_classification order by material_count desc;


-- get the container, seal number, and classification of every shipment 
select container.identifier, container.container_number, seal_number_1, 
hazmatclass.hazmat_classification, hazmat_flash_point_temperature, 
hazmat_flash_point_temperature_negative_ind 
from container inner join hazmat
on container.identifier = hazmat.identifier
inner join hazmatclass on hazmat.identifier = hazmatclass.identifier limit 20;


-- get all orders coming from Korea
select new_vessel_name, vessel_country_code, new_port_unlading as shipping_to, 
new_foreign_port_lading as shipped_from, estimated_arrival_date as 
estimated_arrival, actual_arrival_date as actual_arrival from 
generalhead where new_foreign_port_lading like '%Korea%';


-- get the smallest and largest flashpoints, and the the range between the two
select distinct(select max(hazmat_flash_point_temperature) from hazmat 
where hazmat_flash_point_temperature_negative_ind is not null) as lowest_flash_point_negative, 
(select max(hazmat_flash_point_temperature) from hazmat 
where hazmat_flash_point_temperature_negative_ind is null) as highest_flash_point_positive, 
hazmat_flash_point_temperature_unit as flash_point_unit,
(select distinct((select max(hazmat_flash_point_temperature) as Lowest_flash_point
from hazmat where hazmat_flash_point_temperature_negative_ind is not null) + 
(select max(hazmat_flash_point_temperature) as Highest_flash_point
FROM hazmat where hazmat_flash_point_temperature_negative_ind is null))) 
as flash_point_range from hazmat;


-- get the number of shipments that arrive in oakland during the last
-- week of December and grouped by each of their original ports of lading
select new_foreign_port_lading, count(*) as count_shipments from 
generalhead WHERE new_port_unlading like '%Oakland%' 
AND actual_arrival_date >= '2018-12-23'::date 
AND actual_arrival_date < '2018-12-29'::date
group by new_foreign_port_lading order by count_shipments desc;


-- Get info about all materials marked as explosive or flammable
select cargodesc.container_number, piece_count, hazmat_classification,
hazmat_flash_point_temperature, hazmat_flash_point_temperature_negative_ind,
new_description from cargodesc 
inner join hazmatclass on cargodesc.identifier = hazmatclass.identifier 
inner join hazmat on hazmatclass.identifier = hazmat.identifier
where hazmat_classification = 3 or 
hazmat_classification < 4.4 and hazmat_classification > 4.0 or 
hazmat_classification < 1.7 and hazmat_classification > 1.0
order by piece_count desc limit 20;


-- select info about any shipments that had a difference between the estimated
-- and actual arrival dates of more than 14 days (2 weeks) Display that difference
select new_vessel_name, new_port_unlading, new_foreign_port_lading, 
estimated_arrival_date, actual_arrival_date, 
(((extract(epoch from actual_arrival_date::date) - 
extract(epoch from estimated_arrival_date::date))/(60*60*24))::integer) 
as estimated_arrival_gap from generalhead where estimated_arrival_date >= 
'2018-01-01' and ((((extract(epoch from actual_arrival_date::date) - 
extract(epoch from estimated_arrival_date::date))/(60*60*24))::integer)) >= 15; 


-- use a window function to get the average number of units per container 
-- of each hazmat classification number
select  distinct hazmat_classification,
round(avg(piece_count) over (
	partition by hazmat_classification
)) avg_unit_num_per_container
from hazmatclass inner join newheader on
hazmatclass.identifier = newheader.identifier inner join cargodesc on
newheader.identifier = cargodesc.identifier group by hazmat_classification, piece_count;


