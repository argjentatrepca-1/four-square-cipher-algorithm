from matrix import find_coords

def decrypt (ciphertext, p_grid1, c_grid1, c_grid2, p_grid2):
    """Ciphertexti kthehet ne plaintext"""

    ciphertext= ciphertext.upper() .replace("J", "I")
    ciphertext = "" .join (filter(str.isalpha, ciphertext))

    plaintext = ""

    for i in range (0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]

        loc1 = find_coords(char1, c_grid1)
        loc2 = find_coords(char2, c_grid2)

        if loc1 is not None and loc2 is not None:
            r1, c1 = loc1[0], loc1[1]
            r2, c2 = loc2[0], loc2[1]

            plaintext += p_grid1[r1][c2]
            plaintext += p_grid2[r2][c1]

            return plaintext
