# Description: The One  Stop  Insurance  Companyneeds  a  program  to  enter  and  calculate  new  insurance  policy information for its customers. Allow the program to repeat to allow the user to enter as many customers as  they  want.    Add  at  least  3  functions  to  the  program.    I  will  accept  the  FormatValues.pylibrary  as  a function option –but  you need to add a new  function to the  library–make  it relevant.Bonus point–actually just my admiration-if you can create a function that returns multiple values.
# Author: Kyle Hollett
# Date(s): 2024-03-16



# Define Libraries
import datetime
import FormatValues as FV
import re

# Define Constants

BASIC_PREMIUM = 869.00
DISCOUNT_ADDITIONAL_CARS = 0.25
COST_EXTRA_LIABILITY = 130.00
COST_GLASS_COVERAGE = 86.00
COST_LOANER_CAR_COVERAGE = 58.00
HST_RATE = 0.15
PROCESSING_FEE_MONTHLY_PAYMENT = 39.99
PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
PAYMENT_OPTIONS = ['Full', 'Monthly', 'Down Pay']


Claims = [
    {"ClaimNumber": "0001", "ClaimDate": "2023-01-15", "ClaimAmount": 1000.00},
    {"ClaimNumber": "0002", "ClaimDate": "2023-06-20", "ClaimAmount": 500.00},
    {"ClaimNumber": "0003", "ClaimDate": "2024-02-10", "ClaimAmount": 750.00}
]


# Define Program Functions

def get_valid_province():
    Province = input("Enter province abbreviation (ex: NL): ").upper()
    while Province not in PROVINCES:
        print("Invalid province. Please enter a valid province.")
        Province = input("Enter province abbreviation (ex: NL): ").upper()
    return Province

def get_payment_option():
    while True:
        PaymentOption = input("Payment Option (Full/Monthly/Down Pay): ").title()

        if PaymentOption not in PAYMENT_OPTIONS:
          print("Invalid payment option")
        else:
            return PaymentOption
        break
def calculate_monthly_payment(TotalCost, DownPayment):
    if DownPayment > 0:
        TotalCost -= DownPayment
    MonthlyPayment = (TotalCost + PROCESSING_FEE_MONTHLY_PAYMENT) / 8
    return MonthlyPayment

def display_previous_claims(claims):
    print("Previous Claims:")
    print("Claim #     Claim Date    Amount")
    print("---------------------------------")
    for claim in claims:
        print(f"{claim['ClaimNumber']}{claim['ClaimDate']}${claim['ClaimAmount']:.2f}")

# Main Program 


    #Inputs
PolicyNumber = 1944     
while True: #Below needs valdations - fixed
    print("Enter customer information below:")
    print()

    while True:
        FirstName = input("Enter customer's first name: ").title()
        if FV.validate_name(FirstName):
            break
        else:
            print("Invalid input. Please enter a valid first name.")

    while True:
        LastName = input("Enter customer's last name: ").title()
        if FV.validate_name(LastName):
            break
        else:
            print("Invalid input. Please enter a valid last name.")
    while True:
        StAddress = input("Enter customers street address: ") #Maybe validate - validated
        if FV.validate_street_address(StAddress):
            break
        else:
            print("Invalid street address. Input valid street address")
    
    while True:
        City = input("Enter customers City: ").title() #Maybe validate - validated
        if FV.validate_city(City):
            break
        else: 
            print("Invalid input. Please enter a valid city name.")


    Province = get_valid_province() 

    while True:
        PostalCode = input("Enter customers Postal Code: ").upper()
        if FV.validate_postal_code(PostalCode):
            break
        else:
            print("Enter a valid postal code ex:\"A1B1B7\"")

    while True:            
        PhoneNumber = input("Enter customers Phone Number: ")
        if FV.validate_phone_number(PhoneNumber):
            break
        else:
            print("Enter a valid phone number ex:\"9999999999\"")

    while True:
        NumCars = input("Enter customer's number of cars: ")
        if FV.is_integer(NumCars):
            NumCars = int(NumCars)
            break
        else:
            print("Please enter a valid integer.")

    while True:
        ExtraLiability = input("Enter if customer wants extra liability coverage (Y/N): ").upper()
        if ExtraLiability in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    while True:
        GlassCoverage = input("Enter if customer wants Glass coverage (Y/N): ").upper()
        if GlassCoverage in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    while True:
        LoanerCar = input("Enter if customer wants Loaner car (Y/N): ").upper()
        if GlassCoverage in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


    #Set up displays if needed
    NumCarsDsp = str(NumCars)
    #Calculations
    Name = FirstName + " " + LastName    
    TotalCost = BASIC_PREMIUM + (NumCars - 1) * (BASIC_PREMIUM * DISCOUNT_ADDITIONAL_CARS)
    TotalExtraCost = 0
    if ExtraLiability == "Y":
        TotalCost += NumCars * COST_EXTRA_LIABILITY
        TotalExtraCost += NumCars * COST_EXTRA_LIABILITY
    if GlassCoverage == "Y":
        TotalCost += NumCars * COST_GLASS_COVERAGE
        TotalExtraCost += NumCars * COST_GLASS_COVERAGE
    if LoanerCar == "Y":
        TotalCost  += NumCars * COST_LOANER_CAR_COVERAGE
        TotalExtraCost  += NumCars * COST_LOANER_CAR_COVERAGE



    HST = TotalCost * HST_RATE
    TotalCost += HST
    PaymentOption = get_payment_option()
    while True:
        if PaymentOption == 'Down Pay':
            DownPayment = float(input("Enter customers down payment amount: "))
            if DownPayment > TotalCost:
                print("Down payment can't be higher than total cost.")
            else:
                break
        else:
            DownPayment = 0
            break  
    InsurancePremium = TotalCost - HST
    if PaymentOption == 'Full':
        PaymentAmount = TotalCost
        MonthlyPayment = 0.0
    else:
        PaymentAmount = TotalCost + PROCESSING_FEE_MONTHLY_PAYMENT
        MonthlyPayment = calculate_monthly_payment(TotalCost, DownPayment)
    
    CurrentDate = datetime.datetime.now()
    InvoiceDate = CurrentDate.strftime("%Y-%m-%d")
    NextMonth = (CurrentDate + datetime.timedelta(days=31)).strftime("%Y-%m-%d")
    Year = CurrentDate.year + (CurrentDate.month // 12)
    Month = 1 if CurrentDate.month == 12 else CurrentDate.month + 1
    NextMonth = datetime.datetime(Year, Month, 1).strftime("%Y-%m-%d")
    FirstPaymentDate = NextMonth 

    #Display results
    print("  --------------------------------------------------------------------")
    print(f"|                      The One Stop Insurance              *Receipt*|")
    print("|--------------------------------------------------------------------|")
    print(f"|                       Customer Information:                        |")
    print("|--------------------------------------------------------------------|")
    print(f"|  Name: {Name:<20s}                                      |")
    print(f"|  Street Address: {StAddress:<20s}                       |")
    print(f"|  City: {City:<20s}                                      |")
    print(f"|  Province: {Province:<2s}                                         |")
    print(f"|  Postal Code: {PostalCode:<6s}                                 |")
    print("|--------------------------------------------------------------------|")
    print("|                              Extras                                |")
    print("|--------------------------------------------------------------------|")
    print(f"|  Number of cars: {NumCarsDsp:<4s}                                  |")
    print(f"|  Extra Liability: {ExtraLiability:<3s}                           |")
    print(f"|  Glass Coverage: {GlassCoverage:<3s}                               |")
    print(f"|  Loaner Car: {LoanerCar:<3s}                                        |")
    print(f"|  Payment Option: {PaymentOption:<8s}                                  |")
    print("|--------------------------------------------------------------------|")
    print(f"| Down Payment Amount:{DownPayment}                                                   |")
    print(f"| Total Cost Breakdown:                                                  |")
    print(f"| Insurance Premium: {InsurancePremium}                                                  |")
    print(f"| Total Extra Cost: {TotalExtraCost}                                                  |")
    print(f"| HST: {HST}                                                   |")
    print(f"| Total Cost: {TotalCost}                                                    |")
    print(f"| Monthly Payment Information:                                                   |")
    print(f"| Monthly Payment Amount: {MonthlyPayment}                                                  |")
    print(f"| Payment Dates:                                                 |")
    print(f"| Invoice Date: {InvoiceDate}                                                   |")
    print(f"| First Payment Date:  {FirstPaymentDate}                                                  |")
    print(f"|                                                                  |")
    print("---------------------------------------------------------------------")


# HouseKeeping duties
    print()
    print("Policy data has been saved.")
    PolicyNumber += 1
    print()
    if input("Do you want to enter another customer? (Y/N): ").upper() != 'Y':
        break