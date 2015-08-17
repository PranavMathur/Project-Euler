def isPalindrome(num):
        numstr = str(num)
        a = []
        q = []
        for character in numstr:
                a += [character]
        for character in numstr:
                q += [character]
        a.reverse()
        if a == q:
                return True
        return False

def reverse(num):
        numstr = str(num)
        numlist = []
        for character in numstr:
                numlist += [character]
        numlist.reverse()
        newstr = ''
        for char in numlist:
                newstr += str(char)
        return int(newstr)

def funcGen(num):
        a = 0
        while a <= 50:
                numRev = reverse(num)
                numSum = num + numRev
                yield numSum
                num = numSum
                a += 1

def isLychrel(num):
        for i in funcGen(num):
                if isPalindrome(i):
                        return False
        return True

a = 0

for i in range(1, 10001):
        if isLychrel(i):
                a += 1

print(a)

        
                
        
	
            
