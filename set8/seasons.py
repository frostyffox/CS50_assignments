from datetime import date
import sys
import re

def main():
    # Get date of birth from user
    birthd = input("Date of Birth: ").strip()

    # Validate date format
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", birthd):
        sys.exit("Invalid date")

    try:
        y,m,d = map(int, birthd.split("-"))
        dob = date(y,m,d)
    except ValueError:
        sys.exit("Invalid date")

    # Calculate minutes between dates
    minutes = get_minutes(dob)

    # Convert to words and print
    words = number_to_words(minutes)
    print(f"{words} minutes")

def get_minutes(bd):
    today = date.today()
    days = (today - bd).days
    return days * 24 * 60

def number_to_words(n):
    if n == 0:
        return "Zero"

    # Handle large numbers by breaking into chunks
    units = ["", "thousand", "million", "billion"]
    words = []

    # Process number in chunks of 3 digits
    chunk_index = 0
    while n > 0:
        chunk = n % 1000
        if chunk > 0:
            chunk_words = convert_chunk(chunk)
            if units[chunk_index]:
                chunk_words += " " + units[chunk_index]
            words.append(chunk_words)
        n //= 1000
        chunk_index += 1

    # Reverse to get correct order (largest first)
    words.reverse()

    # Join with commas between major units
    result = ", ".join(words)
    return result.capitalize()

def convert_chunk(n):

    ones = ["", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen",
             "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_words = ["", "", "twenty", "thirty", "forty", "fifty",
                  "sixty", "seventy", "eighty", "ninety"]

    parts = []

    if n >= 100:
        parts.append(ones[n // 100] + " hundred")
        n %= 100
    if n >= 20:
        tens_digit = n // 10
        ones_digit = n % 10
        if ones_digit > 0:
            parts.append(tens_words[tens_digit] + "-" + ones[ones_digit])
        else:
            parts.append(tens_words[tens_digit])
    elif n >= 10:
        parts.append(teens[n - 10])
    elif n > 0:
        parts.append(ones[n])

    return " ".join(parts)

if __name__ == "__main__":
    main()
