import sys
def probKHeads(n,k,p):
  return fact(n)/(fact(k)*fact(n-k)) * p**k * (1-p)**(n-k)

def fact(n):
  if n > 0:
    return n*fact(n-1)
  else:
    return 1


# print(getFact(6,5,1/2))


if __name__ == '__main__':
    num_flips = sys.argv[0]

    total = 0
    for x in [0,1,2,3,4,5,6]:
    # print(getFact(6,x,1/2))
        total = total + probKHeads(6,x,1/2)

    print(total)

