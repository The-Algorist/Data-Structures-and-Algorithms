# Camel Case Converter

This program takes a CamelCase string and converts it to either:

- Snake_case (for S;M command)
- UpperCamelCase (for C;C command)
- lowerCamelCase (for C;V command)
  
## Usage
To use this program, enter the input string in the following format:

'{S;M|C;C|C;V};input_string'

where {S;M|C;C|C;V} specifies the conversion type and input_string is the CamelCase string to be converted.

### Example

Input:

S;M;myVariableName

Output:

my_variable_name

Input:

C;C;myFunctionName

Output:

MyFunctionName

## Edge Cases

The program has the following edge cases:

- Empty input string
- Incorrect command format
- Incorrect semicolon delimiter
- Incorrect conversion type
- Invalid CamelCase input string format
- Unexpected end of file
- 
If any of these edge cases is encountered, the program will return an error message.

## Time and Space Complexity

The time complexity of this program is O(n), where n is the length of the input string. This is because the program goes through the input string character by character.

The space complexity of this program is also O(n), where n is the length of the input string. This is because the program creates a new string for the converted output, which has the same length as the input string.