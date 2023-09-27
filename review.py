from customer import *
from restaurant import *

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    @classmethod
    def average_star_rating(cls, restaurant):
        restaurant_reviews = [review.rating for review in cls.all_reviews if review.restaurant == restaurant]
        if not restaurant_reviews:
            return 0
        return sum(restaurant_reviews) / len(restaurant_reviews)

    @classmethod
    def customer_reviews(cls, customer):
        return [review for review in cls.all_reviews if review.customer == customer]

    @classmethod
    def customer_num_reviews(cls, customer):
        return len(cls.customer_reviews(customer))

    @classmethod
    def find_by_name(cls, full_name):
        return [customer for customer in cls.all_customers if customer.full_name() == full_name][0]

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]