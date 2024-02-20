def hexToDecimal(hexString):
    """
    Converts a hexadecimal string to its decimal equivalent.
    :param hexString: str, hexadecimal string
    :return: int, decimal equivalent
    """
    return int(hexString, 16)

def decimalToBinary(decimalValue):
    """
    Converts a decimal number to its binary string representation.
    :param decimalValue: int, decimal number
    :return: str, binary string representation
    """
    return bin(decimalValue)[2:]  # bin() returns binary string prefixed with '0b', so slice it off.

# Example usage (not necessary for the assignment, just for student testing)
if __name__ == "__main__":
    # Hexadecimal to Decimal
    print("Hexadecimal 'A' to Decimal:", hexToDecimal('A'))
    print("Hexadecimal '1A' to Decimal:", hexToDecimal('1A'))

    # Decimal to Binary
    print("Decimal 2 to Binary:", decimalToBinary(2))
    print("Decimal 5 to Binary:", decimalToBinary(5))
