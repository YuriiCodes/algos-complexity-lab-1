import unittest
import time
from main import StringSet


class TestStringSet(unittest.TestCase):
    def test_add_large(self):
        """Test adding up to 10^6 strings and checking if all are added correctly."""
        string_set = StringSet()
        for i in range(10 ** 6):
            string_set.add(str(i))
        self.assertEqual(len(string_set.set), 10 ** 6)

    def test_find_palindromes(self):
        """Test finding palindromes in a small set of strings."""
        string_set = StringSet()
        string_set.add("aba")
        string_set.add("abc")
        string_set.add("civic")
        string_set.add("deified")
        self.assertCountEqual(string_set.find_palindromes(), ['aba', 'civic', 'deified'])

    def test_add_palindromes_large(self):
        """Benchmark adding 10^5 palindromes and finding them."""
        string_set = StringSet()
        palindromes = [f'{i}{str(i)[::-1]}' for i in range(10 ** 5)]  # Generate 10^5 palindromes

        # Benchmark time to add palindromes
        start_add_time = time.time()
        for palindrome in palindromes:
            string_set.add(palindrome)
        end_add_time = time.time()
        print(f"Time to add 10^5 palindromes: {end_add_time - start_add_time:.8f} seconds")

        # Check that the correct number of strings were added
        self.assertEqual(len(string_set.set), 10 ** 5)

        # Benchmark time to find palindromes
        start_find_time = time.time()
        found_palindromes = string_set.find_palindromes()
        end_find_time = time.time()
        print(f"Time to find 10^5 palindromes: {end_find_time - start_find_time:.8f} seconds")

        # Verify that all added palindromes are found
        self.assertCountEqual(found_palindromes, palindromes)

    def test_remove(self):
        """Test removing strings from the set."""
        string_set = StringSet()
        string_set.add("abc")
        string_set.remove("abc")
        self.assertFalse(string_set.contains("abc"))

    def test_contains(self):
        """Test checking if a string is in the set."""
        string_set = StringSet()
        string_set.add("test")
        self.assertTrue(string_set.contains("test"))
        self.assertFalse(string_set.contains("nonexistent"))


# To run the tests, use the following code block
if __name__ == "__main__":
    unittest.main()
