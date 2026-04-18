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

   