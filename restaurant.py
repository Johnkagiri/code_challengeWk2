class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def restaurant_name(self):
        return self.name

    @classmethod
    def all(cls):
        return []

    def average_star_rating(self):
        # Implement this method to calculate the average star rating
        pass