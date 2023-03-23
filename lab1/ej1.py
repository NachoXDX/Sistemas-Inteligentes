from math import pi as pi #importo pi

def main():
    print(calcArea(getPositiveVal("Inserte el radio: ")))

def getPositiveVal(str="Inserte un valor numerico positivo: "):
    while True:
        try:
            r = float(input(str))  #verifico entrada
        except:
            print("No es un formato valido") #solicito otra
        else:
            if r >= 0:
                return r
            else:
                continue

def calcArea(rad):
    return pi*(rad**2) 

if __name__ == "__main__":
    main()