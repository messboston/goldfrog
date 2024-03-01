# GoldFrog Personal Finance Manager

## Overview

GoldFrog is a Python-based personal finance manager designed to help users track their expenses, incomes, investments, and financial goals efficiently. This command-line application offers a user-friendly interface for managing personal finances without the complexity of graphical tools.

## Features

- **Expense Tracking**: Log and categorize your daily expenses to keep an eye on your spending.
- **Income Management**: Record different sources of income to get a clear picture of your financial inflow.
- **Investment Portfolio**: Keep track of your investments, including stocks, bonds, and other assets.
- **Financial Goals**: Set and monitor progress towards your financial goals, such as saving for a vacation or purchasing a home.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository to your local machine:

git clone https://github.com/yourusername/goldfrog.git
cd goldfrog


2. (Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. No external dependencies are required to run the application as it uses Python's standard library.

### Running GoldFrog

To start the application, run:

python main.py

Follow the on-screen prompts to manage your finances.

## How to Use

After launching GoldFrog, you will be presented with a menu of options:

1. **Add Expense**: Record a new expense by specifying the amount and category.
2. **Add Income**: Log a new income source along with the amount.
3. **Add Investment**: Add details of your investments.
4. **Set Financial Goal**: Specify a financial goal and target amount.
5. **View Financial Summary**: Get an overview of your financial status.
6. **Exit**: Quit the application.

Select an option by entering the corresponding number and follow the prompts to enter the required information.

## Data Persistence

GoldFrog saves your financial data in a file named `data.json` within the application's directory. This file ensures that your data is persisted across sessions.

## Contributing

We welcome contributions to GoldFrog! If you have suggestions for improvements or bug fixes, please open an issue or a pull request.

## License

GoldFrog is released under the MIT License. See the LICENSE file for more details.
