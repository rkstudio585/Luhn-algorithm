import os

class AdvancedLuhnTool:
    def __init__(self):
        self.log_file = "luhn_log.txt"
    
    def validate(self, number):
        checksum = 0
        num_digits = len(number)
        is_second = False
        
        for i in range(num_digits - 1, -1, -1):
            digit = int(number[i])
            if is_second:
                digit = digit * 2
                if digit > 9:
                    digit -= 9
            checksum += digit
            is_second = not is_second

        return checksum % 10 == 0

    def generate_check_digit(self, number):
        partial_number = number
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

    def explain_validation(self, number):
        num_digits = len(number)
        checksum = 0
        is_second = False
        explanation = []
        
        for i in range(num_digits - 1, -1, -1):
            digit = int(number[i])
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

    def batch_validate(self, numbers):
        results = {}
        for number in numbers:
            valid = self.validate(number)
            results[number] = valid
        return results

    def log_result(self, content):
        with open(self.log_file, 'a') as file:
            file.write(content + "\n")
    
    def detect_common_errors(self, number):
        corrections = []
        # Check for single-digit errors
        for i in range(len(number)):
            for replacement in "0123456789":
                if number[i] != replacement:
                    test_number = number[:i] + replacement + number[i+1:]
                    if self.validate(test_number):
                        corrections.append(f"Single digit correction at index {i}: {test_number}")
        
        # Check for transposition errors
        for i in range(len(number) - 1):
            transposed = list(number)
            transposed[i], transposed[i + 1] = transposed[i + 1], transposed[i]
            transposed_number = ''.join(transposed)
            if self.validate(transposed_number):
                corrections.append(f"Transposition correction between index {i} and {i + 1}: {transposed_number}")
        
        return corrections if corrections else ["No common errors detected."]
    
    def run(self):
        while True:
            print("\nAdvanced Luhn Algorithm Tool")
            print("===========================")
            print("1. Validate a Number")
            print("2. Generate a Check Digit")
            print("3. Explain Validation Process")
            print("4. Batch Validate Multiple Numbers")
            print("5. Detect Common Errors")
            print("6. View Log")
            print("7. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                number = input("Enter number to validate: ")
                is_valid = self.validate(number)
                result = f"Validation result: {'Valid' if is_valid else 'Invalid'}"
                print(result)
                self.log_result(result)
            
            elif choice == "2":
                number = input("Enter number (without check digit): ")
                check_digit = self.generate_check_digit(number)
                result = f"Check digit for {number} is: {check_digit}"
                print(result)
                self.log_result(result)

            elif choice == "3":
                number = input("Enter number to explain validation: ")
                explanation = self.explain_validation(number)
                print(explanation)
                self.log_result(f"Explanation for {number}:\n{explanation}")

            elif choice == "4":
                numbers = input("Enter numbers separated by commas: ").split(',')
                results = self.batch_validate(numbers)
                for number, valid in results.items():
                    print(f"{number}: {'Valid' if valid else 'Invalid'}")
                    self.log_result(f"{number}: {'Valid' if valid else 'Invalid'}")
            
            elif choice == "5":
                number = input("Enter number to check for common errors: ")
                corrections = self.detect_common_errors(number)
                for correction in corrections:
                    print(correction)
                self.log_result(f"Common errors for {number}: {', '.join(corrections)}")
            
            elif choice == "6":
                if os.path.exists(self.log_file):
                    with open(self.log_file, 'r') as file:
                        print("\nLog File Content:")
                        print(file.read())
                else:
                    print("No log file found.")
            
            elif choice == "7":
                print("Exiting the tool. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Run the tool
if __name__ == "__main__":
    tool = AdvancedLuhnTool()
    tool.run()
