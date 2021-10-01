# coding: utf-8
import csv
from os import path
from pathlib import Path

#Automated Calculations.

# Automate the calculations for the loan portfolio summaries.
#     1. `len` function to calculate the total number of loans in the list.
#     2. `sum` function to calculate the total of all loans in the list.
#     3. Using the sum of all loans and the total number of loans, calculate the average loan price.
#     4. Print all calculations with descriptive messages.
loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print (f"there are {number_of_loans} number of loans.")

total_of_all_loans = sum(loan_costs)
print (f"the total value of the loans is: ", total_of_all_loans)

average_loan_price=total_of_all_loans/number_of_loans
print (f"the average loan amount is: ", average_loan_price)

    # Loan Data Analysis.

        # 1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    #     a. Save these values as variables called `future_value` and `remaining_months`.
    #     b. Print each variable.

    #     @NOTE:
    #     **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    #     **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

    # 2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
    # 3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    #     a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    #     b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    #     @NOTE:
    #     If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
    # """

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value= loan.get ("future_value")
remaining_months= loan.get ("remaining_months")
print (f"the future values is: ", future_value)
print (f" there are {remaining_months}  remaining months")

present_value=future_value / (1 + 0.20/12)** remaining_months
fair_value=present_value
print (f" the fair value is:", fair_value)

loan_price = loan.get ("loan_price")
if present_value >= loan_price:
    print ("the loan is worth at least the cost to buy it")

else:
    print("the loan is too expensive and not worth the price.")    
    
#Financial Calculations.

# Perform financial calculations using functions.

# 1. Define a new function that will be used to calculate present value.
#     a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#     b. The function should return the `present_value` for the loan.
# 2. Use the function to calculate the present value of the new loan given below.
#     a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value= new_loan.get ("future_value")
remaining_months= new_loan.get ("remaining_months")
def npv (future_value,  remaining_months, annual_discount_rate ):
    npv_new = future_value/ (1+annual_discount_rate/12) ** remaining_months
    return npv_new

 
print (f"The present value of the loan is: {npv (1000,  12, 0.2)}")



# 1. Create a new, empty list called `inexpensive_loans`.
# 2. Use a for loop to select each loan from a list of loans.
#     a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
#     b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
# 3. Print the list of inexpensive_loans.


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans= []

for loan in loans:
    if loan ["loan_price"] <= 500:
        inexpensive_loans.append(loan) 

print (f"the inexpensive loans are:",inexpensive_loans)


# Output this list of inexpensive loans to a csv file
#     1. Use `with open` to open a new CSV file.
#         a. Create a `csvwriter` using the `csv` library.
#         b. Use the new csvwriter to write the header variable as the first row.
#         c. Use a for loop to iterate through each loan in `inexpensive_loans`.
#             i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")

with open ("inexpensive_loans.csv","w", newline="") as csvfile:
    csvwriter=csv.writer(csvfile, delimiter= ",")
    csvwriter.writerow(header)
    for data in inexpensive_loans:
         csvwriter.writerow(data.values())
    