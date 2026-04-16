import re

# --- PERSON 1: GRID GENERATION & COORDINATES ---
def generate_grid(key=""):
    """Builds a 5x5 matrix using a keyword, combining I/J."""
    # Person 1: Insert logic to create the 5x5 grid here
    pass

def find_coords(char, grid):
    """Returns the (row, col) of a character in a specific grid."""
    # Person 1: Insert coordinate lookup logic here
    pass


# --- PERSON 2: ENCRYPTION PROCESS ---
def encrypt(plaintext, p_grid1, c_grid1, c_grid2, p_grid2):
    """Encodes the original message into ciphertext."""
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = "".join(filter(str.isalpha, plaintext))
    
    
    if len(plaintext) % 2 != 0:
        plaintext += "X"
        
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        
        # placeholder name i funksionit
        loc1 = find_coords(char1, p_grid1) 
        loc2 = find_coords(char2, p_grid2)
        
        if loc1 is not None and loc2 is not None:
            r1, c1 = loc1[0], loc1[1] 
            r2, c2 = loc2[0], loc2[1]
            
            
            ciphertext += c_grid1[r1][c2]
            ciphertext += c_grid2[r2][c1]
            
    return ciphertext
    
    pass


# --- PERSON 3: DECRYPTION PROCESS ---
def decrypt(ciphertext, p_grid1, c_grid1, c_grid2, p_grid2):
    """Converts ciphertext back into a readable message."""
    # Person 3: Insert decryption logic here
    pass


# --- PERSON 4: INTEGRATION & TESTING ---
if __name__ == "__main__":
    # This section ties everything together.
    # Person 4: Call the functions above to verify the project works.
    print("Four-Square Cipher System is ready for testing...")
    pass
