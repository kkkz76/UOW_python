""" Template for Assignment 3
    Use this template for submission.
    - This template includes an example function.
"""
# ========== Edit student info ===================#



name = 'Khant Ko Ko Zaw'  # (1) REPLACE THE STRING VARIABLE WITH YOUR NAME in string type
student_num = '8219035'  # (2) REPLACE THIS STRING VARIABLE WITH YOUR UOW ID in string type
subject_code = 'CSIT110'
# ========== End of student info =================#



def myClass_demo_unit_test(inputClass):
    """ This example takes in a class definition as input,
        then instantiates a class object and test its method
        in a try except system. 
    """
    try:
        obj = inputClass()
        obj.demo()
    except ValueError as e:
        print('A ValueError was raised because ' + str(e))


def example():
    # A class with one method
    class MyClass(): 
        def __init__(self):
            pass
        def demo(self):
            raise ValueError('Wrong input given!')
    # test the demo method
    myClass_demo_unit_test(MyClass)

class Price:
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f"${self.value:.2f}"

    def __repr__(self):
        return f"${self.value:.2f}"

# ========== Define function and class definitions here ====#

# ========== Question 1  =========#
def myClass_get_int_unit_test(inputClass):
    
    try:
        obj = inputClass()
        number =int(obj.get_integer()) 
        
    except AttributeError:
        return 'A'
    except ValueError:
        return 'V'
    except:
        return 'O'
    else:
        return number
    

def test1():
    class MyClass():
        def __init__(self):
            self.value = 10
        def get_integer(self):
            return self.value
    print(myClass_get_int_unit_test(MyClass))
    
    

# ========== Question 2  =========#

def compute_unit_prices(data, item_list):
    unit_prices = {}


    try:
        for item_name in item_list:
            try: 
                item_data = data[item_name]
                cost = item_data[0]
                quantity = item_data[1]
                unit_price = cost / quantity
                unit_prices[item_name] = unit_price

            except ZeroDivisionError:
                unit_prices[item_name] = -1
                
            except KeyError:
                unit_prices[item_name] = None
    except:
        return {}
    else:
        return unit_prices
    
    
def test2():
    data = {
    "vinegar": [120.0, 100],
    "ketchup": [950, 1000],
    "apples": [850, 1100],
    "oranges": [1050, 0]
    }

    item_list = ["ketchup", "oranges", "pear"]

    result = compute_unit_prices(data, item_list)
    print(result)
    
    
# ========== Question 3 (a) =========#

class OutOfStockError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return  f"The following item {self.message} is out of stock!"
    
    
def test3a():
    try:
        raise OutOfStockError("Eggs")
    except OutOfStockError as e:
        print(e)

# ========== Question 3 (b) (c) (d) =========#

class Inventory:
    hotline = "1800-1333-5432"
    items = {}
  
    
    @classmethod
    def set_items_from_list(cls,data):
        cls.items = {}
        for item in data:
            name = item[0]
            price = item[1]
            stock = item[2]
            cls.items[name] = {'price': Price(price), 'stock': stock}
            
    @classmethod
    def order(cls):
        Y = {}
       
        for item_name in cls.items.keys():
          
            user = int(input(f"How many {item_name} would you like to order? "))
            
            if user > cls.items.get(item_name)['stock']:
                
                raise OutOfStockError(item_name)

            elif user == 0:
                continue
            else:
                Y[item_name] = user
                
                
        return Y
                      

def test3b():
    print(Inventory.hotline)
    print(Inventory.items)
    
def test3c():
    print(Inventory.items)
    Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 3]])
    print(Inventory.items)
def test3d():
    Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 8],["Tea", 1.50, 6]])
    print(Inventory.order())
    Inventory.order()
    
# ========== Question 3 (e) =========#

def collate_orders(N):
    invalid_count = 0
    valid_count = 0
    oos_count = 0
    Z = {'invalid': None, 'valid_items': None, 'oos': None}
   
    
    for i in range(N):
      
        try:
            
            Order_list = Inventory.order()
        except OutOfStockError:
          
            oos_count+=1
          
        except Exception:
            invalid_count+=1
          
        else:
            
            for item_count in Order_list.values():
                valid_count+=item_count
            
       
   
      
            
    Z['invalid'] = invalid_count
    Z['valid_items'] = valid_count
    Z['oos'] = oos_count
    return Z


def test3e():
    Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 8],["Teas", 1.50, 6]])
    print(collate_orders(4))
    
    
# ========== Question 4 (a)=========#   

class InvalidDepthError(Exception):
    def __str__(self):
        return "Invalid Depth"      


# ========== Question 4 (b)=========# 

import random
class WaterBody:
    RHO = 997  
    G = 9.81   

    def __init__(self,volume:float):
        self.volume = volume
        
    @classmethod
    def get_hydrostatic_pressure(cls,depth:float):
        pressure = cls.RHO*cls.G*depth
        if pressure < 0:
            raise InvalidDepthError()
        else:
            return pressure
        
    def get_water_mass(self):
        return self.RHO * self.volume
    
    @staticmethod
    def is_small(volume:float):
        return volume < 50

    @staticmethod
    def is_medium(volume:float):
        return 50 <= volume <= 100

    @staticmethod
    def is_large(volume:float):
        return volume > 100
        
    @classmethod
    def spawn(cls):
        random_volume = random.uniform(1, 100)  
        return cls(volume=random_volume)
        
        
def test4():
    pool = WaterBody(10)
    print(pool.get_hydrostatic_pressure(1)) # prints 9780.57
    print(pool.get_water_mass()) # prints 9970
    try:
        pool.get_hydrostatic_pressure(-1)
    except Exception as e:
        print(e) # prints Invalid Dept



# ========== Question 5 =========# 
import re
class SingaporeNumbers:
    @staticmethod
    def car_plate_checksum(args:str):
        
        letter1= "0"
        letter2 = "0"
        
        try:
            pattern = re.compile(r'([A-Za-z]{1,3})(\d{1,4})')
            match = pattern.match(args)
            letter = match.group(1)
            number = match.group(2)
            letter_count = len(letter)
            number_count = len(number)
            number = int(number)
        
        except ValueError:
            print("Invalid Value")
        else:
            if letter_count == 1:
                letter2 = letter
            elif letter_count == 2:
                letter1 = letter[0]
                letter2 = letter[1]
            else:
                letter1 = letter[-2]
                letter2 = letter[-1]
                
            if(number_count < 4):
                number = f"{number :04d}"

            alphabet = list('0ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            num1 =alphabet.index(letter1) 
            num2 =alphabet.index(letter2) 
            converted = []
            converted.append(num1)
            converted.append(num2)
            
            for x in str(number):
                converted.append(int(x))
        
            fix_number = [9,4,5,4,3,2]
            sum= 0
            
            for i in range(len(converted)):
                sum+=converted[i]*fix_number[i]
                
            reminder = sum%19       
            reminder_alphabet = list('AZYXUTSRPMLKJHGEDCB')
            final_result = reminder_alphabet[reminder]
            return final_result
        
    
    @staticmethod
    def magic_num_checksum(number):
        number_list = []
        for x in str(number):
            number_list.append(int(x))
        fix_check_number = [2,7,6,5,4,3,2]
        data = 0
        for i in range(len(number_list)):
            data += (number_list[i]*fix_check_number[i])
            
        magic_result = data%11
        checkDigit = list('ABCDEFGHIZJ')
        magic_result_index = len(checkDigit) - (magic_result+1)
        final_check_result = checkDigit[magic_result_index]
        return final_check_result
     

# =========== End of function and class definitions ========#
def main():
    test1()
    test2()
    test3a()
    test3b()
    test3c()
    test3d()
    test3e()
    test4()
    print(SingaporeNumbers.car_plate_checksum("SBS3229"))
    print(SingaporeNumbers.magic_num_checksum(1234567))
    
 
""" an example function that creates a class and feeds into
            the class into the myClass_demo_unit_test for testing
            You are free to create your own test subjects that raise
            errors to test your code here.
"""
    # example()

    # call your functions or instantiate objects of the classes
    # you have defined in the main() definition. Make sure the 
    # code has at least one level of indentation.




if __name__ == '__main__':  ## DO NOT EDIT THESE TWO LINES.Y
    main()
    