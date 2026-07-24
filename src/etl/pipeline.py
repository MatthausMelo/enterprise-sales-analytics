from etl.load import load_table

def run_pipeline():

    print("\n========= ETL START =========\n")

    load_table("customers.csv", "customers")
    load_table("products.csv", "products")
    load_table("orders.csv", "orders")
    load_table("order_items.csv", "order_items")

    print("\n ========= ETL FINISHED =========\n")