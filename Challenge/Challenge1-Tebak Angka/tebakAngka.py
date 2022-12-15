import random

while True:
    print("="*50)
    print("PERMAINAN TEBAK ANGKA")
    print("="*50)
    
    print("\n")
    
    print("PERATURAN")
    print("Komputer akan memilih angka secara acak antara 0 sd 9 secara rahasia. Lalu anda akan menebak angka tersebut dengan 3 kali percobaan. Apabila anda menebak angka tersebut secara benar maka anda akan menang dan apabila anda menebak salah lebih dari 3 kali percobaan maka anda akan kalah.")
    
    print("\n")
    
    secNumb = random.randint(0, 9)
    
    print("Komputer telah menentukan sebuah angka, silahkan tebak!")
    
    trialLimit = 3
    
    for trial in range(trialLimit):
        try:
            ans = int(input(f"\n[Percobaan {trial+1}] Masukan angka: "))

            if 0<=ans<=9:
                if ans == secNumb:
                    print("Selamat, tebakanmu benar!")
                    print(f"Percobaan anda sebanyak {trial}x")
                    break
                else:
                    print(
                        "Angka tebakanmu terlalu", 'kecil' if ans < secNumb else 'besar'
                    )
            else:
                print("Angka yang kamu masukan bukan 0 sd 9")
        except Exception as e:
            print("Masukan hanya angka!")
    else:
        print(f'\nSayang sekali, kamu sudah salah menebak sebanyak {trialLimit}x!')
    
    
    if input('Apakah anda ingin mencobanya lagi? (y/n) ') != 'y':
        break