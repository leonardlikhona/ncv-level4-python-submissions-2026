import random

def generate_minutes():
    """Generate and return a random integer between 30 and 180, inclusive."""
    return random.randint(30, 180)

def calc_amount(machine_type, minutes):
    """Calculate and return the amount before VAT based on machine type and minutes used."""
    # Convert minutes to hours (fractional hours calculated proportionally)
    hours = minutes / 60.0
    
    # Determine costs based on machine type
    if machine_type.upper() == 'A':
        initial_cost = 50.00
        hourly_rate = 30.00
    elif machine_type.upper() == 'B':
        initial_cost = 62.50
        hourly_rate = 36.25
    elif machine_type.upper() == 'C':
        initial_cost = 74.87
        hourly_rate = 40.50
    else:
        initial_cost = 0.00
        hourly_rate = 0.00
        
    amount_before_vat = initial_cost + (hourly_rate * hours)
    return amount_before_vat

def calc_total_amount(amount):
    """Calculate VAT (14%) and total payable, returning both."""
    vat_amount = amount * 0.14
    total_payable = amount + vat_amount
    return vat_amount, total_payable

def display_summary(payment):
    """Receive the payments list and display the daily summary statistics."""
    num_customers = len(payment)
    
    if num_customers == 0:
        print("\nNo customers were processed today.")
        return

    combined_amount = sum(payment)
    average_payment = combined_amount / num_customers
    highest_payment = max(payment)
    lowest_payment = min(payment)

    print("\n" + "=" * 40)
    print("        DAILY PAYMENT SUMMARY")
    print("=" * 40)
    print(f"Number of customers processed : {num_customers}")
    print(f"Combined amount payable       : R{combined_amount:.2f}")
    print(f"Average payment per customer  : R{average_payment:.2f}")
    print(f"Highest payment               : R{highest_payment:.2f}")
    print(f"Lowest payment                : R{lowest_payment:.2f}")
    print("=" * 40)

def process_payment():
    """Manage the customer input loop, invoice generation, and summary call."""
    num_customers = int(input("Enter the number of customers to process: "))
    payments = []

    for i in range(1, num_customers + 1):
        print(f"\n--- Customer {i} ---")
        customer_name = input("Enter customer's name: ")
        machine_type = input("Enter machine type (A, B, or C): ").upper()

        # Generate minutes and calculate amounts
        minutes = generate_minutes()
        amount_before_vat = calc_amount(machine_type, minutes)
        vat_amount, total_payable = calc_total_amount(amount_before_vat)

        # Append total payable to the list
        payments.append(total_payable)

        # Display individual invoice
        print("\n" + "-" * 30)
        print("          INVOICE")
        print("-" * 30)
        print(f"Customer Name     : {customer_name}")
        print(f"Machine Type      : {machine_type}")
        print(f"Generated Minutes : {minutes} mins ({minutes / 60:.2f} hrs)")
        print(f"Amount before VAT : R{amount_before_vat:.2f}")
        print(f"VAT Amount (14%)  : R{vat_amount:.2f}")
        print(f"Total Payable     : R{total_payable:.2f}")
        print("-" * 30)

    # After processing all customers, pass the list to display_summary
    display_summary(payments)

# Start the program
if __name__ == "__main__":
    process_payment()