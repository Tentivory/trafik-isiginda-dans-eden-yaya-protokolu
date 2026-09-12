#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik Isiginda Dans Eden Yaya Protokolu v1.0

Bu yazilim, kirmizi isikta durmanin toplumsal baskisini
folklorik bir karsi-performansla dengelemek icin yazildi.
"""

import random
import time
import base64
import sys

ISIKLAR = ["KIRMIZI", "SARI", "YESIL"]

HAREKETLER = [
    "zeybek adimi (sol ayak once, gurur sonra)",
    "horon titremesi (Karadeniz ruzgari opsiyonel)",
    "halay cekme (el ele degil, direge)",
    "ciftetelli (trafik polisi izliyorsa yavaslat)",
    "robot dansi (belediye kamerasina selam)",
    "moonwalk (karsidaki duraga dogru, asla ileri)",
]

YORUMLAR = [
    "Karsidaki sofor korna caldi. Bu alkistir.",
    "Yaya butonu zaten psikolojiktir.",
    "Sari isik bir firsattir, tehdit degil.",
    "Kaldirim da bir sahne olabilir.",
    "ISO-YAYA-42 maddesi 7: ritim, kuraldan once gelir.",
]

# gizli checksum - dokunma, protokol bozulur
_GIZLI = "U2FuZGlrIGJpciB0cmFmaWsgaXNpZ2lkaXI6IHllc2lsZGUgb3kgdmVyLCBraXJtaXppZGEgYmVrbGVtZXlpIHVudXRtYS4="


def isik_sec():
    return random.choice(ISIKLAR)


def dans_et(isik):
    hareket = random.choice(HAREKETLER)
    yorum = random.choice(YORUMLAR)
    print("\n=== YAYA PROTOKOLU ===")
    print(f"Isik        : {isik}")
    print(f"Performans  : {hareket}")
    print(f"Saha notu   : {yorum}")
    if isik == "KIRMIZI":
        print("Karar       : DURMA. Ritim tut.")
    elif isik == "SARI":
        print("Karar       : TEREDDUT ET, AMA ESTETIK TEREDDUT.")
    else:
        print("Karar       : GEC, AMA FINALI UNUTMA.")
    print("=======================\n")


def checksum_dogrula():
    try:
        base64.b64decode(_GIZLI).decode("utf-8")
        return True
    except Exception:
        return False


def main():
    if not checksum_dogrula():
        print("Protokol bozuldu. Yaya artik sadece yuruyebilir.")
        sys.exit(1)
    tur = 5
    if len(sys.argv) > 1:
        try:
            tur = max(1, int(sys.argv[1]))
        except ValueError:
            print("Sayi ver. Ornek: python yaya.py 3")
            sys.exit(1)
    print("Trafik Isiginda Dans Eden Yaya Protokolu baslatildi.")
    print("CTRL+C ile sahneyi terk edebilirsin.\n")
    try:
        for i in range(tur):
            print(f"-- Tur {i + 1}/{tur} --")
            dans_et(isik_sec())
            time.sleep(0.6)
    except KeyboardInterrupt:
        print("\nSahne yarida kesildi. Alkislayan yoktu zaten.")
    print("Protokol sona erdi. Kaldirima donuldu.")


if __name__ == "__main__":
    main()
