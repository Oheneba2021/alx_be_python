FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9/5

def convert_to_celcius(fahrenheit):
    '''Convert Fahrenheit to Celsius'''
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    '''Convert Celsius to Fahrenheit'''
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    '''Main function to run the temperature conversion tool'''
    print("Temperature Conversion Tool:")
    user_temp = float(input("Enter the temperature to convert: "))

    # check if user entered correct unit
    if user_temp is None:
        print("Invalid temperature. Please enter a numeric value.")
        return
    else:
        temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if temp_unit == "C":
        converted_temp = convert_to_fahrenheit(user_temp)
        print(f"{user_temp}°C is {converted_temp:.2f}°F")
    elif temp_unit == "F":
        converted_temp = convert_to_celcius(user_temp)
        print(f"{user_temp}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid temperature unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
if __name__ == "__main__":
    main()