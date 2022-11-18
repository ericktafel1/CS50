# Define main function, dollars, percent and tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Define dollars, convert to float and remove $ sign
def dollars_to_float(d):
    d_no_sign = d.replace("$", "")
    return float(d_no_sign)

# Define tip, convert to float, divide by 100 and remove % sign
def percent_to_float(p):
    p_no_percent = p.replace("%", "")
    p_divided = float(p_no_percent) / 100
    return float(p_divided)

main()