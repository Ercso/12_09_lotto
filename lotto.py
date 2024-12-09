import random

def lottó_játék():
    print("Üdvözöljük a lottó játékban!")
    print("Válasszon egy játékot:")
    print("1. 5/90 lottó")
    print("2. 6/49 lottó")
    
    választás = input("Kérem, válasszon (1 vagy 2): ")
    
    if választás == '1':
        számok = 5
        max_szám = 90
    elif választás == '2':
        számok = 6
        max_szám = 49
    else:
        print("Érvénytelen választás!")
        return

    tipp = int(input("Kérlek adj meg egy számot! "))
    print(f"Általad generált számok: {tipp}")
    
    nyerő_számok =
    print(f"A nyerő számok:)
    
    találatok = 
    print(f"Találatok száma: {len(találatok)}")
    if találatok:
        print(f"Az általad eltalált számok: {sorted(találatok)}")
    else:
        print("Sajnos nem talált el egy számot sem.")

if __name__ == "__main__":
    lottó_játék()