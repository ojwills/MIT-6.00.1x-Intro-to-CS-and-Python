#Exercise: genPrimes
#5.0/5.0 points (graded)
#ESTIMATED TIME TO COMPLETE: 10 minutes
#
#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():

    primes = []
    n = 1
    
    while True:
        n+=1
        for p in primes:
            if n % p == 0:
                break
            
        else:
            primes.append(n)
            yield n
 
#Complete