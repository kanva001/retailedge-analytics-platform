import pandas as pd
from pathlib import Path

CURATED_DIR = Path(__file__).resolve().parents[2] / "data" / "curated"
TRANSFORM_DIR = Path(__file__).resolve().parents[2] / "data" / "transformed"
TRANSFORM_DIR.mkdir(parents=True, exist_ok=True)


def transform_dim_product():
    df = pd.read_csv(CURATED_DIR / "dim_product.csv")
    df = df.drop_duplicates(subset=["product_id"])
    df["product_category"] = df["product_category"].fillna("Unknown")
    df["product_subcategory"] = df["product_subcategory"].fillna("Unknown")
    df.to_parquet(TRANSFORM_DIR / "dim_product.parquet", index=False)
    print("dim_product.parquet saved")


def transform_dim_customer():
    df = pd.read_csv(CURATED_DIR / "dim_customer.csv")
    df = df.drop_duplicates(subset=["customer_id"])
    df["EmailAddress"] = df["EmailAddress"].fillna("unknown@example.com")
    df.to_parquet(TRANSFORM_DIR / "dim_customer.parquet", index=False)
    print("dim_customer.parquet saved")


def transform_fact_sales():
    df = pd.read_csv(CURATED_DIR / "fact_sales.csv")
    df = df.drop_duplicates(subset=["sales_order_id", "product_id", "customer_id"])
    # remove invalid or negative sales
    df = df[df["line_total"] >= 0]
    # convert order_date_id to string (optional: easier for Athena)
    df["order_date_id"] = df["order_date_id"].astype(str)
    df.to_parquet(TRANSFORM_DIR / "fact_sales.parquet", index=False)
    print("fact_sales.parquet saved")


def run_transform():
    transform_dim_product()
    transform_dim_customer()
    transform_fact_sales()


if __name__ == "__main__":
    run_transform()
