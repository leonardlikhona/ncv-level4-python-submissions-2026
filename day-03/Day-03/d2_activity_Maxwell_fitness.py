# Facility pricing dictionary based on Maxwell Fitness Centre rates
facility = {
    "squa": {"name": "Squash court", "rate": 13.00},
    "swim": {"name": "Swimming pool", "rate": 12.00},
    "gym": {"name": "Gymnasium", "rate": 11.00},
    "wei": {"name": "Weights", "rate": 8.00}
}

def calculate_payment(hours_used, hourly_rate):
    """
    Calculates the total payment based on the hours used and the hourly rate.
    """
    return hours_used * hourly_rate

def display_receipt(facility_name, hours_used, hourly_rate, total_payment):
    """
    Displays a formatted receipt of the customer's payment.
    """
    print("\n" + "=" * 45)
    print("         MAXWELL FITNESS CENTRE RECEIPT         ")
    print("=" * 45)
    print(f"Facility Used  : {facility_name}")
    print(f"Hours Used     : {hours_used:.2f} hrs")
    print(f"Rate per Hour  : R{hourly_rate:.2f}")
    print("-" * 45)
    print(f"Total Payment  : R{total_payment:.2f}")
    print("=" * 45)

def main():
    print("Welcome to Maxwell Fitness Centre!")
    print("\nAvailable Facilities and Codes:")
    print("-" * 35)
    print("Code\tFacility\t\tRate per hour")
    print("-" * 35)
    for code, details in facility.items():
        print(f"{code}\t{details['name']}\t\tR{details['rate']:.2f}")
    print("-" * 35)
    
    # Get user input for facility code
    code_input = input("\nEnter the facility code (e.g., squa, swim, gym, wei): ").strip().lower()
    
    if code_input not in facility:
        print("Error: Invalid facility code entered. Please restart and try again.")
        return
        
    try:
        # Get hours used
        hours = float(input("Enter the number of hours used: "))
        
        if hours < 0:
            print("Error: Hours used cannot be negative.")
            return
            
        # Retrieve facility details
        facility_name = facility[code_input]["name"]
        hourly_rate = facility[code_input]["rate"]
        
        # Calculate payment using the function
        total_amount = calculate_payment(hours, hourly_rate)
        
        # Display the result using the function
        display_receipt(facility_name, hours, hourly_rate, total_amount)
        
    except ValueError:
        print("Invalid input! Please enter a numerical value for the hours.")

if __name__ == "__main__":
    main()