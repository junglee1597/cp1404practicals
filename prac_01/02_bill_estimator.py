def exchange_cent(value):
    cent = value / 100
    return cent


def estimated_bill(cent,daily,days):
    bill = cent * daily * days
    print("Estimated bill: %.2f" % bill)


def main():
    print("Electricity bill estimator")
    cents = int(input("Enter cents per kWh: "))
    daily_used = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    estimated_bill(exchange_cent(cents),daily_used,billing_days)


main()
