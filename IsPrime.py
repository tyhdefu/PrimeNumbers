import unittest

class TestIsPrime(unittest.TestCase):
 
  def test_0(self):
    self.assertEqual(is_prime(0), False)
    
  def test_1(self):
    self.assertEqual(is_prime(1), False)

  def test_2(self):
    self.assertEqual(is_prime(2), True)

  def test_3(self):
    self.assertEqual(is_prime(3), True)

  def test_4(self):
    self.assertEqual(is_prime(4), False)

  def test_97(self):
    self.assertEqual(is_prime(97), True)

  def test_99(self):
    self.assertEqual(is_prime(99), False)

def is_prime(number):
  if number <= 1:
    return False
  checkNumberList = list(range(2, number))
  return not any(number % x == 0 for x in checkNumberList)

if __name__ == '__main__':
  unittest.main()
