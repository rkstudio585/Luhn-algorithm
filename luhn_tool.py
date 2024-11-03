from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.progress import Progress
import pyfiglet
from rich import box
import os

console = Console()

class LuhnTool:
    def __init__(self, number):
        self.number = str(number)
    
    def validate(self):
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
        num_digits = len(self.number)
        checksum = 0
        is_second = False
        explanation = []
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Processing digits...", total=num_digits)
            
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
                progress.update(task, advance=1)

        explanation.append(f"\nTotal checksum: {checksum}")
        explanation.append(f"Result: {'Valid' if checksum % 10 == 0 else 'Invalid'}")
        return explanation, checksum % 10 == 0

    def save_results(self, results):
        with open("luhn_results.txt", "w") as file:
            file.write("\n".join(results))
        console.print("[green]Results saved to 'luhn_results.txt'.[/green]")

    def run_tool(self):
        # ASCII banner
        ascii_banner = pyfiglet.figlet_format("Luhn Tool", font="slant")
        console.print(f"[bold cyan]{ascii_banner}[/bold cyan]")
        
        while True:
            console.print("\n[bold green]Luhn Algorithm Tool Menu[/bold green]")
            console.print("1. Validate a Number")
            console.print("2. Generate Check Digit")
            console.print("3. Step-by-Step Validation Explanation")
            console.print("4. Validate Multiple Numbers")
            console.print("5. Save Results to File")
            console.print("6. Exit\n")
            
            choice = console.input("[yellow]Enter your choice (1-6): [/yellow]")
            if choice == '1':
                number = console.input("Enter the number to validate: ")
                if not number.isdigit():
                    console.print("[red]Invalid input! Please enter only digits.[/red]")
                    continue
                self.number = number
                is_valid = self.validate()
                console.print(f"[bold]Validation Result:[/bold] {'[green]Valid[/green]' if is_valid else '[red]Invalid[/red]'}")
            
            elif choice == '2':
                number = console.input("Enter the partial number (without the check digit): ")
                if not number.isdigit():
                    console.print("[red]Invalid input! Please enter only digits.[/red]")
                    continue
                self.number = number + "0"
                check_digit = self.generate_check_digit()
                console.print(f"[bold]Generated Check Digit:[/bold] [green]{check_digit}[/green]")
            
            elif choice == '3':
                number = console.input("Enter the number to explain validation: ")
                if not number.isdigit():
                    console.print("[red]Invalid input! Please enter only digits.[/red]")
                    continue
                self.number = number
                explanation, is_valid = self.explain_validation()
                table = Table(title="Luhn Algorithm Explanation", box=box.ROUNDED)
                table.add_column("Step", justify="left", style="cyan")
                table.add_column("Description", justify="left", style="magenta")
                
                for idx, step in enumerate(explanation, 1):
                    table.add_row(f"Step {idx}", step)
                
                console.print(table)
                console.print(f"[bold magenta]Final Checksum[/bold magenta]: [bold cyan]{'Valid' if is_valid else 'Invalid'}[/bold cyan]")
            
            elif choice == '4':
                numbers = console.input("Enter multiple numbers separated by spaces: ").split()
                results = []
                for num in numbers:
                    self.number = num
                    is_valid = self.validate()
                    results.append(f"{num}: {'Valid' if is_valid else 'Invalid'}")
                console.print("\n[bold]Validation Results for Multiple Numbers:[/bold]")
                for result in results:
                    console.print(result)
            
            elif choice == '5':
                if not os.path.exists("luhn_results.txt"):
                    console.print("[red]No results to save. Please validate numbers first.[/red]")
                else:
                    console.print("[green]Results have already been saved![/green]")
            
            elif choice == '6':
                console.print("[bold blue]Exiting the Luhn Algorithm Tool. Goodbye![/bold blue]")
                break
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")

# Example Usage
if __name__ == "__main__":
    LuhnTool("").run_tool()
