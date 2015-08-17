from time import *
start = time()

cardVals = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
numVals = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

def ocs(l, num):
    answer = 0
    for i in l:
        if i == num:
            answer += 1
    return answer

def bigger(player1, player2):
    if player1 > player2:
        return 1
    if player2 > player1:
        return 2
    else:
        return 0

def isConsecutive(l):
    a = min(l)
    b = [i for i in range(a, a+5)]
    for i in b:
        if i not in l:
            return False
    return True

def sameSuit(l):
    a = l[0]
    for i in l:
        if i != a:
            return False
    return True

class Card:
    def __init__(self, num, suit):
        if num == 'T':
            self.num = 10
        else:
            self.num = num
        self.suit = suit
        self.val = cardVals[self.num]

class Hand:
    def __init__(self, c1, c2, c3, c4, c5):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.nums = [self.c1.num, self.c2.num, self.c3.num, self.c4.num, self.c5.num]
        self.vals = [self.c1.val, self.c2.val, self.c3.val, self.c4.val, self.c5.val]
        self.suits = [self.c1.suit, self.c2.suit, self.c3.suit, self.c4.suit, self.c5.suit]
        self.highCard = max(self.vals)

    def onePair(self):
        self.occurences = []
        for val in self.vals:
            valOc = ocs(self.vals, val)
            self.occurences += [valOc]
        if ocs(self.occurences, 2) == 2 and ocs(self.occurences, 1) == 3:
            for val in self.vals:
                if ocs(self.vals, val) == 2:
                    self.onePairNum = val
                    break
            return True
        return False

    def twoPairs(self):
        self.occurences = []
        for val in self.vals:
            valOc = ocs(self.vals, val)
            self.occurences += [valOc]
        if ocs(self.occurences, 2) == 4 and ocs(self.occurences, 1) == 1:
            self.twoPairsNum = 0
            for val in self.vals:
                if ocs(self.vals, val) == 2 and val > self.twoPairsNum:
                    self.twoPairsNum = val
            return True
        return False

    def threeKind(self):
        self.occurences = []
        for val in self.vals:
            valOc = ocs(self.vals, val)
            self.occurences += [valOc]
        if ocs(self.occurences, 3) == 3 and ocs(self.occurences, 1) == 2:
            for val in self.vals:
                if ocs(self.vals, val) == 3:
                    self.threeKindNum = val
                    break
            return True
        return False

    def straight(self):
        if sameSuit(self.suits):
            return False
        if isConsecutive(self.vals):
            self.straightNum = self.highCard
            return True
        return False

    def flush(self):
        if isConsecutive(self.vals):
            return False
        if sameSuit(self.suits):
            self.flushNum = self.highCard
            return True
        return False
    
    def fullHouse(self):
        self.occurences = []
        for val in self.vals:
            valOc = ocs(self.vals, val)
            self.occurences += [valOc]
        if ocs(self.occurences, 3) == 3 and ocs(self.occurences, 2) == 2:
            for val in self.vals:
                if ocs(self.vals, val) == 3:
                    self.fullHouseNum = val
                    break
            return True
        return False

    def fourKind(self):
        self.occurences = []
        for val in self.vals:
            valOc = ocs(self.vals, val)
            self.occurences += [valOc]
        if ocs(self.occurences, 4) == 4 and ocs(self.occurences, 1) == 1:
            for val in self.vals:
                if ocs(self.vals, val) == 4:
                    self.fourKindNum = val
                    break
            return True
        return False

    def straightFlush(self):
        if isConsecutive(self.vals) and sameSuit(self.suits) and 14 not in self.vals:
            self.straightFlushNum = self.highCard
            return True
        return False

    def royalFlush(self):
        if isConsecutive(self.vals) and sameSuit(self.suits) and 14 in self.vals:
            return True
        return False

    def rankNum(self):
        if self.royalFlush():
            self.rank = 23
        elif self.straightFlush():
            self.rank = 22
        elif self.fourKind():
            self.rank = 21
        elif self.fullHouse():
            self.rank = 20
        elif self.flush():
            self.rank = 19
        elif self.straight():
            self.rank = 18
        elif self.threeKind():
            self.rank = 17
        elif self.twoPairs():
            self.rank = 16
        elif self.onePair():
            self.rank = 15
        else:
            self.rank = self.highCard
        return self.rank

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def tie(self):
        if self.player1.rank != self.player2.rank:
            return 0
        if self.player1.rank == 22:
            return bigger(self.player1.straightFlushNum, self.player2.straightFlushNum)
        elif self.player1.rank == 21:
            return bigger(self.player1.fourKindNum, self.player2.fourKindNum)
        elif self.player1.rank == 20:
            return bigger(self.player1.fullHouseNum, self.player2.fullHouseNum)
        elif self.player1.rank == 19:
            return bigger(self.player1.flushNum, self.player2.flushNum)
        elif self.player1.rank == 18:
            return bigger(self.player1.straightNum, self.player2.straightNum)
        elif self.player1.rank == 17:
            return bigger(self.player1.threeKindNum, self.player2.threeKindNum)
        elif self.player1.rank == 16:
            return bigger(self.player1.twoPairsNum, self.player2.twoPairsNum)
        elif self.player1.rank == 15:
            return bigger(self.player1.onePairNum, self.player2.onePairNum)
        else:
            return 0
        
            

    def winner(self):
        if self.player1.rankNum() > self.player2.rankNum():
            return 1
        elif self.player2.rankNum() > self.player1.rankNum():
            return 2
        else:
            return self.tie()

    

poker = open('poker.txt', 'r')
answer = 0

for line in poker:
    lineList = []
    currentChar = 0
    while currentChar <= 28:
        if line[currentChar] != ' ':
            if line[currentChar] in [str(i) for i in range(2, 15)]:
                lineList += [int(line[currentChar])]
            else:
                lineList += [str(line[currentChar])]
        currentChar += 1
    c1 = Card(lineList[0], lineList[1])
    c2 = Card(lineList[2], lineList[3])
    c3 = Card(lineList[4], lineList[5])
    c4 = Card(lineList[6], lineList[7])
    c5 = Card(lineList[8], lineList[9])
    c6 = Card(lineList[10], lineList[11])
    c7 = Card(lineList[12], lineList[13])
    c8 = Card(lineList[14], lineList[15])
    c9 = Card(lineList[16], lineList[17])
    c10 = Card(lineList[18], lineList[19])
    player1 = Hand(c1, c2, c3, c4, c5)
    player2 = Hand(c6, c7, c8, c9, c10)
    g = Game(player1, player2)
    if g.winner() == 1:
        answer += 1

print(answer, time()-start)
