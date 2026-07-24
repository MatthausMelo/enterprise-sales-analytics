from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_US")
Faker.seed(42)
random.seed(42)


def generate_customers(quantity=10000):

    customers = []

    loyalty_levels = ["Bronze", "Silver", "Gold", "Platinum"]

    for customer_id in range(1, quantity + 1):

        customers.append(
            {
                "customer_id": customer_id,
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "city": fake.city(),
                "state": fake.state(),
                "country": "United States",
                "age": random.randint(18, 75),
                "signup_date": fake.date_between(start_date="-5y", end_date="today"),
                "loyalty_level": random.choices(
                    loyalty_levels,
                    weights=[50, 30, 15, 5]
                )[0]
            }
        )

    df = pd.DataFrame(customers)

    output_folder = Path("data/raw")
    output_folder.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        output_folder / "customers.csv",
        index=False
    )

    print(f" {len(df):,} customers generated.")