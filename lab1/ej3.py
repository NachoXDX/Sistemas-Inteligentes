def main():
    print(getSeason())


def getSeason():
    verano = ["diciembre","enero","febrero"]
    otono = ["marzo","abril","mayo"]
    invierno = ["junio","julio","agosto"]
    primavera = ["septiembre","octubre","noviembre"]
    while True:
        m = input("Escriba el mes: ").lower().strip()
        if m in verano:
            return "Verano"
        elif m in otono:
            return "Otono"
        elif m in invierno:
            return "Invierno"
        elif m in primavera:
            return "Primavera"
        else:
            continue

if __name__ == "__main__":
    main()