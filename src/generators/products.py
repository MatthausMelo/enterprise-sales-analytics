from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_US")
Faker.seed(42)
random.seed(42)

OUTPUT_PATH = Path("data/raw")

PRODUCT_CATALOG = {
    "Electronics": [
        "Wireless Mouse",
        "Gaming Keyboard",
        "Bluetooth Speaker",
        "USB-C Hub",
        "External SSD",
        "Webcam",
        "Monitor",
        "Laptop Stand"
    ],
    "Office": [
        "Notebook",
        "Desk Lamp",
        "Office Chair",
        "Standing Desk",
        "Printer",
        "Paper Shredder",
        "Whiteboard",
        "Desk Organizer"
    ],
    "Home": [
        "Coffee Maker",
        "Air Fryer",
        "Vacuum Cleaner",
        "Blender",
        "Electric Kettle",
        "Microwave",
        "Toaster",
        "Ceiling Fan"
    ],
    "Sports": [
        "Yoga Mat",
        "Dumbbell Set",
        "Running Shoes",
        "Football",
        "Basketball",
        "Resistance Bands",
        "Water Bottle",
        "Treadmill"
    ],
    "Books": [
        "Python Programming",
        "SQL Fundamentals",
        "Business Analytics",
        "Machine Learning Basics",
        "Data Engineering",
        "Project Management",
        "Artificial Intelligence",
        "Cloud Computing"
    ]
}


def generate_products(quantity=500):

    products = []

    for product_id in range(1, quantity + 1):

        category = random.choice(list(PRODUCT_CATALOG.keys()))
        product_name = random.choice(PRODUCT_CATALOG[category])

        cost = round(random.uniform(10, 600), 2)

        markup = random.uniform(1.2, 2.0)

        price = round(cost * markup, 2)

        if cost > 300:
            stock = random.randint(10, 60)
        elif cost > 100:
            stock = random.randint(50, 200)
        else:
            stock = random.randint(200, 1000)

        products.append(
            {
                "product_id": product_id,
                "product_name": product_name,
                "category": category,
                "supplier": fake.company(),
                "cost": cost,
                "price": price,
                "stock_quantity": stock,
                "created_at": fake.date_between(
                    start_date="-3y",
                    end_date="today"
                )
            }
        )

    df = pd.DataFrame(products)

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        OUTPUT_PATH / "products.csv",
        index=False
    )

    print(f" {len(df):,} products generated.")