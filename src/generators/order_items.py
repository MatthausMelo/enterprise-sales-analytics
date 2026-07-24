import pandas as pd
import random
from pathlib import Path

OUTPUT_PATH = Path("data/raw")

random.seed(42)


def generate_order_items():

    orders = pd.read_csv(OUTPUT_PATH / "orders.csv")
    products = pd.read_csv(OUTPUT_PATH / "products.csv")

    order_items = []

    item_id = 1

    for _, order in orders.iterrows():

        number_of_products = random.randint(1, 5)

        selected_products = products.sample(number_of_products)

        for _, product in selected_products.iterrows():

            quantity = random.randint(1, 4)

            order_items.append(
                {
                    "order_item_id": item_id,
                    "order_id": order["order_id"],
                    "product_id": product["product_id"],
                    "quantity": quantity,
                    "unit_cost": product["cost"],
                    "unit_price": product["price"],
                    "line_total": round(quantity * product["price"], 2)
                }
            )

            item_id += 1

    df = pd.DataFrame(order_items)

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        OUTPUT_PATH / "order_items.csv",
        index=False
    )

    print(f" {len(df):,} order items generated.")