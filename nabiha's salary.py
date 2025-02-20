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

        # Output results
        print(f"\nBudget Allocation for {month}:")
        print(f"Savings: ${savings:.2f}")
        print(f"Rent: ${rent:.2f}")
        print(f"Electricity: ${electricity:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Salary: ${remaining_salary:.2f}")
        print(f"Estimated Yearly Rent: ${yearly_rent:.2f}")
        print(f"Estimated Yearly Electricity Cost: ${yearly_electricity:.2f}")
        print(f"Salary squared (just for fun!): {squared_salary:.2f}")
        print(f"Additional savings of $50 divided by savings: {savings_divided:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter numerical values where required.")

if __name__ == "__main__":
    main()
