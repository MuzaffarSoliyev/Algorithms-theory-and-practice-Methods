import sys

class Heap:
    def __init__(self):
        self.elems = []

    def get_left(self, i):
        return 2 * i + 1

    def get_right(self, i):
        return 2 * i + 2

    def get_parent(self, i):
        return (i - 1) // 2

    def heap_up(self, i):
        while i > 0:
            if self.elems[i] > self.elems[self.get_parent(i)]:
                self.elems[i], self.elems[self.get_parent(i)] = self.elems[self.get_parent(i)], self.elems[i]
            i = self.get_parent(i)

    def heap_down(self, i):
        size = len(self.elems)
        while self.get_left(i) < size:
            cur = self.elems[i]
            left = self.elems[self.get_left(i)]
            right = -1
            if self.get_right(i) < size:
                right = self.elems[self.get_right(i)]

            if left > right and left > cur:
                self.elems[i], self.elems[self.get_left(i)] = self.elems[self.get_left(i)], self.elems[i]
                i = self.get_left(i)
            elif right > left and right > cur:
                self.elems[i], self.elems[self.get_right(i)] = self.elems[self.get_right(i)], self.elems[i]
                i = self.get_right(i)
            elif left == right and left > cur:
                self.elems[i], self.elems[self.get_left(i)] = self.elems[self.get_left(i)], self.elems[i]
                i = self.get_left(i)
            else:
                break

    def insert(self, v):
        self.elems.append(v)
        index = len(self.elems) - 1
        self.heap_up(index)

    def extract_max(self):
        max_elem = 0
        last = len(self.elems) - 1
        if last == -1:
            return max_elem
        else:
            self.elems[0], self.elems[last] = self.elems[last], self.elems[0]
            max_elem = self.elems[last]
            self.elems.pop()
            self.heap_down(0)
            return max_elem


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    h = Heap()
    for i in range(n):
        command = sys.stdin.readline().strip().split()
        if len(command) > 1:
            h.insert(int(command[1]))
        else:
            print(h.extract_max())
