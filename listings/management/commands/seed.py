from django.core.management.base import BaseCommand
from django_seed import Seed
from listings.models import Listing, Booking, Review
import random
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with listings, bookings, and reviews"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        # Seed Listings
        seeder.add_entity(Listing, 10, {
            'title': lambda x: fake.company(),
            'description': lambda x: fake.text(),
            'location': lambda x: fake.city(),
            'price': lambda x: round(random.uniform(50, 500), 2)
        })

        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS('Listings seeded successfully!'))

        listings = Listing.objects.all()

        # Seed Bookings & Reviews
        for listing in listings:
            for _ in range(random.randint(1, 5)):
                Booking.objects.create(
                    listing=listing,
                    user_name=fake.name(),
                    user_email=fake.email(),
                    check_in=fake.date_this_year(),
                    check_out=fake.date_this_year()
                )
            for _ in range(random.randint(1, 3)):
                Review.objects.create(
                    listing=listing,
                    user_name=fake.name(),
                    rating=random.randint(1,5),
                    comment=fake.sentence()
                )
        self.stdout.write(self.style.SUCCESS('Bookings & Reviews seeded successfully!'))
