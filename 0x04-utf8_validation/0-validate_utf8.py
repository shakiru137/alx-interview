#!/usr/bin/python3
"""  UTF-8 Validation """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The list of integers representing the data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    # Mask to check if the leading bits are correct
    mask1 = 1 << 7   # 10000000
    mask2 = 1 << 6   # 01000000

    for num in data:
        # Get the 8 least significant bits of the integer
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine how many bytes in this UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character must start with 0xxxxxxx
                return False
        else:
            # For multibyte characters,check ifthe byte starts with '10xxxxxx'
            if not (byte >> 6 == 0b10):  # The byte should start with 10xxxxxx
                return False
            num_bytes -= 1

    return num_bytes == 0
