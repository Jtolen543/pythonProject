def fibonacci(n): # defines the function with the parameter being an input of x
    n1 = 0
    n2 = 1
    if n <= 0: # prints this out when given number is not in fibonacci
        return "Number should be higher"
    elif n == 1: # prints 0 for the 1st number in fibonacci
        return 0
    elif n == 2: # prints 1 for the 2nd number in fibonacci
        return 1
    else:
        for i in range(2,n): # brings out the nth number in the fibonacci
            sum = n1 + n2
            n1 = n2
            n2 = sum
        return sum

def is_prime(n):
    if n < 2: # returns prime for all negative numbers and numbers less than 2
        return False
    if n == 2: # had to hard code because None would be printed due to the range excluding 2 if n was 2
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
        if i+1 != n:
            continue
        if i+1 == n:
            return True

def print_prime_factors(n): # calculate the prime factors of n
    n1 = n
    prime = []
    while n % 2 == 0: # divides all non-prime numbers by 2 until it cannot anymore
        n = n // 2
        prime.append(2) # adds 2 to the list
    is_prime(n) # determines if prime to see if there's further factors
    while True: # trouble getting none, made this boolean to state how it will append numbers to the list only if prime
        for i in range(3,n+1,2):
            while n % i == 0: # made this into while instead if to cover cases of squared numbers
                n = n // i
                prime.append(i)
        prime = str(prime) # turned the list into a string
        prime = prime.replace("[","") # learned this to help format the problem better by
        prime = prime.replace("]","") # removing the brackets, commas, etc.
        prime = prime.replace(","," *") # astrick to represent multiplication
        break
    print(f"{n1} = {prime}")