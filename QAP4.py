# Description: The One  Stop  Insurance  Companyneeds  a  program  to  enter  and  calculate  new  insurance  policy information for its customers. Allow the program to repeat to allow the user to enter as many customers as  they  want.    Add  at  least  3  functions  to  the  program.    I  will  accept  the  FormatValues.pylibrary  as  a function option –but  you need to add a new  function to the  library–make  it relevant.Bonus point–actually just my admiration-if you can create a function that returns multiple values.
# Author: Kyle Hollett
# Date(s): 2024-03-16



# Define Libraries
import datetime
import FormatValues as FV
import re
import time
import sys
# Define Constants
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
DISCOUNT_ADDITIONAL_CARS = 0.25
COST_EXTRA_LIABILITY = 130.00
COST_GLASS_COVERAGE = 86.00
COST_LOANER_CAR_COVERAGE = 58.00
HST_RATE = 0.15
PROCESSING_FEE_MONTHLY_PAYMENT = 39.99
PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
PAYMENT_OPTIONS = ['Full', 'Monthly', 'Down Pay']




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
def calculate_monthly_payment(TotalCost, DownPayment):
    if DownPayment > 0:
        TotalCost -= DownPayment
    MonthlyPayment = (TotalCost + PROCESSING_FEE_MONTHLY_PAYMENT) / 8
    return MonthlyPayment

def validate_down_payment(DownPayment):
    if not DownPayment.strip():  # Checks if input is empty or contains blankspace
        return False, "Input cannot be empty."
    
    if not DownPayment.replace('.', '', 2).isdigit():  # Check if the input is a number (allowing for two decimal point)
        return False, "Invalid input. Please enter a valid number for the down payment."
    
    DownPayment = float(DownPayment)
    if DownPayment >= 0:
        return True, DownPayment
    else:
        return False, "Down payment must be a positive number."

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
Claims = []

def get_claims(Claims):
    print()
    print("Enter previous claim data. Type '000' in the claim number input to end.")
    print()
    while True:
        ClaimNumber = input("Enter claim number: ")
        if ClaimNumber == "000":
            break
        elif not ClaimNumber.isdigit():
            print("Please enter a valid claim number.")
            continue

        while True:
            ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
            if ClaimDate == "000":
                break
            try:
                datetime.datetime.strptime(ClaimDate, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please enter the date in (YYYY-MM-DD) format.")
                continue
            else:
                break

        if ClaimDate == "000":
            break
        
        while True:
            try:
                ClaimAmount = float(input("Enter claim amount: "))
                ClaimAmount = FV.FDollar2(ClaimAmount)
                break
            except ValueError:
                print("Please enter a valid number for claim amount.")
                continue

        # Check for duplicate claim number
        for claim in Claims:
            if claim['Claim Number'] == ClaimNumber:
                print("Duplicate claim number. Please enter a different claim number.")
                break
        else:
            Claims.append({'Claim Number': ClaimNumber, 'Claim Date': ClaimDate, 'Claim Amount': ClaimAmount})
            print("Claim added successfully.")

    return Claims




# Main Program 


    #Inputs
     
while True: #Below needs valdations - fixed
    print()
    print("Enter customer information below:")
    print()

    while True:
        FirstName = input("Enter customer's first name: ").title()
        if FV.validate_name(FirstName):
            break
        else:
            print("Invalid input. Please enter a valid first name. Cannot contain special characters, digits or spaces. ")
    while True:
        LastName = input("Enter customer's last name: ").title()
        if FV.validate_name(LastName):
            break
        else:
            print("Invalid input. Please enter a valid last name. Cannot contain special characters, digits or spaces. ")
    while True:
        StAddress = input("Enter customers street address: ").title() #Maybe validate - validated
        if FV.validate_street_address(StAddress):
            break
        else:
            print("Invalid street address. Input valid street address Example '123 Freshwater Road/rd")
    
    while True:
        City = input("Enter customers City: ").title() #Maybe validate - validated
        if FV.validate_city(City):
            break
        else: 
            print("Invalid input. Please enter a valid city name. You're bein bad, you cannot include numbers or special characters.")


    Province = get_valid_province() 

    while True:
        PostalCode = input("Enter customers Postal Code: (X#X#X#) ").upper()
        if FV.validate_postal_code(PostalCode):
            break
        else:
            print("Enter a valid postal code ex:\"A1B1B7\"")

    while True:            
        PhoneNumber = input("Enter customers Phone Number: ")
        if FV.validate_phone_number(PhoneNumber):
            PhoneNumber = str(PhoneNumber)
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

     #Calculations
    Name = FirstName + " " + LastName    
    TotalCost = BASIC_PREMIUM + (int(NumCars) - 1) * (BASIC_PREMIUM * DISCOUNT_ADDITIONAL_CARS)
    TotalExtraCost = 0
    if ExtraLiability == "Y":
        TotalCost += int(NumCars) * COST_EXTRA_LIABILITY
        TotalExtraCost += int(NumCars) * COST_EXTRA_LIABILITY
    if GlassCoverage == "Y":
        TotalCost += int(NumCars) * COST_GLASS_COVERAGE
        TotalExtraCost += int(NumCars) * COST_GLASS_COVERAGE
    if LoanerCar == "Y":
        TotalCost  += int(NumCars) * COST_LOANER_CAR_COVERAGE
        TotalExtraCost  += int(NumCars) * COST_LOANER_CAR_COVERAGE

    HST = TotalCost * HST_RATE
    TotalCost += HST
    PaymentOption = get_payment_option()
    while True:
        if PaymentOption == 'Down Pay':
            while True:
                try:
                    DownPayment = input("Enter customer's down payment amount: ")
                    ValidatedDownPayment = validate_down_payment(DownPayment)
                    if ValidatedDownPayment:
                        DownPayment = float(DownPayment)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the down payment.")
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


    get_claims(Claims)
        
    
        #Set up displays if needed
    NumCarsDsp = str(NumCars)
    if ExtraLiability == "Y":
        ExtraLiabilityDSP = "Yes"
    else: 
        ExtraLiabilityDSP = "No"
    if GlassCoverage == "Y":
        GlassCoverageDSP = "Yes"
    else: 
        GlassCoverageDSP = "No"
    if LoanerCar == "Y":
        LoanerCarDSP = "Yes"
    else: 
        LoanerCarDSP = "No"
    if PaymentOption == 'Down Pay':
        PaymentOptionDsp = "Down Payment"
    elif PaymentOption == "Full":
        PaymentOptionDsp = "Full Payment"
    else:
        PaymentOptionDsp = "Monthly Payment"
     

    #Display results
    print()
    print(" ---------------------------------------------------------------------")
    print(f"|                       The One Stop Insurance         *Receipt{POLICY_NUMBER:<5} |")
    print("|--------------------------------------------------------------------|")
    print(f"|                        Customer Information:                       |")
    print("|--------------------------------------------------------------------|")
    print(f"|                                                                    |")
    print(f"|                    Name                  : {Name:<20s}    |")
    print(f"|                    Street Address        : {StAddress:<20s}    |")
    print(f"|                    City                  : {City:<20s}    |")
    print(f"|                    Province              : {Province:<2s}                      |")
    print(f"|                    Postal Code           : {PostalCode:<6s}                  |")
    print(f"|                    Phone Number          : {PhoneNumber:<10s}              |")
    print(f"|                                                                    |")
    print("|--------------------------------------------------------------------|")
    print("|                              Extras:                               |")
    print("|--------------------------------------------------------------------|")
    print(f"|                                                                    |")
    print(f"|                    Number of cars        : {NumCarsDsp:<4s}                    |")
    print(f"|                    Extra Liability       : {ExtraLiabilityDSP:<3s}                     |")
    print(f"|                    Glass Coverage        : {GlassCoverageDSP:<3s}                     |")
    print(f"|                    Loaner Car            : {LoanerCarDSP:<3s}                     |")
    print(f"|                    Payment Option        : {PaymentOptionDsp:<15s}         |")
    print(f"|                                                                    |")
    print("|--------------------------------------------------------------------|")
    print("|                        Payment Information:                        |")
    print("|--------------------------------------------------------------------|")
    print(f"|                                                                    |")
    print(f"|                    Down Payment Amount   : {FV.FDollar2(DownPayment):<10s}              |")
    print(f"|                    Monthly Payment Amount: {FV.FDollar2(MonthlyPayment):<10s}              |")
    print(f"|                                                                    |")
    print(f"|                    Total Extra Cost      : {FV.FDollar2(TotalExtraCost):<10s}              |")
    print(f"|                                                                    |")
    print(f"|                    Insurance Premium     : {FV.FDollar2(InsurancePremium):<10s}              |")
    print(f"|                    HST                   : {FV.FDollar2(HST):<10s}              |")
    print(f"|                    Total Cost            : {FV.FDollar2(TotalCost):<10s}              |")   
    print(f"|                                                                    |")
    print("|--------------------------------------------------------------------|")
    print(f"|                           Payment Dates:                           |")
    print("|--------------------------------------------------------------------|")
    print(f"|                                                                    |")
    print(f"| Invoice Date: {InvoiceDate:<10s}            First Payment Date: {FirstPaymentDate:<10s} |")
    print(f"|                                                                    |")
    print("|--------------------------------------------------------------------|")
    print(f"|                           Previous Claims                          |")
    print("|--------------------------------------------------------------------|")
    print(f"|        Claim Number:        Claim Date:          Amount:           |")
    print("|--------------------------------------------------------------------|")
    for claim in Claims:
        print(f"|           {claim['Claim Number']:>5}              {claim['Claim Date']:<10}          {claim['Claim Amount']:<10}        |")
    print(" --------------------------------------------------------------------") 
    print()

    for _ in range(4):  # Change to control no. of 'blinks'
        print('Saving claim data ...', end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)
    print()
    print("Claim data successfully saved ...", end='\r')
    print()
    time.sleep(1.5)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    POLICY_NUMBER += 1
    print()
    if input("Do you want to enter another customer? Enter y if you want to continue, or anything else if you want to stop.: ").upper() != 'Y':
        break

# HouseKeeping duties
