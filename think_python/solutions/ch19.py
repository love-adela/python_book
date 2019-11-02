def binomial_coeff(n, k):
    if k==0:
        return 1
    if n==0:
        return 0
            
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res
	
	
def b(n,k):
    memo = {}
    if (n,k) in memo:
        return memo[(n,k)]
    if k==0:
        return 1
    if n==0:
        return 0
    
    r = b(n-1, k) + b(n-1, k-1)
    memo[(n,k)] = r	
    return r

a = binomial_coeff(3,4)
print(a) # 0
print(b(3,4)) # 0
c = binomial_coeff(10,4)
print(c) # 210
print(b(10,4)) # 210
