# --- PERSON 4: INTEGRATION & TESTING ---
from matrix import generate_grid
from encryption import encrypt
from decryption import decrypt


def preprocess_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text))
    if len(text) % 2 != 0:
        text += "X"
    return text


# --- PERSON 2: ENCRYPTION PROCESS ---
def encrypt(plaintext, p_grid1, c_grid1, c_grid2, p_grid2):
    """Encodes the original message into ciphertext."""
    
    pass
def main():
    print("Four-Square Cipher - Integration & Testing\n")

    key1 = input("Enter key 1: ")
    key2 = input("Enter key 2: ")

    p_grid1 = generate_grid("")
    p_grid2 = generate_grid("")
    c_grid1 = generate_grid(key1)
    c_grid2 = generate_grid(key2)

    plaintext = input("Enter plaintext: ")
    processed = preprocess_text(plaintext)

    print("Processed Plaintext:", processed)

    encrypted = encrypt(processed, p_grid1, c_grid1, c_grid2, p_grid2)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, p_grid1, c_grid1, c_grid2, p_grid2)
    print("Decrypted:", decrypted)

    if processed == decrypted:
        print("\nTEST PASSED")
    else:
        print("\nTEST FAILED")


if __name__ == "__main__":
    main()