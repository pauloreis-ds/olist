
SELECT region, AVG(avg_freight) FROM (
    SELECT *, 
        CASE
             WHEN customer_state IN ('AM','RR','AP','PA','TO','RO','AC') THEN 'north'
                    WHEN customer_state IN ('MA','PI','CE','RN','PE','PB','SE','AL','BA') THEN 'northeast'
                    WHEN customer_state IN ('MT','MS','GO','DF') THEN 'midwest'
                    WHEN customer_state IN ('SP','RJ','ES','MG') THEN 'southeast'
                    WHEN customer_state IN ('PR','RS','SC') THEN 'south'
                    ELSE 'unknown_region'
                END region
    FROM (
        SELECT customer_state,
               AVG(freight_value) AS avg_freight
        FROM orders LEFT JOIN order_items ON orders.order_id = order_items.order_id
                    LEFT JOIN customers ON orders.customer_id = customers.customer_id
        WHERE order_purchase_timestamp BETWEEN date('2015-01-01') AND date('2019-01-01')
        GROUP BY customer_state
        ) AS states_sales
) AS regional_sales
GROUP BY regional_sales.region
