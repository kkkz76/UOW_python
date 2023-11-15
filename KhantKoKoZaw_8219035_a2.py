"""
Instructions:
(A) Edit student info
   - Replace value of the string variable 'name' with your name in string type.
     Do not change the variable name
   - Replace value of the string variable 'student_num' wotj your uow id in string type

(B) Your solution
   - Your solution should contain 5 function definitions. 

(C) How you can test your solution
   - You can test your solution by calling the functions you have
     defined in the 'main' function defintion below.
   - You can choose to use any values of the specified data type to test your solution.
   - The marking script will not be based on your function calls,
     it will call the functions separately.
"""


# ========== Edit student info ===================#
name = 'Khant Ko Ko Zaw'  # (1) REPLACE THE STRING VARIABLE WITH YOUR NAME in string type
student_num = '8219035'  # (2) REPLACE THIS STRING VARIABLE WITH YOUR UOW ID in string type
subject_code = 'CSIT110'
# ========== End of student info =================#
# ========== Define function definitions here ====#

#Question1
def nosiy_traffic(N):
    
    numList = []
    for num in range(1,N+1):
       
        
        if num % 5 == 0 and num % 7 == 0:
            num = "VroomHonk"
        elif num % 5 == 0:
            num = "Vroom"
        elif num % 7 == 0:
            num = "Honk"
        else:
            num = str(num)
            
        numList.append(num)
        
    text = ",".join(numList) + "."
    return text



#Question2
def get_cpf_interest_rates():
    
    ordinary_acc_max = 20000.00
    total_max = 60000.00
    firstBase = 30000.00
    secondBase = 30000.00
    retire_acc = 0.00
    base_OA_rate = 0.025
    base_SA_rate = 0.04
    base_MA_rate = 0.04
    base_RA_rate = 0.04 
    extra_interest_below55 = 0.01
    extra_interest_firstBase = 0.02
    extra_interest_secondBase = 0.01
   
    age = float(input("Enter current age: "))
    ordinary_acc = float(input ("Enter current amount in OA: "))
    special_acc = float(input ("Enter current amount in SA: "))
    medisave_acc = float(input("Enter current amount in MA: "))
    
    if age >= 55:
        retire_acc = float(input("Enter current amount in RA: "))

    interest_OA = ordinary_acc * base_OA_rate
    interest_SA = special_acc * base_SA_rate
    interest_MA = medisave_acc * base_MA_rate
    interest_RA = retire_acc * base_RA_rate
    
    if ordinary_acc > 20000.00:
        total = ordinary_acc_max + special_acc + medisave_acc + retire_acc
    else:
        total = ordinary_acc + special_acc + medisave_acc + retire_acc
    
    
    if age < 55:
        if total > 60000.00:
            extra = total_max * extra_interest_below55
        else:
            extra = total * extra_interest_below55
            
    else:
        if total >= 60000.00:
            extra = (firstBase * extra_interest_firstBase) + (secondBase * extra_interest_secondBase)
        elif total >= 30000.00:
            extra = (firstBase * extra_interest_firstBase) + ((total - firstBase) * extra_interest_secondBase)
        else:
            extra = total * extra_interest_firstBase
            
    final  =  interest_OA + interest_SA + interest_MA + interest_RA + extra
    print (f"Your interest rate this year will be ${final:0,.2f}")


#Question3
def get_car_rental_booking():
    
    Economy = {}
    Standard = {}
    Premium = {}
    Suv = {}
    Sub_total = {}
    
    economy_rate = 40
    standard_rate = 70
    premium_rate = 100
    suv_rate = 130
    tax_rate = 0.18
    
    economy_count = int(input("Number of Economy cars: "))
    standard_count = int(input("Number of Standard cars: "))
    premium_count = int(input("Number of Premium cars: "))
    suv_count = int(input("Number of SUVs: "))
    duration = int(input("Rental duration (number of days): "))
    
    economy_charges = (duration * economy_rate) * economy_count
    standard_charges = (duration * standard_rate) * standard_count
    premium_charges = (duration * premium_rate) * premium_count
    suv_charges = (duration * suv_rate) * suv_count
    
    total_car_count = economy_count + standard_count + premium_count + suv_count
    sub_total = economy_charges + standard_charges + premium_charges + suv_charges
    tax_charges = sub_total * tax_rate
    total = sub_total + tax_charges
    
    Economy["count"] = economy_count
    Economy["charges"] = economy_charges
    
    Standard["count"] = standard_count
    Standard["charges"] = standard_charges
    
    Premium["count"] = premium_count
    Premium["charges"] = premium_charges
    
    Suv["count"] = suv_count
    Suv["charges"] = suv_charges
    
    Sub_total["count"] = total_car_count
    Sub_total["charges"] = sub_total
    
    customer_data = {
        "Economy": Economy,
        "Standard": Standard,
        "Premium": Premium,
        "SUV": Suv,
        "Subtotal": Sub_total,
        "Total (18% tax)": total
    }
    print(f"\nSummary of your car rental for {duration} day(s)")
    
    for x,y in customer_data.items():
        if x == "Total (18% tax)":
            y = f"${y:0,.2f}"
            print(f"{x:<16}{y:>10}")
        else:
            count = y["count"]
            charges = y["charges"]
            charges = f"${charges:0,.2f}" 
            print(f"{x:<13}{count:^3}{charges:>10}")
            

#Question4
def sanitize_vehicle_filenames():
    
    filenames = []
    
    while True:
        filename = input("Filename?")
        if not filename:
            break
        
        bracket_check = []
        cleaned_filename = ""
        loop_check = 0

        for char in filename:
            if char == "<":
                bracket_check.append(char)
            elif char == ">" and bracket_check:
                bracket_check.pop()
            else:
                if not bracket_check:
                    cleaned_filename += char

                loop_check += 1
                if loop_check > len(filename) * 2:
                    return None

        filenames.append(cleaned_filename)

    return ",".join(filenames)


# ========== End of function definition===========#

def main():  # DO NOT EDIT THIS LINE.
    print("Assignment2")  # DO NOT EDIT THIS LINE.
    # ========== Call your functions here ========#
    result = nosiy_traffic(48)
    print(result)
    print()
    get_cpf_interest_rates()
    print()  
    get_car_rental_booking()
    print()
    output = sanitize_vehicle_filenames()
    print(output)
    # ========== End of function calls ===========#

if __name__ == '__main__':  # DO NOT EDIT THIS LINE.
    main()  # DO NOT EDIT THIS LINE.