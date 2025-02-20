import random

# Monthly Budget Allocator for Nabiha
def main():
    try:
        month = input("Enter the month you are storing the salary for: ")
        salary = float(input("Enter your salary for the month: "))
        
        # Get custom percentage allocations
        savings_pct = float(input("Enter the percentage for Savings: ")) / 100
        rent_pct = float(input("Enter the percentage for Rent: ")) / 100
        electricity_pct = float(input("Enter the percentage for Electricity: ")) / 100
        
        # Calculate allocations
        savings = salary * savings_pct
        rent = salary * rent_pct
        electricity = salary * electricity_pct
        
        total_expenses = savings + rent + electricity
        remaining_salary = salary - total_expenses
        
        yearly_rent = rent * 12
        yearly_electricity = electricity * 12
        
        squared_salary = salary ** 2
        
        additional_savings = 50
        savings_divided = additional_savings / savings if savings != 0 else 0

if __name__ == "__main__":
    main()
