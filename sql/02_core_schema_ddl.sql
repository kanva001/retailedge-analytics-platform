/* CORE-2: Star Schema for RetailEdge Analytics
   Author: <Your Name>
   Date: 12/27/2025
*/

/* Dimension Tables */

/* dim_product */
CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    name NVARCHAR(255),
    product_category NVARCHAR(255),
    product_subcategory NVARCHAR(255)
);

/* dim_customer */
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    first_name NVARCHAR(100),
    last_name NVARCHAR(100),
    email NVARCHAR(255),
    phone NVARCHAR(50),
    address NVARCHAR(255)
);

/* dim_date */
CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE,
    year INT,
    month INT,
    quarter INT
);

/* dim_territory */
CREATE TABLE dim_territory (
    territory_id INT PRIMARY KEY,
    name NVARCHAR(255),
    country NVARCHAR(10)
);

/* Fact Table */

/* fact_sales */
CREATE TABLE fact_sales (
    sales_order_id INT PRIMARY KEY,
    order_date_id INT,
    customer_id INT,
    product_id INT,
    territory_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    line_total DECIMAL(10,2),
    total_due DECIMAL(10,2),
    FOREIGN KEY (order_date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (territory_id) REFERENCES dim_territory(territory_id)
);
