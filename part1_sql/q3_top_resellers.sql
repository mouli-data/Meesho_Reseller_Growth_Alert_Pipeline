SELECT
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM resellers r
JOIN orders o
    ON r.reseller_id = o.reseller_id
GROUP BY r.reseller_id, r.reseller_name
HAVING SUM(o.quantity * o.unit_price) > 50000
ORDER BY total_spend DESC
LIMIT 5;
