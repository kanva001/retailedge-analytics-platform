import pandas as pd
from db_connection import get_sql_server_engine

SERVER = "bethel\SQLEXPRESS"
DATABASE = "AdventureWorks2022"  # adjust if yours is different

engine = get_sql_server_engine(SERVER, DATABASE)


def extract_dim_product():
    query = """
    SELECT
        p.ProductID AS product_id,
        p.Name,
        pc.Name AS product_category,
        ps.Name AS product_subcategory
    FROM Production.Product p
    LEFT JOIN Production.ProductSubcategory ps
        ON p.ProductSubcategoryID = ps.ProductSubcategoryID
    LEFT JOIN Production.ProductCategory pc
        ON ps.ProductCategoryID = pc.ProductCategoryID;
    """
    return pd.read_sql(query, engine)


def extract_dim_customer():
    query = """
    SELECT
        c.CustomerID AS customer_id,
        p.FirstName,
        p.LastName,
        ea.EmailAddress,
        pp.PhoneNumber
    FROM Sales.Customer c
    LEFT JOIN Person.Person p
        ON c.PersonID = p.BusinessEntityID
    LEFT JOIN Person.EmailAddress ea
        ON p.BusinessEntityID = ea.BusinessEntityID
    LEFT JOIN Person.PersonPhone pp
        ON p.BusinessEntityID = pp.BusinessEntityID;
    """
    return pd.read_sql(query, engine)


def extract_fact_sales():
    query = """
    SELECT
        soh.SalesOrderID AS sales_order_id,
        CAST(FORMAT(soh.OrderDate, 'yyyyMMdd') AS INT) AS order_date_id,
        soh.CustomerID AS customer_id,
        sod.ProductID AS product_id,
        soh.TerritoryID AS territory_id,
        sod.OrderQty AS quantity,
        sod.UnitPrice AS unit_price,
        sod.LineTotal AS line_total,
        soh.TotalDue AS total_due
    FROM Sales.SalesOrderHeader soh
    JOIN Sales.SalesOrderDetail sod
        ON soh.SalesOrderID = sod.SalesOrderID;
    """
    return pd.read_sql(query, engine)
