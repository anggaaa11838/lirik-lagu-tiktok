import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("pe guwa mau ngomong", 0.1),
        ("guwa suka lu", 0.09),
        ("tapi boonk aowkwowk😹", 0.09),
        ("engga ege engga", 0.09),
        ("serius, aku suka kamu", 0.09),
        ("nahh", 0.09),
        ("hhhh", 0.09),
    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [0.3, 0.2, 0.3, 0.4, 0.6, 0.3, 0.3]
    # Ubah judul lagu
    print("\n== Separuh Aku - Noah ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    # Ganti nama pembuat
    print("// Code by Micola Arighi")


jalanin_lirik()
