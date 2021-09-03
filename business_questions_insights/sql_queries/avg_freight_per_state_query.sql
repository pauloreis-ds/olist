

        SELECT customer_state,
               AVG(freight_value) AS avg_freight
        FROM orders LEFT JOIN order_items ON orders.order_id = order_items.order_id
                    LEFT JOIN customers ON orders.customer_id = customers.customer_id
        WHERE order_purchase_timestamp BETWEEN date('2015-01-01') AND date('2019-01-01')
        GROUP BY customer_state
