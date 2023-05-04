def hapus_index_genap(inpu):
    while len(inpu)>1 :
        inpu = [inpu[i] for i in range(len(inpu))if i % 2 !=0]
    return inpu[0]

n = int(input("masukkan n: "))
if n <= 0:
    print("eror harus bilangan positif")
else:
    inpu=[]
    for i in range(n):
        angka = int(input("masukkan angka: "))
        inpu.append(int(angka))
    else:
        hasil_akhir = hapus_index_genap(inpu)
        print(hasil_akhir)
