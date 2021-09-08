
    SELECT product_category_name AS category,
           COUNT(order_items.order_id) AS number_of_orders           
    FROM products RIGHT JOIN order_items ON order_items.product_id = products.product_id
                  LEFT JOIN orders ON orders.order_id = order_items.order_id
    WHERE order_approved_at BETWEEN DATE('2018-01-01') AND DATE('2019-01-01')
    GROUP BY product_category_name
