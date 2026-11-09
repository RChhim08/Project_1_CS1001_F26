"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("HEllo"), 2)
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        #self.fail("TODO: write the first unit test for vowel_count")

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)
    #     # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
    #     self.fail("TODO: write the second unit test for vowel_count")

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual(hw1.short_lists([[4, 4, 3], [3], [3, 2], [6, 4]]), [[3, 2], [6, 4]])
    #     # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
    #     self.fail("TODO: write the first unit test for short_lists")

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[3, 3, 2], [2, 1, 4], [3]]), [])
    #     # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
    #     self.fail("TODO: write the second unit test for short_lists")

    #Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[4, 4], [3, 4], [4, 3]]), [[4, 4] , [3, 4], [3, 4]])
    #     # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
    #     self.fail("TODO: write the first unit test for ascending_pairs")

    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual(hw1.ascending_pairs([[4, 4, 4], [3, 4], [1], [4, 3]]), [[4, 4, 4], [3, 4], [1], [3, 4]])
    #     # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
    #     self.fail("TODO: write the second unit test for ascending_pairs")

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(3, 0), data.Price(3, 25)), data.Price(6, 25))
    #     # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
    #     self.fail("TODO: write the first unit test for add_prices")

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(3, 50), data.Price(3, 50)), data.Price(7, 0))
    #     # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
    #     self.fail("TODO: write the second unit test for add_prices")

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(1, 4), data.Point(4, 0))), 12)
    #     # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
    #     self.fail("TODO: write the first unit test for rectangle_area")

    def test_rectangle_area_negative_coordinates(self):
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-3, 4), data.Point(4, -8))), 84)
    #     # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
    #     self.fail("TODO: write the second unit test for rectangle_area")

    #Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        first = data.Book(["Ben Obama", "William Will"], "Lost Sea's")
        second = data.Book(["Ben Obama"], "Boys In Forest")
        self.assertEqual(hw1.books_by_author("Ben Obama", [data.Book(["Ben Obama", "William Will"], "Lost Sea's"), data.Book(["Ben Obama"], "Boys In Forest")]), [first, second])
    #     # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
    #     self.fail("TODO: write the first unit test for books_by_author")

    def test_books_by_author_no_matches(self):
            self.assertEqual(hw1.books_by_author("Patrick Mahomes", [data.Book(["Deebo Samuel", "Tom Brady"], "Win Or Loose"), data.Book(["Travis Kelce"], "Road to Victory")]), [])
    #     # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
    #     self.fail("TODO: write the second unit test for books_by_author")

    # Part 7: circle_bound
    def test_circle_bound_square(self):
            top_left = data.Point(1, 9)
            bottom_right = data.Point(7, 1)
            rectangle_test = data.Rectangle(top_left, bottom_right)
            circle_test = data.Circle(data.Point(4, 5), 5)
            self.assertEqual(hw1.circle_bound(rectangle_test), circle_test)
    #     # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
    #     self.fail("TODO: write the first unit test for circle_bound")

    def test_circle_bound_non_square_rectangle(self):
        point_Positive_Left = data.Point(1, 3)
        point_Positive_Right = data.Point(3, 1)
        rectangle_test = data.Rectangle(point_Positive_Left, point_Positive_Right)
        circle_test = data.Circle(data.Point(2, 2), 2 ** 0.5)
        self.assertEqual(hw1.circle_bound(rectangle_test), circle_test)
    #     # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
    #     self.fail("TODO: write the second unit test for circle_bound")

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees_one = [data.Employee("Ava", 10), data.Employee("Sam", 20), data.Employee("Matt", 30)]
        self.assertEqual(hw1.below_pay_average(employees_one), ["Ava"])
        employees_two = [data.Employee("Ava", 20), data.Employee("Sam", 20), data.Employee("Matt", 20)]
        self.assertEqual(hw1.below_pay_average(employees_two), [])
    #     # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
    #     self.fail("TODO: write the first unit test for below_pay_average")

    def test_below_pay_average_empty_list(self):
         self.assertEqual(hw1.below_pay_average([]), [])
    #     # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
    #     self.fail("TODO: write the second unit test for below_pay_average")


if __name__ == '__main__':
    unittest.main()
