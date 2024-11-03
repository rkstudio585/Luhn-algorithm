def luhn_generate_check_digit(number):
    """
    Given a number, calculate and append its Luhn check digit to make it valid.
    """
    digits = [int(d) for d in str(number)]
    checksum = 0
    
    # Start from the rightmost digit and double every second digit
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        
        # Double every second digit (counting from right)
        if (len(digits) - i) % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        checksum += digit
    
    # Determine check digit that makes sum a multiple of 10
    check_digit = (10 - (checksum % 10)) % 10
    return check_digit

# Example Usage: Generate check digit for 7992739871
print("Check digit:", luhn_generate_check_digit(7992739871))  # Output: 3
