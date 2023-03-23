from ej1 import getPositiveVal as getVal

def porToLet():
    while True:
        v = getVal()
        if 0 <= v <= 100:
            break
        else:
            continue

    l = "A" if (v >= 90 and v<= 100) else ""
    l = "B" if (v >= 80 and v <= 89) else l
    l = "C" if (v >= 70 and v <= 79) else l
    l = "D" if (v >= 60 and v <= 69) else l
    l = "F" if (v >=  0 and v <= 59) else l

    print(l) 
            
