from time import *
start = time()

cipher1F = open('cipher1.txt', 'r')

cipher1S = ''

for char in cipher1F:
        cipher1S += str(char)

cipher1F.close()

cipher1S = cipher1S.strip()
cipher1 = [int(i) for i in cipher1S.split(',')]

possible = [i for i in range(97, 123)] + [i for i in range(65, 91)] + [32, 44, 46, 58, 59]

currentXOR = 0

def convert(l):
        s = ''
        for i in l:
                s += chr(i)
        return s

def decrypt(l, k):
        current = 0
        ans = []
        for i in l:
                ans += [k[current]^i]
                if current in [0, 1]:
                        current += 1
                else:
                        current = 0
        return ans

common = ['the', 'and', 'Gospel']


for k1 in range(97, 123):
        for k2 in range(97, 123):
                for k3 in range(97, 123):
                        currentDecrypt = decrypt(cipher1, [k1, k2, k3])
                        currentDecryptString = ''
                        for i in currentDecrypt:
                                currentDecryptString += chr(i)
                        if common[0] in currentDecryptString and common[2] in currentDecryptString:
                                key = [k1, k2, k3]
                                

print(sum(decrypt(cipher1, key)), time()-start)


