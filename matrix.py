def generate_grid(key=""):
    #Alfabeti pa J(duhet me qene 25 shkronja sepse matrica eshte 5x5)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    #Pergatitja e keywordit,( zevendesojme J me I )
    key = (key or "").upper().replace("J", "I")

    used = []

    # 1-Shto keyword (pa perseritje)
    for char in key:
        if char in alphabet and char not in used:
            used.append(char)

   
    # 2-Shtojme pjesen tjeter te alfabetit
    for char in alphabet:
        if char not in used:
            used.append(char)

    # 3- E ndajme ne  matrice 5x5
    grid = []
    for i in range(0, 25, 5):
        grid.append(used[i:i+5])

    return grid