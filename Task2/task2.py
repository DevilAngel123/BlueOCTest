#x = [1, 4, 2, 3, 5]
# #max1 = -1;
# max2 = -1;
# for i in range(len(x)):
#     if x[i] > max1:
#         max2 = max1
#         max1 = x[i]
#     elif x[i] > max2:
#         max2 = x[i]

# print(max1+max2)

def sum_of_largest_number(numbers):
    if len(numbers) < 2:
        raise ValueError ("Please enter array length larger than two numbers")
    
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return largest + second_largest

array = [3, 5, 1, 8, 2]
answer = sum_of_largest_number(array)
print (answer)


import unittest

class TestSumOfTwoLargest(unittest.TestCase):
    
    def test_normal_case(self):
        arr = [3, 5, 1, 8, 2]
        result = sum_of_largest_number(arr)
        self.assertEqual(result, 13)
    
    def test_exact_two_elements(self):
        arr = [10, 20]
        result = sum_of_largest_number(arr)
        self.assertEqual(result, 30)

    def test_repeated_values(self):
        arr = [10, 10, 10, 10]
        result = sum_of_largest_number(arr)
        self.assertEqual(result, 20)

    def test_with_negative_numbers(self):
        arr = [-10, -20, -5, -15]
        result = sum_of_largest_number(arr)
        self.assertEqual(result, -15)

    def test_with_mixed_positive_and_negative_numbers(self):
        arr = [-1, 10, 3, -5]
        result = sum_of_largest_number(arr)
        self.assertEqual(result, 13)
        
    def test_negative_numbers_only(self):
        arr = [-50, -30, -100, -20, -40]
        result = sum_of_largest_number(arr)
        self.assertEqual(result, -50)
    
    def test_single_element_raises_error(self):
        arr = [5]
        with self.assertRaises(ValueError):
            sum_of_largest_number(arr)
    
    def test_empty_array_raises_error(self):
        arr = []
        with self.assertRaises(ValueError):
            sum_of_largest_number(arr)

if __name__ == "__main__":
    unittest.main()
