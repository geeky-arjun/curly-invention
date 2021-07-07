#  if we have given two no a and b and 
# those are very large no 
# then we can get (a/b)%m let's say m is 1000000007 which a prime no.
# b^-1 % m can only be calculated if b and m are co-prime

def modDivide(a,b):
    m = 1000000007
    a = a % m
    inv = pow(b, m - 2, m)
    return (inv*a) % m

print(modDivide(134567475, 7853))