/* RetailEdge Analytics Platform
   CORE-1: Business KPIs from AdventureWorks
   Author: VK
   Date: 12/27/2025
*/

/* KPI 1: Total Revenue by Year and Month */
SELECT
    YEAR(OrderDate) AS sales_year,
    MONTH(OrderDate) AS sales_month,
    SUM(TotalDue) AS total_revenue
FROM Sales.SalesOrderHeader
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY sales_year, sales_month;


/* KPI 2: Top 10 Products by Revenue */
SELECT TOP 10
    p.Name AS product_name,
    SUM(d.LineTotal) AS revenue
FROM Sales.SalesOrderDetail d
JOIN Production.Product p
    ON d.ProductID = p.ProductID
GROUP BY p.Name
ORDER BY revenue DESC;


/* KPI 3: Customer Lifetime Value (CLV) */
SELECT
    c.CustomerID,
    SUM(h.TotalDue) AS lifetime_value
FROM Sales.SalesOrderHeader h
JOIN Sales.Customer c
    ON h.CustomerID = c.CustomerID
GROUP BY c.CustomerID
ORDER BY lifetime_value DESC;


/* KPI 4: Monthly Returns / Refund Rate */
SELECT
    YEAR(h.OrderDate) AS sales_year,
    MONTH(h.OrderDate) AS sales_month,
    SUM(CASE WHEN r.SalesOrderID IS NOT NULL THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS return_rate
FROM Sales.SalesOrderHeader h
LEFT JOIN Sales.SalesOrderHeader r
    ON h.SalesOrderID = r.SalesOrderID
    AND r.Status = 4  -- Status 4 = Canceled/Returned
GROUP BY YEAR(h.OrderDate), MONTH(h.OrderDate)
ORDER BY sales_year, sales_month;


/* KPI 5: Revenue by Territory */
SELECT
    t.Name AS territory_name,
    t.CountryRegionCode AS country,
    SUM(h.TotalDue) AS total_revenue
FROM Sales.SalesOrderHeader h
JOIN Sales.SalesTerritory t
    ON h.TerritoryID = t.TerritoryID
GROUP BY t.Name, t.CountryRegionCode
ORDER BY total_revenue DESC;
