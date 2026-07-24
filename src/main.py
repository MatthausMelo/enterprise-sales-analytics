from generators.customers import generate_customers
from generators.products import generate_products
from generators.orders import generate_orders
from generators.order_items import generate_order_items
from etl.pipeline import run_pipeline

def main():
    print("=" * 50)
    print("Enterprise Sales Analytics Platform")
    print("=" * 50)

    generate_customers()
    generate_products()
    generate_orders()
    generate_order_items()
    
    run_pipeline()

if __name__ == "__main__":
    main()