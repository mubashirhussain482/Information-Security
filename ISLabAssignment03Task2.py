# Import required libraries (no external crypto libraries used)
# ECC math is implemented manually for learning purpose
# Elliptic Curve parameters
a = 2                 # Curve parameter a
b = 3                 # Curve parameter b
p = 97                # Prime modulus
# ----------------------------------------
# Modular inverse function
# ----------------------------------------
def mod_inverse(k, p):
    # Returns modular inverse of k modulo p
    return pow(k, -1, p)
# ----------------------------------------
# Point addition on elliptic curve
# ----------------------------------------
def point_add(P, Q):
    # If P is point at infinity, return Q
    if P == "O":
        return Q
    # If Q is point at infinity, return P
    if Q == "O":
        return P
    # Extract x and y coordinates of points
    x1, y1 = P
    x2, y2 = Q
    # If x coordinates same but y different, result is infinity
    if x1 == x2 and y1 != y2:
        return "O"
    # If points are equal, perform point doubling
    if P == Q:
        return point_double(P)
    # Calculate slope for point addition
    m = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p
    # Calculate x coordinate of result
    x3 = (m*m - x1 - x2) % p
    # Calculate y coordinate of result
    y3 = (m*(x1 - x3) - y1) % p
    # Return resulting point
    return (x3, y3)
# ----------------------------------------
# Point doubling
# ----------------------------------------
def point_double(P):
    # If P is infinity, return infinity
    if P == "O":
        return "O"
    # Extract x and y coordinates
    x, y = P
    # Calculate slope for point doubling
    m = ((3*x*x + a) * mod_inverse(2*y, p)) % p
    # Calculate new x coordinate
    x3 = (m*m - 2*x) % p
    # Calculate new y coordinate
    y3 = (m*(x - x3) - y) % p
    # Return doubled point
    return (x3, y3)
# ----------------------------------------
# Scalar multiplication
# ----------------------------------------
def scalar_multiply(k, P):
    # Initialize result as point at infinity
    result = "O"
    # Repeatedly add point P, k times
    for _ in range(k):
        result = point_add(result, P)
    # Return final multiplied point
    return result
# ----------------------------------------
# Generator point
# ----------------------------------------
G = (3, 6)             # Base point on the curve
# ----------------------------------------
# Key generation
# ----------------------------------------
private_key = 5       # Manually chosen private key
public_key = scalar_multiply(private_key, G)  # Public key
# Display keys
print("Private Key:", private_key)
print("Public Key:", public_key)
# ----------------------------------------
# Message
# ----------------------------------------
message = 7           # Small numeric message
print("\nOriginal Message:", message)
def get_x(point):
    if point == "O":
        raise ValueError("Shared secret is point at infinity. Choose different k or keys.")
    return point[0]
# Encryption
k = 3
C1 = scalar_multiply(k, G)
shared_secret = scalar_multiply(k, public_key)
C2 = message + get_x(shared_secret)
print("\nEncrypted Message:")
print("C1:", C1)
print("C2:", C2)
# Decryption
shared_secret_dec = scalar_multiply(private_key, C1)
decrypted_message = C2 - get_x(shared_secret_dec)
print("\nDecrypted Message:", decrypted_message)         # Recover message
# Display decrypted message
print("\nDecrypted Message:", decrypted_message)