# String Set Data Structure

This repository contains the implementation of a "String Set" data structure, which is capable of efficiently managing a set of strings with operations to add, remove, and check for the presence of strings. Additionally, it can identify all palindromes within the set. The implementation is designed to handle up to 10^6 strings, each up to 15 characters long, making it suitable for high-performance requirements.

## Features

- **Add String**: Adds a string to the set, even if it already exists.
- **Remove String**: Removes a string from the set, without requiring that it must exist in the set prior to removal.
- **Check Membership**: Checks whether a string is present in the set and returns `yes` or `no`.
- **Find Palindromes**: Identifies all palindromic strings within the set.
- **Performance Evaluation**: Measures the time taken for the palindrome detection process.

## Operations

Each operation is denoted by a line in the input data, with the following format:

- `+ <string>`: Adds the specified string to the set.
- `- <string>`: Removes the specified string from the set.
- `? <string>`: Checks if the specified string is present in the set.

The list of operations ends with a line containing the `#` symbol.

## Input and Output

- **Input**: The operations are specified in a text file where each line corresponds to one operation.
- **Output**: For each membership check operation (`?`), the output is either `yes` or `no` depending on whether the string is present in the set.



## Installation

No external libraries are required for the basic operations. The code can be run in any standard Python environment.

## Testing

The `test` file contains unit tests to verify the functionality and performance of the data structure.
