# Meminta input jenis kendaraan dari pemilik kendaraan
jenis_kendaraan = input("Masukkan jenis kendaraan (Motor/Mobil): ").strip().lower()

# Input durasi parkir dalam jam dari pemilik kendaraan
durasi_parkir = int(input("Masukkan durasi parkir (jam): "))

#biaya awal parkir
biaya = 3000

# Mengecek apakah durasi parkir lebih dari 2 jam
if durasi_parkir > 2:
    # Mengecek apakah durasi parkir kurang dari atau sama dengan 24 jam
    if durasi_parkir <= 24:
        # Jika jenis kendaraan adalah Motor
        if jenis_kendaraan == "motor":
            # Tambahkan biaya untuk setiap jam setelah 2 jam
            biaya += (durasi_parkir - 2) * 1000
        # Jika jenis kendaraan adalah Mobil
        elif jenis_kendaraan == "mobil":
            # Tambahkan biaya untuk setiap jam setelah 2 jam
            biaya += (durasi_parkir - 2) * 1500
        else:
            print("Jenis kendaraan tidak valid. Harap masukkan 'Motor' atau 'Mobil'.")
            biaya = 0  # Set biaya menjadi 0 jika jenis kendaraan tidak valid
    else:
        # Jika durasi parkir lebih dari 24 jam
        if jenis_kendaraan == "motor":
            # Tambahkan biaya untuk setiap jam setelah 2 jam dan biaya tambahan
            biaya += (durasi_parkir - 2) * 1000 + 10000
        elif jenis_kendaraan == "mobil":
            # Tambahkan biaya untuk setiap jam setelah 2 jam dan biaya tambahan
            biaya += (durasi_parkir - 2) * 1500 + 10000
        else:
            print("Jenis kendaraan tidak valid. Harap masukkan 'Motor' atau 'Mobil'.")
            biaya = 0  # Set biaya menjadi 0 jika jenis kendaraan tidak valid

# Menampilkan total biaya parkir kepada pengguna jika biaya tidak 0
if biaya > 0:
    print("Total biaya parkir:", biaya)