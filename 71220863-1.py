def tribobonacci(a,b,c,n):
    total= [a,b,c]
    mulai = 2
    panjang= n-3
    for i in range (panjang):
        next = total[mulai-2]+ total[mulai-1]+total[mulai]
        total.append(next)
        mulai += 1
    return total

a =int(input("a: "))
b =int(input("b: "))
c =int(input("c: "))
n =int(input("n: "))

total = tribobonacci(a,b,c,n)
print(total)