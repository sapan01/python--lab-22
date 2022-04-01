N = int(input())
A = list(map(int, input().split()))[:N]
even_count = 0
odd_count = 0
for i in A:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
if even_count > odd_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
