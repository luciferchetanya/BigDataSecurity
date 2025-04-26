def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(n):
    """Calculate Euler's Totient function φ(n)"""
    if n <= 0:
        return 0
    count = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            count += 1
    return count

# Example usage:
n = 10
print(f"φ({n}) = {euler_totient(n)}")