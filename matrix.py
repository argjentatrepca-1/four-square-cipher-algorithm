def generate_grid(key=""):
    # Alfabeti pa J (25 shkronja per me bo matricen 5x5)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Pergatitja e keyword-it (J e zevendesojme me  I)
    key = (key or "").upper().replace("J", "I")

    used = []

    # 1 Shtojme keyword-et(pa perseritje)
    for char in key:
        if char in alphabet and char not in used:
            used.append(char)

    # 2 pjesa tjetar e alfabetit
    for char in alphabet:
        if char not in used:
            used.append(char)

    # 3 Ndarja e matrices  5x5
    grid = []
    for i in range(0, 25, 5):
        grid.append(used[i:i + 5])

    return grid


def find_coords(char, grid):
    char = char.upper().replace("J", "I")

    for r, row in enumerate(grid):
        if char in row:
            return r, row.index(char)

    return None


# ================= TESTIM =================
if __name__ == "__main__":
    key = "KEYWORD"

    grid = generate_grid(key)

    print("Matrica 5x5:\n")
    for row in grid:
        print(" ".join(row))

    print("\nKoordinatat e shkronjave:")
    print("A ->", find_coords("A", grid))
    print("K ->", find_coords("K", grid))
    print("Z ->", find_coords("Z", grid))
    