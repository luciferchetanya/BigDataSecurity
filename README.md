# Cryptographic Operations Implementation

A Python implementation of various cryptographic concepts including Euler's Totient Function, RSA encryption, dataset access logging, and homomorphic encryption for secure tax calculations.

## Features

1. **Euler's Totient Function** - Computes φ(n) from scratch without library functions
2. **RSA Cryptosystem** - Full implementation including:
   - Large prime generation
   - Key pair generation
   - Message encryption/decryption
3. **Dataset Access Logger** - Simulates and logs user access to sensitive data
4. **Homomorphic Encryption** - Computes taxes on encrypted salaries without decryption

## Installation

1. Clone this repository:
   ```bash
   pip install phe  # For homomorphic encryption example
   .
├── euler_totient.py       # Totient function implementation
├── rsa.py                 # RSA cryptosystem
├── access_logger.py       # Dataset access logging
├── homomorphic_tax.py     # Encrypted tax calculation
├── sample_data.csv        # Example dataset
├── requirements.txt       # Dependencies
└── README.md              # This file

