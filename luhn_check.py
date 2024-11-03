def luhn_check(card_number):
    card_number = [int(digit) for digit in str(card_number)]
    checksum = 0
    
    # Process each digit from right to left
    for i in range(len(card_number) - 1, -1, -1):
        digit = card_number[i]
        
        # Double every second digit
        if (len(card_number) - i) % 2 == 0:
            digit *= 2
            # If doubling makes the digit > 9, subtract 9
            if digit > 9:
                digit -= 9
        
        # Add the processed digit to checksum
        checksum += digit
    
    # Check if the checksum is a multiple of 10
    return checksum % 10 == 0

# Test the function with an example card number
print(luhn_check(4539148803436467))  # Output: False (invalid)
