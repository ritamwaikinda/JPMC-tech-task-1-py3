import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
#test to see if priceA is zero
def test_getRatio_priceAEqualToZero(self)
  price_a: 0
  price_b: 121.68
  self.assertEqual(getRatio(price_a, price_b), 0))

#test to see if priceB is zero
def test_getRatio_priceBEqualToZero(self)
  price_a: 120.48
  price_b: 0
  self.assertIsNone(getRatio(price_a, price_b))

#testing to see when Price A Company's stock outperforms Price B Company's.
def test_getRatio_greaterThan1(self):
  price_a = 385.14
  price_b = 154.82
  self.assertGreater(getRatio(price_a, price_b), 1)

#testing to see when Price A Company's stock underperforms Price B Company's.
def test_getRatio_lessThan1(self):
  price_a = 167.97
  price_b = 344.69
  self.assertLess(getRatio(price_a, price_b), 1)

#testing to see when the two stock prices are equal.
def test_getRatio_isExactlyOne(self):
  price_a = 229.37
  price_b = 229.37
  self.assertEqual(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
