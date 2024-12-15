def hitung_parkir_terminal(durasi):
    # Biaya awal untuk parkir
    biaya_awal = 3000
    
    # Jika durasi parkir kurang dari atau sama dengan 2 jam, kembalikan biaya awal
    if durasi <= 2:
        return biaya_awal
    
    # Menghitung jam tambahan setelah 2 jam
    tambahan_jam = durasi - 2
    # Menghitung biaya tambahan berdasarkan jam tambahan
    tambahan_biaya = tambahan_jam * 1500
    
    # Menghitung total biaya parkir
    total_biaya = biaya_awal + tambahan_biaya
    
    # Jika durasi parkir lebih dari 24 jam, tambahkan biaya tambahan
    if durasi > 24:
        total_biaya += 10000
    
    # Mengembalikan total biaya yang harus dibayar
    return total_biaya

try:
    # Meminta input durasi parkir dari pengguna
    durasi = float(input("Masukkan durasi parkir (jam): "))
    
    # Memeriksa apakah durasi yang dimasukkan valid (tidak negatif)
    if durasi < 0:
        print("Durasi tidak valid")
    else:
        # Menghitung biaya parkir menggunakan fungsi yang telah didefinisikan
        biaya = hitung_parkir_terminal(durasi)
        # Menampilkan total biaya yang harus dibayar 
        print(f"Biaya yang harus dibayar adalah Rp {biaya:,.0f}.")
except ValueError:
    # Menangani kesalahan jika input bukan angka yang valid
    print("Error, masukkan angka yang valid untuk durasi!")