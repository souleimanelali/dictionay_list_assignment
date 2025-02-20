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
        

if __name__ == "__main__":
    main()
