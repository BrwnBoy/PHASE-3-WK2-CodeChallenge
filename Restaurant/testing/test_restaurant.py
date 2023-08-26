import unittest
from your_module import Customer, Restaurant, Review

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('John', 'Doe')

    def test_init(self):
        self.assertEqual(self.customer.given_name, 'John')
        self.assertEqual(self.customer.family_name, 'Doe')

    def test_full_name(self):
        self.assertEqual(self.customer.full_name(), 'John Doe')

    def test_all(self):
        self.assertIn(self.customer, Customer.all())

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.restaurant = Restaurant('Test Restaurant')

    def test_init(self):
        self.assertEqual(self.restaurant.name, 'Test Restaurant')

class TestReview(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('John', 'Doe')
        self.restaurant = Restaurant('Test Restaurant')
        self.review = Review(self.customer, self.restaurant, 5)

    def test_init(self):
        self.assertEqual(self.review.customer, self.customer)
        self.assertEqual(self.review.restaurant, self.restaurant)
        self.assertEqual(self.review.rating, 5)

    def test_all(self):
        self.assertIn(self.review, Review.all())

if __name__ == '__main__':
    unittest.main()
