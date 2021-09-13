#  find out all the primes less than give no 
# in below function we are just finding minimum prime factor for a given no
def seive_algo(num):
    mx, p = num, 2
    prime = [-1] * (mx + 1) #Stores the smallest prime factor of integers 1 mx
    while p * p <= mx:
        if prime[p] == -1:
            prime[p] = p
            for i in range(p * p, mx + 1, p):
                if prime[i] == -1:
                    prime[i] = p
        p += 1
    return prime