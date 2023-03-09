# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

import math
import os
import random
import re
import sys

# Complete timeConversion function below.
def timeConversion(s):
    # Use try-except to catch any errors when parsing the input string
    try:
        # Parse the hour, minute, and second values from the input string
        hour, minute, second = map(int, s[:-2].split(':'))
        period = s[-2:]
        
        # Check if the input string is in the correct format
        if hour < 0 or hour > 12 or minute < 0 or minute > 59 or second < 0 or second > 59:
            raise ValueError("Invalid input string")
        
        # Convert the hour value to 24-hour format
        if period == 'PM' and hour != 12:
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0
        
        # Format the output string in 24-hour format
        return f"{hour:02d}:{minute:02d}:{second:02d}"
    
    except (ValueError, TypeError):
        # Return an empty string if the input string is invalid or cannot be parsed
        return ""
