class PriorityQueue:

    def __init__(self, string_dict):
        self.queue = []
        for key, val in string_dict.items():
            self.queue.append((key, val))
        self.queue.sort(key=lambda x: x[1])

    def insert(self, elem):
        self.queue.append(elem)
        self.queue.sort(key=lambda x: x[1])

    def extract_min(self):
        min_elem = self.queue[0]
        del self.queue[0]
        return min_elem

    def get_len_queue(self):
        return len(self.queue)


if __name__ == '__main__':
    string = input()
    letters = {}
    for letter in string:
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1
    if len(letters) == 1:
        for val in letters.keys():
            letters[val] = '0'
    else:
        pq = PriorityQueue(letters)
        new_dict = []
        while pq.get_len_queue() > 1:
            min_1 = pq.extract_min()
            min_2 = pq.extract_min()
            new_node = (min_1[0] + min_2[0], min_1[1] + min_2[1])
            pq.insert(new_node)
            new_dict.append((min_1[0], 0))
            new_dict.append((min_2[0], 1))
        for key in letters.keys():
            letters[key] = ''
            for elem in new_dict:
                if key in elem[0]:
                    letters[key] += str(elem[1])
    result = ''
    for i in string:
        result += letters[i][::-1]
    print(len(letters), len(result))
    for key, val in letters.items():
        print(key + ': ' + val[::-1])
    print(result)
