class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []

    def change_given_name(self, new_given_name):
        self.given_name = new_given_name

    def change_family_name(self, new_family_name):
        self.family_name = new_family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return []

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        # Implement this method to find a customer by full name
        pass

    @classmethod
    def find_all_by_given_name(cls, given_name):
        # Implement this method to find all customers by given name
        pass

    def add_review(self, restaurant, rating):
        # Implement this method to add a review associated with this customer
        pass