import matplotlib.pyplot as plt

length = 20

class DFSignal():
    def __init__(self, left, strtype, valueList=[], root=0, Fs=8000):
        self.valueList = valueList
        self.left = left
        self.root = root
        self.strtype = strtype
        self.Fs = Fs

    def printf(self):
        strpre = "{"
        for i in range(len(self.valueList)):
            if i + self.left == self.root:
                strpre += '\\vec{' + str(self.valueList[i]) + '}' + ';'
            else:
                strpre += str(self.valueList[i]) + ";"
        strpre = strpre[:-1]
        print(strpre + "}")

    def plot(self):
        listplot = []
        for i in range(len(self.valueList)):
            listplot.append(self.left + i)
        plt.stem(listplot, self.valueList)
        plt.show()

class unitJump(DFSignal):
    def __init__(self, left, strtype='unitJumpSequence', valueList=[], root=0, Fs=8000):
        super().__init__(left, strtype, valueList, root, Fs)
        self.values()

    def values(self):
        self.valueList = []
        for i in range(length):
            if i + self.left >= self.root:
                self.valueList.append(1)
            else:
                self.valueList.append(0)

class unitPulse(DFSignal):
    def __init__(self, left, strtype='unitPulseSeries', valueList=[], root=0, Fs=8000):
        super().__init__(left, strtype, valueList, root, Fs)
        self.values()

    def values(self):
        self.valueList = []
        for i in range(length):
            if i + self.left == self.root:
                self.valueList.append(1)
            else:
                self.valueList.append(0)

class rect(DFSignal):
    def __init__(self, left, N, strtype='rectangularWindows', valueList=[], root=0, Fs=8000):
        super().__init__(left, strtype, valueList, root, Fs)
        self.N = N
        self.values()

    def values(self):
        self.valueList = []
        for i in range(length):
            if (i + self.left >= self.root) and (i + self.left <= self.N-1):
                self.valueList.append(1)
            else:
                self.valueList.append(0)

un = unitJump(-2)
un.printf()
un.plot()
