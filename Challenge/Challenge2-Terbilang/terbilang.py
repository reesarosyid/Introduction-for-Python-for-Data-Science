
from asyncio.windows_events import NULL


def terbilang(angka):
    huruf = ['Nol', 'Satu', 'Dua', 'Tiga', 'Empat', 'Lima', 'Enam',
             'Tujuh', 'Delapan', 'Sembilan', 'Sepuluh', 'Sebelas']
    if angka < 12:
        temp = ' '+huruf[angka]
    elif angka < 20:
        temp = str(terbilang(angka-10))+' Belas'
    elif angka <100:
        temp = str(terbilang(angka//10))+' Puluh'+str(terbilang(angka%10))
    else:
        temp = "Angka hanya 0-99!"
    return temp


def main():
    angka = 1
    while angka != (0):
       angka = int(input("Masukan angka 0-99(0 Untuk keluar) :"))
       print(terbilang(angka))
       continue

if __name__ == "__main__":
    main()

