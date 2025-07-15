def is_prime(n):
    if n < 1:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def longest_prime_sum(n):
    primes = [i for i in range(1, n) if is_prime(i)]
    result = []
    current_sum = 0
    for prime in reversed(primes):
        if current_sum + prime <= n:
            current_sum += prime
            result.append(prime)
    return result

while True:
    txtfile = open("projectntoepad.txt", 'a', encoding='utf-8')
    n = int(input('Please enter a positive prime integer: '))

    da_sum = longest_prime_sum(n)
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        print("Sorry, " + str(n) + " isn't a prime number")
    else:
        print(da_sum)


    with txtfile as f:
        if n%2 == 0 or n%3 == 0 or n%5 == 0:
            f.write("Sorry, " + str(n) + " isn't a prime number")
        else:
            f.write(str(n) + " is made up of the following prime numbers: ")
            for a in da_sum:
                f.write(str(a))
                f.write(' ')
        f.write("\n")
    user_input = input("Do you with to continue?: (yes/no) ")

    if user_input.lower() == "no":
        txtfile.close()
        break