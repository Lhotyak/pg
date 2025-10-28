def je_tah_mozny(figura: str, start: tuple[int, int], cil: tuple[int, int], obsazena: set[tuple[int, int]]) -> bool:
    """
    figura: 'pesec' | 'jezdec' | 'vez' | 'strelec' | 'dama' | 'kral'
    start: (radek, sloupec) 1..8
    cil:   (radek, sloupec) 1..8
    obsazena: množina obsazených polí (řádek, sloupec). Barvy neřešíme, cílové pole musí být volné.

    Pozn.: Pěšec jde směrem k vyšším řádkům; dvojkrok pouze z řádku 2 a jen když jsou obě pole volná.
    """

    def na_sachovnici(p):
        r, c = p
        return 1 <= r <= 8 and 1 <= c <= 8

    def sign(x):
        return (x > 0) - (x < 0)

    def cesta_volna(a, b):
        """Zkontroluje, zda je volná cesta z a do b (mimo cílového pole; to se kontroluje zvlášť). 
        Používá se pro věž/střelce/dámu a také pro pěšcův dvojkrok (1 mezikrok)."""
        ra, ca = a
        rb, cb = b
        dr, dc = rb - ra, cb - ca
        stepr, stepc = sign(dr), sign(dc)

        if stepr == 0 and stepc == 0:
            return True
        r, c = ra + stepr, ca + stepc
        while (r, c) != b:
            if (r, c) in obsazena:
                return False
            r += stepr
            c += stepc
        return True

    if not na_sachovnici(start) or not na_sachovnici(cil):
        return False

    if cil in obsazena:
        return False
    
    if start == cil:
        return False

    sr, sc = start
    tr, tc = cil
    dr, dc = tr - sr, tc - sc
    adr, adc = abs(dr), abs(dc)

    f = figura.strip().lower()

    if f == 'jezdec':
        return (adr, adc) in {(1, 2), (2, 1)}

    if f == 'kral':
        return max(adr, adc) == 1

    if f == 'vez':
        if sr == tr or sc == tc:
            return cesta_volna(start, cil)
        return False

    if f == 'strelec':
        if adr == adc:
            return cesta_volna(start, cil)
        return False

    if f == 'dama':
        if sr == tr or sc == tc or adr == adc:
            return cesta_volna(start, cil)
        return False

    if f == 'pesec':
        
        if dc != 0:
            return False
        
        if dr == 1:
            
            return True
        
        if sr == 2 and dr == 2:
            mezikrok = (sr + 1, sc)
            if mezikrok in obsazena:
                return False
            
            return cesta_volna(start, cil)
        return False

    return False
