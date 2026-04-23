# APLIKASI KALCULATOR SEDERHANA
print("=== SELAMAT DATANG DI KALCULATOR SEDERHANA ===")
print("Pilih operasi yang diinginkan:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")
print("5. Keluar")

while True:
    # Input pilihan user
    pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")
    
    # Jika user pilih keluar
    if pilihan == '5':
        print("Terima kasih! Sampai jumpa lagi! 👋")
        break
    
    # Cek pilihan valid
    if pilihan in ['1', '2', '3', '4']:  # Semua string!
        try:
            # Input dua angka
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            # Hitung berdasarkan pilihan
            if pilihan == '1':
                hasil = angka1 + angka2
                print(f"Hasil {angka1} + {angka2} = {hasil}")
            
            elif pilihan == '2':
                hasil = angka1 - angka2
                print(f"Hasil {angka1} - {angka2} = {hasil}")
            
            elif pilihan == '3':
                hasil = angka1 * angka2
                print(f"Hasil {angka1} * {angka2} = {hasil}")
            
            elif pilihan == '4':
                if angka2 != 0:
                    hasil = angka1 / angka2
                    print(f"Hasil {angka1} / {angka2} = {hasil}")
                else:
                    print("❌ Tidak bisa membagi dengan nol!")
            
            # Tanya lanjut atau tidak
            lanjut = input("Hitung lagi? (y/n): ")
            if lanjut.lower() != 'y':
                print("Terima kasih! 👋")
                break
                
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    
    else:
        print("❌ Pilihan tidak valid! Pilih 1-5")