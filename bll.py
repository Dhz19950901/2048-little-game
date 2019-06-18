class move:
    def __init__(self):
        self.list_target = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4,
        ]
        print(self.list_target)

    def zero_to_end(self, list_target):
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] == 0:
                del list_target[i]
                list_target.append(0)

    def sum_number(self, list_target):
        self.zero_to_end(list_target)
        for i in range(len(list_target) - 1):
            if list_target[i] == list_target[i + 1]:
                list_target[i] += list_target[i + 1]
                del list_target[i + 1]
                list_target.append(0)

    def move_left(self, map):
        for line in map:
            self.sum_number(line)

    def move_right(self, map):
        for i in range(len(map)):
            list_sum_number = map[i][::-1]
            self.sum_number(list_sum_number)
            map[i][::-1] = list_sum_number

    def move_up(self, map):
        list02 = []
        list03 = []
        list04 = []
        x = 0
        y = 0
        for r in range(4):
            for item in map:
                list02.append(item[x])
            x += 1
            list03.append(list02)
            list02 = []
        self.move_left(list03)

        for r in range(4):
            for i in list03:
                list02.append(i[y])
            y += 1
            list04.append(list02)
            list02 = []
        map.clear()
        map.extend(list04)

    def move_down(self, map):
        list02 = []
        list03 = []
        list04 = []
        x = 0
        y = 0
        for r in range(4):
            for item in map:
                list02.append(item[x])
            x += 1
            list03.append(list02)
            list02 = []
        self.move_right(list03)

        for r in range(4):
            for i in list03:
                list02.append(i[y])
            y += 1
            list04.append(list02)
            list02 = []
        map.clear()
        map.extend(list04)


m = move()
