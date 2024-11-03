class LuhnTool:
    def __init__(self, number):
        self.number = str(number)
    
    def validate(self):
        """
        Validates the number using the Luhn algorithm.
        Returns True if the number is valid, otherwise False.
        """
        checksum = 0
        num_digits = len(self.number)
        is_second = False
        
        for i in range(num_digits - 1, -1, -1):
            digit = int(self.number[i])
            
            if is_second:
                digit = digit * 2
                if digit > 9:
                    digit -= 9
            checksum += digit
            is_second = not is_second

        return checksum % 10 == 0

    def generate_check_digit(self):
        """
        Calculates the Luhn check digit for the number (excluding the last digit).
        Returns the check digit that should be appended to make the number valid.
        """
        partial_number = self.number[:-1]
        checksum = 0
        num_digits = len(partial_number) + 1
        is_second = True
        
        for i in range(len(partial_number) - 1, -1, -1):
            digit = int(partial_number[i])
            
            if is_second:
                digit = digit * 2
                if digit > 9:
                    digit -= 9
            checksum += digit
            is_second = not is_second
        
        check_digit = (10 - (checksum % 10)) % 10
        return check_digit
    
    def explain_validation(self):
        """
        Provides a step-by-step explanation of the Luhn validation process.
        """
        num_digits = len(self.number)
        checksum = 0
        is_second = False
        explanation = []
        
        for i in range(num_digits - 1, -1, -1):
            digit = int(self.number[i])
            original_digit = digit
            
            if is_second:
                digit = digit * 2
                if digit > 9:
                    digit -= 9
                explanation.append(f"Doubling {original_digit} gives {original_digit * 2} -> Adjusted to {digit}")
            else:
                explanation.append(f"Unchanged {original_digit}")
            
            checksum += digit
            is_second = not is_second

        explanation.append(f"\nTotal checksum: {checksum}")
        explanation.append(f"Result: {'Valid' if checksum % 10 == 0 else 'Invalid'}")
        return "\n".join(explanation)

    def run_tool(self):
        """
        Runs the Luhn tool, providing options for validation, check digit generation, 
        and explanation of the process.
        """
        print("Luhn Algorithm Tool")
        print("===================")
        print(f"Input Number: {self.number}\n")
        
        # Validation
        is_valid = self.validate()
        print("1. Validation Result:")
        print(f"   {'The number is valid.' if is_valid else 'The number is invalid.'}\n")
        
        # Check digit generation
        check_digit = self.generate_check_digit()
        print("2. Check Digit Generation:")
        print(f"   The correct check digit for {self.number[:-1]} is: {check_digit}\n")
        
        # Explanation of validation process
        print("3. Step-by-Step Validation Explanation:")
        print(self.explain_validation())
        print("\n")

# Example Usage
if __name__ == "__main__":
    # Sample number (change this as needed)
    number = input("Enter the number to validate and explain using Luhn's algorithm: ")
    tool = LuhnTool(number)
    tool.run_tool()
  
