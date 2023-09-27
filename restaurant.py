from customer import *
from review import *

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def restaurant_name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def add_review(self, customer, rating):
        review = Review(customer, self, rating)
        self.reviews.append(review)

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer for review in self.reviews]))
