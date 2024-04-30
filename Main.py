from functools import lru_cache

@lru_cache
def fiboo(n):
    if n == 2 or n == 1:
        return 1
    return fiboo(n-1) + fiboo(n-2)
    

n = int(input("\nEnter The Number : \n"))
print("\n")
for i in range(n, 0, -1):
    print(i,":",fiboo(i))