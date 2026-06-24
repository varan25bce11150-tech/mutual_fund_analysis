-- Top 5 funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;


-- Average NAV

SELECT
AVG(nav)
FROM fact_nav;



-- SIP transactions

SELECT
transaction_type,
COUNT(*)

FROM fact_transactions

GROUP BY transaction_type;



-- Low expense funds

SELECT *

FROM fact_performance

WHERE expense_ratio < 1;