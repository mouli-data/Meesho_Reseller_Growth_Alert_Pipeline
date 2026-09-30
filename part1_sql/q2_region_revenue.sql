SELECT
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_revenue,
    COUNT(o.order_id) AS order_count
FROM resellers r
JOIN orders o
    ON r.reseller_id = o.reseller_id
GROUP BY r.region
ORDER BY total_revenue DESC;