# Time Conversion Algorithm

This is a Python function that converts a string representing a time in 12-hour format to 24-hour format. The function takes a single parameter, 's', which is a string in the format "hh:mm:ssAM/PM", where:

- 'hh' is an integer between 01 and 12, representing the hour of the day
- 'mm' is an integer between 00 and 59, representing the minute of the  hour
- 'ss' is an integer between 00 and 59, representing the second of the minute
- 'AM/PM' is a string representing either "AM" or "PM", indicating whether the time is before or after noon.
  
## Usage

To use the timeConversion function in your Python code, simply import the function and call it with a valid input string. The function returns a string representing the same time in 24-hour format, in the format "hh:mm:ss".

Here's an example usage of the function:

``` PYTHON

from time_conversion import timeConversion

input_string = "07:05:45PM"
output_string = timeConversion(input_string)

print("Input: ", input_string)
print("Output: ", output_string)

```

This would output:

``` MAKEFILE
Input:  07:05:45PM
Output:  19:05:45
```

## Edge Cases

The following are the edge cases of this algorithm:

1. Incorrectly formatted input string: The algorithm assumes that the input string is in the format "hh:mm:ssAM/PM", where "hh" is an integer between 1 and 12, "mm" is an integer between 0 and 59, "ss" is an integer between 0 and 59, and "AM/PM" is either "AM" or "PM". If the input string is not formatted correctly, the function may produce unexpected results or raise an error.

2. Input time is exactly 12:00:00 AM or 12:00:00 PM: In 12-hour format, 12:00:00 AM represents midnight, and 12:00:00 PM represents noon. In 24-hour format, these times are represented as 00:00:00 and 12:00:00, respectively. The algorithm must be able to handle these special cases correctly.

3. Input hour is outside the valid range: The hour value in the input string must be between 1 and 12, inclusive. If the input hour is less than 1 or greater than 12, the function may produce unexpected results or raise an error.

4. Input minute or second is outside the valid range: The minute and second values in the input string must be between 0 and 59, inclusive. If either value is less than 0 or greater than 59, the function may produce unexpected results or raise an error.

5. Empty input string: If the input string is empty, the function may produce unexpected results or raise an error.

## Complexity

The timeConversion function has a time complexity of O(1), which means that its running time does not depend on the size of the input. The space complexity of the function is also O(1), meaning that it uses only a fixed amount of memory to store its variables and intermediate results.

Overall, this algorithm is efficient and can handle large inputs efficiently and without using excessive memory.

### Contributing

Contributions to this project are welcome! If you find a bug, or have an idea for an improvement or feature, please feel free to open an issue or submit a pull request on the GitHub repository.