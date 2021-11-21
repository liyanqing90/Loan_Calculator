import math
import argparse

error_msg = "Incorrect parameters"

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
de_type = args.type
payment = int(args.payment) if args.payment is not None else args.payment
principal = int(args.principal) if args.principal is not None else args.principal
periods = int(args.periods) if args.periods is not None else args.periods
interest = float(args.interest) if args.interest is not None else args.interest
if de_type not in ["annuity", "diff"]:
    print(error_msg)
else:
    if de_type == "diff" and args.payment:
        print(1)
        print(error_msg)
    else:
        if interest is None or interest < 0:
            print(2)
            print(error_msg)
        else:
            a_list = [i for i in [payment, principal, periods] if i]
            if len(a_list) < 2:
                print(3)
                print(error_msg)
            else:
                if [i for i in a_list if i < 0]:
                    print(4)
                    print(error_msg)
                else:
                    i = interest / 100 / 12
                    if de_type == "diff":
                        all_pay = 0
                        for m in range(1, periods + 1):
                            payment = math.ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
                            all_pay += payment
                            print(f"Month {m}: payment is {payment}")
                        print()
                        print(f"Overpayment = {all_pay - principal}")
                    else:
                        if all([principal, periods]):
                            payment = math.ceil(principal * (i * ((1 + i) ** periods) / ((1 + i) ** periods - 1)))
                            Overpayment = payment * periods - principal
                            print(f"Your annuity payment = {payment}!")
                            print(f"Overpayment = {Overpayment}")
                        elif all([payment, periods]):
                            principal = math.floor(payment / (i * ((1 + i) ** periods) / ((1 + i) ** periods - 1)))
                            Overpayment = payment * periods - principal
                            print(f'Your loan principal = {principal}!')
                            print(f"Overpayment = {Overpayment}")
                        elif all([principal, payment]):
                            periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
                            Overpayment = payment * periods - principal
                            year = periods // 12
                            if year:
                                periods = periods % 12
                            if year:
                                if periods:
                                    print(f"It will take {year} years and {periods} months to repay this loan!")
                                else:
                                    print(f"It will take {year} years to repay this loan!")
                            else:
                                print(f"It will take {periods} months to repay this loan!")
                            print(f"Overpayment = {Overpayment}")
