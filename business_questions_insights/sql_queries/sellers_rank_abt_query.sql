
SELECT *,
       CASE WHEN percent_revenue <= 0.5 AND percent_orders <= 0.5 THEN 'LOW VALUE LOW FREQUENCY'
       WHEN percent_revenue > 0.5 AND percent_orders <= 0.5 THEN 'HIGH VALUE'
       WHEN percent_revenue <= 0.5 AND percent_orders > 0.5 THEN 'HIGH FREQUENCY'
       WHEN percent_revenue < 0.9 AND percent_orders < 0.9 THEN 'PRODUCTIVE'
       WHEN percent_revenue > 0.9 AND percent_orders > 0.9 THEN 'SUPER PRODUCTIVE'
       ELSE 'PRODUCTIVE'
       END AS segment_value_frequency
FROM (
    SELECT seller_id,
           total_revenue/months_since_first_sale AS revenue_per_month,
           orders_quantity/months_since_first_sale AS orders_per_month,
           PERCENT_RANK() OVER (ORDER BY (total_revenue/months_since_first_sale)) AS percent_revenue,
           PERCENT_RANK() OVER (ORDER BY (orders_quantity/months_since_first_sale)) AS percent_orders
    FROM (
        SELECT seller_id,
               SUM(price) AS total_revenue,
               COUNT(orders.order_id) AS orders_quantity,
               DATE_PART('month', AGE(DATE('2018-10-01'), MIN(order_approved_at))) AS months_since_first_sale
        FROM orders LEFT JOIN order_items ON orders.order_id = order_items.order_id
        WHERE order_approved_at BETWEEN DATE('2018-01-01') AND DATE('2018-10-01') AND
              seller_id IS NOT NULL
        GROUP BY seller_id
    ) AS percent_rank_segment
) AS segment_class
