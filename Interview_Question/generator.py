
  #  Create a generator to produce first n prime numbers 


def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# print(list(filter(lambda num : isprime(num),[12,10,2,3,5,9,77,72,71,23,31,83,53])))

def prime_generator(n):
    num = 2
    while n:
        if isprime(num):
            yield num
            n-=1
        num +=1

print(prime_generator(12))