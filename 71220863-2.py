def hitung_vote(vote):
    panjang = len(vote)
    for kandidat in vote:
        if vote.count(kandidat)>panjang/2:
            return kandidat
    return None

list_vote = []
panjang = int(input('Jumalh Vote : '))
for i in range(panjang):
    vt = input('Masukan Vote : ')
    list_vote.append(vt)

hasil = hitung_vote(list_vote)
print(hasil)