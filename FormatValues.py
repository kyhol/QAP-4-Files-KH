import re

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr

def is_integer(value): #Validation to check if value is an int
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def validate_name(name):
    if not name.strip(): #strip leading and trailing spaces and then check if the resulting string is empty
        return False  
    if not all(char.isalpha() for char in name): # checks to see if its all characters
        return False 
    return True

def validate_postal_code(PostalCode):   #Could change it so it could accept examples a1b-1b3 or a1b 1b3 instead of just a1b1b3
    Pattern = r'^[A-Za-z]\d[A-Za-z]\d[A-Za-z]\d$' #'^' signifies the start of the line then input has to follow pattern [A-Za-z] accepted letters | \d digits then repeat
    if re.match(Pattern, PostalCode): #Have to import re to use this function
        return True
    else:
        return False
    
def validate_phone_number(PhoneNumber): #Could change to include -'s or something like this example (709) 782-7208
    Pattern = r"^\d{10}$" #Pattern of digits 10 numbers long ^ is the line start $ is the line end

    if re.match(Pattern, PhoneNumber):
        return True
    else:
        return False