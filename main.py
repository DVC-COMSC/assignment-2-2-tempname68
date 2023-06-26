def main():
    """
    ##################################################
    # Complete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    celcius = float(input("Enter temperature in celsius"))
    fahrenheit = (9/5)*celcius+32
    print(f'Fahrenheit: \t{fahrenheit:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
