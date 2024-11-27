select * ,
 rank() over (order by No_of_dishes desc ) as  Best_restaurants_rank 
from 
(
select 
restaurant_id , count(distinct item_id) as 'No_of_dishes'
from food_items 
group by restaurant_id 
order by 'No_of_dishes' ) t1 ;


select * ,
item_id ,  rank() over (order by num_of_orders desc) 
from  
(SELECT item_id, COUNT(order_id) AS num_of_orders 
FROM orders_items
GROUP BY item_id) t1 ; 

select *,
case 
when totall_spend <= 300 then 'low'
when totall_spend <= 400 then 'medium'
when totall_spend > 400 then 'high'
end as spending 
from
(select customer_id, 
round(sum(final_price), 0) as totall_spend 
from orders
group by (customer_id ) 
order by totall_spend desc)
t1 ;

select * 
from 
(
select order_id, delivered_time,
case 
when delivered_time <= '00:30:00'  then 'fast'
when delivered_time between  '00:31:00'and '01:00:00' then 'medium'
when delivered_time > '01:0:00' then 'slow'
end as delivery_time
from orders
) as t1 
where delivery_time = 'fast' ;
















