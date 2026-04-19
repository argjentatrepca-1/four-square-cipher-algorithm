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

    # 2 pjesa tjeter e alfabetit
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


