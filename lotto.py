import random

def lottó_játék():
    print("Üdvözöljük a lottó játékban!")
    print("Válasszon egy játékot:")
    print("1. 5/90 lottó")
    print("2. 6/45 lottó")
    
    választás = input("Válassz a 2 közül (1 vagy 2): ")
    
    if választás == '1':
        számok = 5
        max_szám = 90
    elif választás == '2':
        számok = 6
        max_szám = 45
    else:
        print("Érvénytelen!")
        return

    tippelt_számok = set()
    while len(tippelt_számok) < számok:
        try:
            tipp = int(input(f"Adj meg egy számot (1-{max_szám}): "))
            if 1 <= tipp <= max_szám:
                tippelt_számok.add(tipp)
            else:
                print(f"A számnak 1 és {max_szám} között kell lennie.")
        except ValueError:
            print("Érvényes számot adj meg.")


    nyerő_számok = set(random.sample(range(1, max_szám + 1), számok))
    
    print(f"A tippelt számok: {sorted(tippelt_számok)}")
    print(f"A nyerő számok: {sorted(nyerő_számok)}")
    
    találatok = tippelt_számok.intersection(nyerő_számok)
    print(f"Találatok száma: {len(találatok)}")
    if találatok:
        print(f"A találatok: {sorted(találatok)}")
    else:
        print("Sajnos nem volt találatod.")
lottó_játék()