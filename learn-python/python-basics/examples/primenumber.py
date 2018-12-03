"""Write a program to find if a number is prime or not"""

def check_prime_num(input_num):
    found = 0
    if input_num >= 2:
        for x in range(2, input_num):
            if (input_num % x) == 0:
                found = 1
                print(input_num, 'is not a prime number')
                break
        if found == 0:
            print(input_num, ' is a prime number')


if __name__ == "__main__":
    INPUT_NUM = int(input('Please enter a number greater than 1: '))
    check_prime_num(INPUT_NUM)
