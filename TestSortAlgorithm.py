import unittest
from SortAlgorithm import SortAlgorithm
class TestSortAlgorithm(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.sortAlgorithm = SortAlgorithm()
  #Each test method starts with the keyword test_
  def test_insertionSort(self):
    self.assertEqual(self.sortAlgorithm.insertionSort([4, 7, -1, 0, 4, 9, -89, 23]), [-89, -1, 0, 4, 4, 7, 9, 23])
    self.assertEqual(self.sortAlgorithm.insertionSort([4, 0, -5, 1, 4, 9, -8, 0, 9]), [-8, -5, 0, 0, 1, 4, 4, 9, 9])
    self.assertEqual(self.sortAlgorithm.insertionSort([4]), [4])
    with self.assertRaises(Exception):
       self.sortAlgorithm.insertionSort([])
    with self.assertRaises(TypeError):
      self.sortAlgorithm.insertionSort(['строка', 0, 1, 4, -7])
      self.sortAlgorithm.insertionSort([0, 1, 4, -7, 2.6])

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
