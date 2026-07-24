from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_US")
Faker.seed(42)
random.seed(42)

OUTPUT_PATH = Path("data/raw")

ORDER_STATUS = [
    "Completed",
    "Completed",
    "Completed",
    "Completed",
    "Shipped",
    "Cancelled",
    "Returned"
]

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "PayPal",
    "Bank Transfer"
]

SALES_CHANNELS = [
    "Online",
    "Retail Store"
]


def generate_orders(quantity=100000):

    orders = []

    for order_id in range(1, quantity + 1):

        order_date = fake.date_between(
            start_date="-2y",
            end_date="today"
        )

        orders.append(
            {
                "order_id": order_id,
                "customer_id": random.randint(1, 10000),
                "store_id": random.randint(1, 50),
                "order_date": order_date,
                "status": random.choice(ORDER_STATUS),
                "payment_method": random.choice(PAYMENT_METHODS),
                "sales_channel": random.choice(SALES_CHANNELS)
            }
        )

    df = pd.DataFrame(orders)

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        OUTPUT_PATH / "orders.csv",
        index=False
    )

    print(f" {len(df):,} orders generated.")