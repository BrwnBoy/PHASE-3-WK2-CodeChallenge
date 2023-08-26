class Restaurant:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def reviews(self):
        return [review for review in Review.all() if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]
        return sum(ratings) / len(ratings) if ratings else 0
