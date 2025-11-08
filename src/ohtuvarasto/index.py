from .varasto import Varasto


def print_mehuvarasto(mehua):
    print(f"Mehuvarasto: {mehua}")
    print(f"saldo = {mehua.saldo}")
    print(f"tilavuus = {mehua.tilavuus}")
    print(f"paljonko_mahtuu = {mehua.paljonko_mahtuu()}")


def print_olutvarasto(olutta):
    print(f"Olutvarasto: {olutta}")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def test_mehu_lisays(mehua):
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print_mehuvarasto(mehua)


def test_mehu_otto(mehua):
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print_mehuvarasto(mehua)


def test_virhetilanteet():
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def test_olut_lisays_otot(olutta, mehua):
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print_olutvarasto(olutta)

    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print_mehuvarasto(mehua)

    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print_olutvarasto(olutta)


# --- Main function ---

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print_mehuvarasto(mehua)
    print_olutvarasto(olutta)

    # Run tests
    test_mehu_lisays(mehua)
    test_mehu_otto(mehua)
    test_virhetilanteet()
    test_olut_lisays_otot(olutta, mehua)

    print("mehua.ota_varastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print_mehuvarasto(mehua)


if __name__ == "__main__":
    main()
