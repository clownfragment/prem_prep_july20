
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))

# print(binomial_pmf(8, 4, p=0.25))


def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0

    for k in range(k_high+1):
        cumulative += binomial_pmf(n, k, p)
    
    return cumulative

# print(binomial_cdf(n=8, k=4, p=0.25))

def binomial_dict(n, k_low, k_high, p=0.5):
    d = dict()

    for k in range(k_low, k_high+1):
        d[k] = binomial_pmf(n, k, p=p) 

    return d

# for k, v in binomial_dict(8, 0,  8, 0.25).items():
#     print(f'{k}: {v}')


'''There are 8 components in parallel and at least 3 of those components need to be operational for a circuit to function. The probability of any given component being operational is 0.7. What is the probability that 3 components are operational?'''


# print(binomial_pmf(8, 3, p=0.7))

'''What is the probability that at least 3 components are operational?'''
