def romanToInt(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.

    Args:
        s: The Roman numeral string.

    Returns:
        The integer representation of the Roman numeral.
    """

    rv = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and (rv[s[i]] < rv[s[i + 1]]):
            result += rv[s[i + 1]] - rv[s[i]]
            i += 2
        else:
            result += rv[s[i]]
            i += 1
    return result

# Example Usage:
print(romanToInt("III"))    # Output: 3
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV")) # Output: 1994
