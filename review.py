class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return []

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    @classmethod
    def customer(cls):
        return []

    @classmethod
    def restaurant(cls):
        return []

    @classmethod
    def create_review(cls, customer, restaurant, rating):
        # Implement this method to create a review
        pass
