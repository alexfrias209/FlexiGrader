print("Welcome to the Largest prime factor \nDeveloped by Marlene Perez \n Compute the prime factor of given number <100")
import csv

def prime_factors(n):
    """Find prime factors of a number."""
    factors = []
    current_number = 2
    
    while n != 1:
        while n % current_number == 0:
            factors.append(current_number)
            n = n // current_number

        current_number = current_number + 1 # Move to the next number
    return factors

def adding(num, biggest):
    with open('62467_6419704_9050445.csv', mode = 'a') as file:
       spam = csv.writer(file)
    #    prime.csv = [num, biggest]
    #    writer_object = csv.writer(num, biggest)
       spam.writerow([num,biggest])
       return
    
def prime():
    num = int(input("Enter a number: "))
    if num <= 0:
      print("Please enter a positive integer.")
    with open('62467_6419704_9050445.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            if int(lines[0]) == num:
                print("Found saved. The biggest prime factor is:",lines[1])
                print("Found saved")
                return
    
    factors =  prime_factors(num)
    factors.sort(reverse=True)
    adding(num,factors[0])
    print("Biggest factor is", factors[0])
    if len(factors) == 0:
        print(f"{num} is a prime number.")
    else:
         print(f"{factors} are the prime factorization of {num}")
        
prime()