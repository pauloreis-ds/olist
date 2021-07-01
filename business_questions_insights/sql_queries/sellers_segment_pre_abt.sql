
SELECT orders.order_id AS order_id,
       order_approved_at AS order_approved_at,
       order_purchase_timestamp as purchase_date,
       price AS price,
       order_items.seller_id AS seller_id
FROM orders LEFT JOIN order_items ON orders.order_id = order_items.order_id
            LEFT JOIN sellers ON order_items.seller_id = sellers.seller_id