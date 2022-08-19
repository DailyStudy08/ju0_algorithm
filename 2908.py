A, B = input().split()
A, B = int(A[::-1]), int(B[::-1])
print(A if A > B else B)

# print(max(input()[::-1].split()))