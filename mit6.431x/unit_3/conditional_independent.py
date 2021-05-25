import sys

def fact(n):
  if n > 0:
    return n*fact(n-1)
  else:
    return 1

def binom(n, k):
    if k == 0:
        return 1
    return fact(n) // (fact(k) * fact(n - k))

if __name__ == '__main__':

    n = int(sys.argv[1])
    k = int(sys.argv[2])


    cur = binom(n, k)
    print(cur)
    print()