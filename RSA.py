import random
import math
from math import gcd

def is_prime(n, k=5):
    """Miller-Rabin primality test"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    
    # Write n as d*2^s + 1
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bit_length=1024):
    """Generate a large prime number"""
    while True:
        p = random.getrandbits(bit_length)
        # Ensure it's odd and has the right bit length
        p |= (1 << bit_length - 1) | 1
        if is_prime(p):
            return p

def extended_gcd(a, b):
    """Extended Euclidean algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    """Modular inverse using extended Euclidean algorithm"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def rsa_key_generation(bit_length=1024):
    """Generate RSA public and private keys"""
    p = generate_large_prime(bit_length//2)
    q = generate_large_prime(bit_length//2)
    while p == q:
        q = generate_large_prime(bit_length//2)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 65537  # Common choice
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = modinv(e, phi)
    
    return (e, n), (d, n)

def rsa_encrypt(message, public_key):
    """Encrypt message using RSA public key"""
    e, n = public_key
    # Convert message to integer if it's not already
    if isinstance(message, str):
        message = int.from_bytes(message.encode('utf-8'), 'big')
    elif isinstance(message, bytes):
        message = int.from_bytes(message, 'big')
    if message >= n:
        raise ValueError("Message too large for key size")
    return pow(message, e, n)

def rsa_decrypt(ciphertext, private_key):
    """Decrypt ciphertext using RSA private key"""
    d, n = private_key
    message = pow(ciphertext, d, n)
    # Convert back to bytes
    byte_length = (message.bit_length() + 7) // 8
    return message.to_bytes(byte_length, 'big').decode('utf-8')

# Example usage:
public_key, private_key = rsa_key_generation(bit_length=1024)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

message = "Hello, RSA!"
print("\nOriginal message:", message)

ciphertext = rsa_encrypt(message, public_key)
print("Encrypted message:", ciphertext)

decrypted_message = rsa_decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
