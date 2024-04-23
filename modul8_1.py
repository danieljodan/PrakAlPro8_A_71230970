# Program Membandingkan Isi Dua File
def bandingkan_teks(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        handle1 = f1.readlines()
        handle2 = f2.readlines()
    ada_perbedaan = False
    i = 0
    for line1, line2 in zip(handle1, handle2):
        if line1 != line2:
            print(f"Perbedaan pada baris {i+1}:")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}")
            print()
            ada_perbedaan = True
        i += 1
    if ada_perbedaan == False:
        print("Tidak ada perbedaan")
    f1.close()
    f2.close()

file1 = "fileSatu.txt"
file2 = "fileDua.txt"
bandingkan_teks(file1, file2)

