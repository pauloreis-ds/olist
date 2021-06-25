
           SELECT date(MIN(order_purchase_timestamp)), SUM(price)
           FROM   orders LEFT JOIN order_items ON orders.order_id = order_items.order_id
           WHERE  order_status='delivered' and
                  order_purchase_timestamp BETWEEN date('{intial_date}') AND date('{final_date}')
           
           
           ;
        