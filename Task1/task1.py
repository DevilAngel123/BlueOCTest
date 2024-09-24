from collections import Counter
import unittest

def most_frequent_string_lengths(strings):
    if not strings: 
        return []
    lengths = [len(s) for s in strings]
    length_counts = Counter(lengths)
    max_count = max(length_counts.values())
    most_frequent_lengths = [length for length, count in length_counts.items() if count == max_count]
    result = [s for s in strings if len(s) in most_frequent_lengths]
    return result

test_input_1 = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
print(most_frequent_string_lengths(test_input_1))  
test_input_2 = ['apple', 'orange', 'banana', 'kiwi', 'pear']
print(most_frequent_string_lengths(test_input_2)) 

# Unit test class
class TestMostFrequentStringLengths(unittest.TestCase):

    def test_typical_input(self):
        input_data = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
        expected_output = ['ab', 'cd', 'gh']
        self.assertEqual(sorted(most_frequent_string_lengths(input_data)), sorted(expected_output))

    def test_all_same_length(self):
        input_data = ['aa', 'bb', 'cc']
        expected_output = ['aa', 'bb', 'cc']
        self.assertEqual(sorted(most_frequent_string_lengths(input_data)), sorted(expected_output))

    def test_varying_lengths(self):
        input_data = ['apple', 'orange', 'banana', 'kiwi', 'pear']
        expected_output = ['orange', 'banana', 'kiwi', 'pear']  # Lengths 4 and 6 are most frequent
        self.assertEqual(sorted(most_frequent_string_lengths(input_data)), sorted(expected_output))
        
    def test_with_multiple_teams(self):
        input_data = [
            "Manchester United","Real Madrid","FC Barcelona","Bayern Munich","Liverpool FC","Juventus","Paris Saint-Germain","Chelsea","Inter Milan","Arsenal"
        ]

if __name__ == '__main__':
    unittest.main()






