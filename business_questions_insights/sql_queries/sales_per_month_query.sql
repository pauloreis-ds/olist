
SELECT date_trunc('month', order_purchase_timestamp), SUM(price+freight_value)
FROM orders LEFT JOIN order_items ON orders.order_id = order_items.order_id
WHERE order_status='delivered' and
      order_purchase_timestamp BETWEEN date('2018-01-01') AND date('2019-01-01')
GROUP BY date_trunc('month', order_purchase_timestamp)
