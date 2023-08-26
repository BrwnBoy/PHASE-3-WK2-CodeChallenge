class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        self.reviews.append(self)

    @property
    def rating(self):
        return self._rating

    @property
    def customer(self):
        return self._customer

    @property
    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.reviews
 
    @property
    def customer(self):
        return self._customer

    @property
    def restaurant(self):
       return self._restaurant
