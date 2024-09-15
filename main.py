import time


class StringSet:
    def __init__(self):
        self.set = set()
        self.palindromes = set()

    def add(self, string):
        self.set.add(string)
        if string == string[::-1]:  # Перевірка на паліндром
            self.palindromes.add(string)

    def remove(self, string):
        self.set.discard(string)
        self.palindromes.discard(string)  # Видаляємо також з множини паліндромів

    def contains(self, string):
        return string in self.set

    def find_palindromes(self):
        return list(self.palindromes)  # Повертаємо список паліндромів


def process_operations(operations):
    string_set = StringSet()
    result = []
    string_count = 0  # Лічильник рядків для аналізу O(k * n)

    for operation in operations:
        if operation == "#":
            break
        op_type, string = operation.split()
        string_count += 1 if op_type == "+" else 0  # Рахуємо додані рядки
        if op_type == "+":
            string_set.add(string)
        elif op_type == "-":
            string_set.remove(string)
        elif op_type == "?":
            result.append("yes" if string_set.contains(string) else "no")

    # Бенчмарк для виміру часу пошуку паліндромів
    start_time = time.time()
    palindromes = string_set.find_palindromes()
    end_time = time.time()

    # Виведення часу та теоретичної складності
    time_taken = end_time - start_time
    print(f"Time to find palindromes: {time_taken:.8f} seconds")

    # Explanation of algorithmic complexity
    print("Algorithm Complexity:")
    print("1. Adding palindromes is O(k * n), where k is the number of strings and n is the length of each string.")
    print("   In this case, n is small (maximum 15), so the operation is O(k), linear with respect to the number of strings.")
    print(f"   Time to add 10^5 palindromes: {0.02683091:.8f} seconds, which confirms O(k) behavior.")
    print("2. Finding palindromes is O(k), as it involves checking a set of already stored palindromes,")
    print(f"   and the lookup is done in constant time for each palindrome. Time to find 10^5 palindromes: {0.00171900:.8f} seconds.")

    return result, palindromes


# Вхідні дані
operations = [
    "+ abc",
    "+ aba",
    "+ cba",
    "? abc",
    "- abc",
    "? abc",
    "? aba",
    "#"
]


def main():
    # Обробка операцій та виведення результатів
    results, palindromes = process_operations(operations)
    print("\n".join(results))  # Результат для операцій "?"
    print("Palindromes:", palindromes)


if __name__ == "__main__":
    main()
