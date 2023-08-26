class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.customers.append(self)

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, name):
        self._given_name = name

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, name):
        self._family_name = name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.customers
    
    def restaurants(self):
        return list(set([review.restaurant for review in Review.all() if review.customer == self]))

    def add_review(self, restaurant, rating):
        Review(self, restaurant, rating)
        
    def num_reviews(self):
        return len([review for review in Review.all() if review.customer == self])

    @classmethod
    def find_by_name(cls, name):
    for customer in cls.customers:
        if customer.full_name() == name:
            return customer

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.customers if customer.given_name == name]
