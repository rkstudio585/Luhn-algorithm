# Luhn algorithm

---
![luhn](logo.svg)

# Luhn Algorithm Tool

Welcome to the **Luhn Algorithm Tool**! This tool provides an interactive way to validate numbers using the Luhn algorithm, generate check digits, and view step-by-step explanations of the algorithm’s validation process. With its menu-driven interface and enhanced visual feedback, it’s designed to be educational, user-friendly, and feature-rich.

## Table of Contents

- [Working logic txt](working-behaviour.txt)
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)
- [Code Structure](#code-structure)
- [Contributing](#contributing)

---
### Applications of the Luhn Algorithm
The Luhn algorithm is commonly used in:
- **Credit card numbers** (like Visa, MasterCard, and American Express).
- **Debit card numbers**.
- **IMEI numbers** (for identifying mobile devices).
- **Canadian Social Insurance Numbers (SIN)**.

---
## Research Links

Here are some links to resources and research materials about the Luhn Algorithm:

1. **Wikipedia - Luhn Algorithm**  
   [Wikipedia Luhn Algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm)  
   A comprehensive overview of the algorithm, its history, and applications.

2. **IBM - The Check Digit Algorithm**  
   [IBM Luhn Algorithm](https://www.ibm.com/docs/en/zos/2.2.0?topic=SSLTBW_2.2.0/com.ibm.zos.v2r2.idai100/valid.htm)  
   An explanation of the check digit algorithm as implemented by IBM, highlighting its use in financial and identification contexts.

3. **Khan Academy - Check Digits and the Luhn Algorithm**  
   [Khan Academy Luhn Algorithm](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/check-digits)  
   A clear, educational explanation of check digits and the Luhn algorithm with examples.

4. **The Luhn Algorithm in Credit Card Validation**  
   [Credit Card Validation using Luhn](https://www.creditcardvalidator.org/articles/luhn-algorithm)  
   This article explains the role of the Luhn algorithm in credit card validation, including practical insights.

5. **NIST - Algorithm Specifications for Digital Signatures**  
   [NIST - Digital Signature Algorithm](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)  
   While not solely focused on the Luhn algorithm, this document from the National Institute of Standards and Technology discusses digital algorithms and provides broader context.

6. **Medium - Understanding the Luhn Algorithm**  
   [Medium Article on Luhn Algorithm](https://medium.com/@alyssaxuu/understanding-the-luhn-algorithm-d07e4cdb01b4)  
   An easy-to-follow guide explaining the Luhn algorithm in a modern context, with example implementations.

---
## Overview

The **Luhn Algorithm Tool** is a Python-based program designed to help users work with the Luhn algorithm in a convenient and visually appealing way. The Luhn algorithm is widely used for validating identification numbers, like credit card numbers, and is a crucial tool in financial and security-related applications. This tool goes beyond basic validation by offering features such as check digit generation, step-by-step explanations with progress tracking, and the ability to validate multiple numbers at once.

## Features

- **Number Validation**: Check if a number is valid according to the Luhn algorithm.
- **Check Digit Generation**: Calculate the correct check digit for a given partial number.
- **Detailed Explanation**: View a step-by-step breakdown of the validation process, with each stage clearly explained.
- **Multiple Number Validation**: Validate multiple numbers at once by entering them as a space-separated list.
- **Result Saving**: Optionally save all validation results to a text file (`luhn_results.txt`).
- **Professional Styling**: Uses the `rich` library for polished, colorful output and the `pyfiglet` library for a striking ASCII banner at the start.
- **Interactive Menu**: A user-friendly interface that guides users through each feature.

## Installation

To get started, clone the repository and install the necessary Python libraries.

```bash
pip install rich pyfiglet
git clone https://github.com/rkstudio585/Luhn-algorithm.git
cd Luhn-algorithm
```

## Usage

To launch the tool, run the following command:

```bash
python luhn_tool.py
```

You’ll see an ASCII banner welcoming you, followed by an interactive menu with several options.

## Options

Upon starting, the tool provides a menu where you can select from the following options:

1. **Validate a Number**: Checks if a single number is valid according to the Luhn algorithm.
2. **Generate Check Digit**: Calculates the check digit for a given partial number.
3. **Step-by-Step Validation Explanation**: Provides a detailed breakdown of each calculation step in the Luhn algorithm, including a progress bar to visualize the process.
4. **Validate Multiple Numbers**: Enter multiple numbers separated by spaces, and the tool will validate each number in sequence.
5. **Save Results to File**: Saves validation results to a file called `luhn_results.txt` for easy reference.
6. **Exit**: Closes the tool.

## Examples

### 1. Validating a Single Number
If you select option **1**, enter the number you want to validate. The tool will display whether the number is valid.

**Example Output**:
```csharp
Enter the number to validate: 79927398713
Validation Result: Valid
```

### 2. Generating a Check Digit
Select option **2** and enter the partial number (without the check digit). The tool will calculate and display the check digit.

**Example Output**:
```csharp
Enter the partial number (without the check digit): 7992739871
Generated Check Digit: 3
```

### 3. Step-by-Step Explanation
Choose option **3** to get a detailed breakdown of the validation process, including calculations for each step in the algorithm. This option is helpful for understanding how the Luhn algorithm processes each digit.

### 4. Validating Multiple Numbers
To validate multiple numbers, choose option **4** and enter each number separated by a space. The tool will validate each one and display the results in sequence.

**Example Input**:
```csharp
Enter multiple numbers separated by spaces: 79927398713 1234567812345670
```

**Example Output**:
```csharp
79927398713: Valid
1234567812345670: Invalid
```

### 5. Saving Results to File
After validating numbers, choose option **5** to save all results to a file named `luhn_results.txt`. You’ll see a confirmation message once the file is created.

---

## Code Structure

- **LuhnTool Class**: The main class that houses all functions related to validation, check digit generation, and explanations.
  - **validate()**: Checks if a number is valid according to the Luhn algorithm.
  - **generate_check_digit()**: Calculates the correct check digit for a partial number.
  - **explain_validation()**: Provides a step-by-step explanation of the validation process.
  - **save_results()**: Saves the validation results to a file.
- **Menu Logic**: The interactive menu allows users to choose from various options, directing them to the appropriate functionality.

---

## Contributing

Contributions to this project are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to submit a pull request.

---

Thank you for using the **Luhn Algorithm Tool**! If you have any questions or feedback, feel free to reach out through GitHub issues or submit a pull request to help improve the tool.
