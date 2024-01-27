import re


class Kharchang:

    def __init__(self, stri):
        self.stri = stri+stri[:10]

    def tt(self):
        self.stri = re.sub('tt', 'o', self.stri)
        return self.stri


class Spongbob(Kharchang):

    def __init__(self, stri):
        super().__init__(stri)

    def merge(self, left, right):
        sorted = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if int(left[i]) < int(right[j]):
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1

        sorted += right[j:]
        sorted += left[i:]
        return sorted

    # Decomposition
    def sort(self, arr):
        # print(arr)
        if len(arr) > 1:
            middle = len(arr) // 2
            left = self.sort(arr[:middle])
            right = self.sort(arr[middle:])
            arr = self.merge(left, right)
            arr = ''.join(arr)
        return arr


class Oktapus:

    def __init__(self, stri):
        self.stri = stri

    def xindex(self):
        for s in range(len(self.stri)):
            if self.stri[s]=='x':
                self.stri = self.stri + str(s)
                break

    def eliminate(self):
        self.stri = re.sub(r'(.)\1\1', '(0_0)', self.stri)
        return self.stri


inp = input()
def process(inp):
    global a
    a = 0
    if inp[0:2] == 'sb':
        sb = Spongbob(inp)
        e = sb.sort(str(len(inp)))
        r = str(int(e[0])+1) + e[1:]
        print(r)
    elif inp[0] == 's' and inp[1] != 'b':
        ok = Oktapus(inp)
        ok.xindex()
        print(ok.eliminate())
    elif inp[0] == 'm':
        kh = Kharchang(inp)
        print(kh.tt())
    else:
        a = 1

process(inp)
if a==1:
    process(inp[::-1])
    if a ==1:
        print('invalid input')
