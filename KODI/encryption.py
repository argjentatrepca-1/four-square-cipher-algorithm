from matrix import find_coords
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
