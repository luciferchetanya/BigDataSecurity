from phe import paillier  # Library for partially homomorphic encryption

def encrypt_salary_and_compute_tax():
    # Generate public and private keys
    public_key, private_key = paillier.generate_paillier_keypair()
    
    # Employee data
    employees = [
        {"name": "Alice", "salary": 50000},
        {"name": "Bob", "salary": 75000},
        {"name": "Charlie", "salary": 100000}
    ]
    
    # Encrypt salaries
    for emp in employees:
        emp["encrypted_salary"] = public_key.encrypt(emp["salary"])
    
    # Compute 10% tax on encrypted salaries
    tax_rate = 0.10
    for emp in employees:
        # Homomorphic operation: multiply encrypted value by plaintext tax rate
        emp["encrypted_tax"] = emp["encrypted_salary"] * tax_rate
    
    # Decrypt results
    for emp in employees:
        emp["tax"] = private_key.decrypt(emp["encrypted_tax"])
        emp["decrypted_salary"] = private_key.decrypt(emp["encrypted_salary"])
    
    # Display results
    print("{:<10} {:<10} {:<10} {:<15} {:<10}".format(
        "Name", "Salary", "Encrypted", "Encrypted Tax", "Tax"))
    print("-" * 60)
    for emp in employees:
        print("{:<10} {:<10} {:<10} {:<15} {:<10.2f}".format(
            emp["name"],
            emp["salary"],
            "Yes",
            "Yes",
            emp["tax"]))
    
    # Verify calculations
    print("\nVerification:")
    for emp in employees:
        expected_tax = emp["salary"] * tax_rate
        print(f"{emp['name']}: Expected tax {expected_tax:.2f}, Computed tax {emp['tax']:.2f}")

# Install required library first: pip install phe
# Then run:
encrypt_salary_and_compute_tax()
