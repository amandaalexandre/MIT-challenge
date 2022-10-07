from sympy import prime


def main():
    prime_numbers = [2]
    upper_limit = 10000

    #generating odd numbers that may be prime from 2 to 10000
    odd_numbers = []
  
    for number in range(2, upper_limit):
        if (number % 2 != 0):
            odd_numbers.append(number)
    #print(f'Odd numbers: {odd_numbers}')

    #case 3:
    prime_numbers.append(3)

    #checking if these numbers are divisible by the 1st 10 odd numbers
    for number in odd_numbers:
        #print(f'odd number: {number}')

        for i in range(odd_numbers.index(number)):
            if number % odd_numbers[i] == 0:
                #print(f'{number} divisible by {odd_numbers[i]}')
                break
            elif number not in prime_numbers:
                prime_numbers.append(number)
    
    print(f'prime number: {prime_numbers[1000]}')
    return prime_numbers[99]

if __name__ == '__main__':
    main()