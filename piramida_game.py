from Piramida import *

while True:
    print("\n\t" + "__" * 12)
    print("\tDa zazenes igro vpisi S")
    print("\tZa izhod vpisi Q")

    action = input("\nKaj bi rad naredil? ").lower()

    if action == 's':
        # Ustvari instance Mapa s parametrom 'vhod'
        o_mapa = Mapa('vhod')
        # Ustvari instance Pogon() s parametrom objecta o_mapa
        o_igra = Pogon(o_mapa)
        # V objectu o_igra pozene method igraj()
        o_igra.igraj()

    if action == 'q':
        Mapa('vhod').izhod()
