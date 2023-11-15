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
name = 'Khant Ko Ko Zaw' 
student_num = '8219035'  
subject_code = 'CSIT110'
# ========== End of student info =================#
# ========== Define function definitions here ====#

#Question 1
def compute_tax(first_number , second_number = 0.18):
    return float(first_number * second_number)
  
#Question 2
def get_class(value):
    return type(value)

#Question 3
def formulate_equation():
    user_input1 = float(input("Enter first number: "))
    user_input2 = float(input("Enter second number: "))
    sum_result = user_input1 + user_input2
    formula = f"{user_input1} + {user_input2}"
    return (sum_result , formula )

#Question 4
def filter_by(fcn , N):
    fcn_value = fcn()
    if fcn_value > N:
        return True
    else:
        return False

#Question 5
def format_price(price):
    result = f"${price:0,.2f}"
    print(result)
    return result


# ========== End of function definition===========#

def main():  # DO NOT EDIT THIS LINE.
    print("Assignment2")  # DO NOT EDIT THIS LINE.
    # ========== Call your functions here ========#
    
    #Question 1
    Q1_a = compute_tax(2)
    print(Q1_a)
    Q1_b = compute_tax(2,1.1)
    print(Q1_b)
    
    #Question 2
    test_string = "Hello"
    resultA = get_class(test_string)
    resultB = get_class(123)
    print(resultA)
    print(resultB)
    
    #Question 3
    sum_result, formula = formulate_equation()
    print(sum_result)
    print(formula)
    
    #Question 4
    def test_fcn1():
        return 3*3
    Q_4a = filter_by(test_fcn1,16)
    Q_4b = filter_by(test_fcn1,4)
    print(Q_4a)
    print(Q_4b)
    
    #Question 5
    final_result = format_price(2.2)
    print(final_result)

    # ========== End of function calls ===========#

if __name__ == '__main__':  # DO NOT EDIT THIS LINE.
    main()  # DO NOT EDIT THIS LINE.
