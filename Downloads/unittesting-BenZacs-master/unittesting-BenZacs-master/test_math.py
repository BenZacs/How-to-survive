import unittest
# import math
#
# class MathTest(unittest.TestCase):
#     def test_sqrt(self):
#         # self.assertEqual(correct, thing_to_test)
#         self.assertEqual(0, math.sqrt(0)) # edge
#         self.assertEqual(4, math.sqrt(16))
#         self.assertEqual(9, math.sqrt(81))
#
#     def test_pow(self):
#         """test of math.pow(x,n)"""
#         self.assertEqual(4, math.pow(2,2))
#         self.assertEqual(9, math.pow(3,2))
#
#     def test_wrong_sqrt(self):
#         self.assertEqual(1.414, math.sqrt(2))
#
#     def test_illegal_argument(self):
#         self.assertEqual(0, math.sqrt(-1))

# def inverse(n):
#     try:
#         result = 1/n
#     except ZeroDivisionError:
#         print("Except block executed!")
#         result = f"Can't compute inverse of {n}"
#     except ValueError:
#         print("ValueError raised")
#     return result
# if __name__ == "__main__":
#     while True:
#         n = int(input("Input a integer: "))
#         print(f"the inverse of {n} is {inverse(n)}")def a

# def avg(list):
#     if len(list) == 0:
#         raise ValueError
#     result = sum(list)/len(list)
#     return result
# class ListUtilTest(unittest.TestCase):
#     def test_avg_singleton_list(self):
#         self.assertEqual(1, avg([1]))
#         self.assertEqual(6, avg([6]))
#         self.assertEqual(7, avg([9]))
#
#     def test_avg_many_values(self):
#         list = [2, 4, -4, 8]
#         self.assertEqual(2.5, avg(list))
#         self.assertEqual(5, avg(list))
#     def test_avg_empty_list(self):
#         with self.assertRaises(ValueError):
#             average = avg([])
