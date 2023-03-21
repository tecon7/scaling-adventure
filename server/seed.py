from app import app
from models import db, Sweet, Vendor, VendorSweet
from faker import Faker
import random

fake = Faker()


def seed_data():
    with app.app_context():
        Sweet.query.delete()
        Vendor.query.delete()
        VendorSweet.query.delete()

        v1 = Vendor(name=fake.name())
        v2 = Vendor(name=fake.name())
        v3 = Vendor(name=fake.name())

        s1 = Sweet(name=fake.word())
        s2 = Sweet(name=fake.word())
        s3 = Sweet(name=fake.word())
        s4 = Sweet(name=fake.word())
        s5 = Sweet(name=fake.word())

        v1.sweets = [s1, s2]
        v2.sweets = [s3, s4, s5]
        v3.sweets = [s2, s4]

        db.session.add_all([v1, v2, v3, s1, s2, s3, s4, s5])

        for vs in v1.vendor_sweets:
            vs.price = random.randint(1, 10)
        for vs in v2.vendor_sweets:
            vs.price = random.randint(1, 10)
        for vs in v3.vendor_sweets:
            vs.price = random.randint(1, 10)

        db.session.commit()

if __name__ == '__main__':
    seed_data()