from extract import (
    extract_dim_product,
    extract_dim_customer,
    extract_fact_sales
)
from load_csv import save_to_csv


def run():
    save_to_csv(extract_dim_product(), "dim_product.csv")
    save_to_csv(extract_dim_customer(), "dim_customer.csv")
    save_to_csv(extract_fact_sales(), "fact_sales.csv")


if __name__ == "__main__":
    run()
