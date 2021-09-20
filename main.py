import collections

N = 6
K = 2

n1 = [0, 1, 1, 0, 0, 0]
n2 = [1, 0, 1, 0, 0, 0]
n3 = [0, 0, 1, 1, 0, 0]
n4 = [1, 0, 0, 0, 1, 0]
n5 = [0, 0, 0, 0, 1, 1]
n6 = [1, 0, 0, 0, 0, 1]
matrix = [n1, n2, n3, n4, n5, n6]
logicalOperations = ["{0} and {1}",
                     "{0} or {1}",
                     "{0} != {1}",
                     "not({0} and {1})",
                     "not({0} or {1})",
                     "not({0} != {1})",
                     "{0} == {1}"]


def main():
    attractors = []
    vector = [0 for _ in range(N)]
    for i in range(2 ** N):
        refill(vector, i)
        state(vector, attractors)
    uniqueAttractor(attractors)


def refill(vector, iter):
    j = 0
    for i in range(len(vector)):
        vector[i] = 0
    while True:
        vector[j] = iter % 2
        iter //= 2
        if iter == 0:
            break
        j += 1


def state(vector, attractors):
    print(f"\nvector {vector}")
    string = vectorToStr(vector)
    temp = [string]
    for i in range(2 ** N):
        for j in range(N):
            pos = find(matrix[j])
            for k in range(N):
                vector[j] = int(eval(logicalOperations[k].format(vector[pos[0]], vector[pos[1]])))
        print(f"State {i + 1} {vector}")
        string = vectorToStr(vector)
        if string in temp:
            attractors.append(temp)
            return
        else:
            temp.append(string)


def vectorToStr(vector):
    return "".join([str(i) for i in vector])


def find(vector):
    return [i for i, x in enumerate(vector) if x == 1]


def uniqueAttractor(attractors):
    uniqueAttractors = dict()
    for i in range(len(attractors)):
        sum = ""
        for j in range(N):
            tempSum = 0
            for k in range(len(attractors[i])):
                tempSum += int(attractors[i][k][j])
            sum += str(tempSum)
        uniqueAttractors[sum] = i
    j = 1
    uniqueAttractors = collections.OrderedDict(sorted(uniqueAttractors.items()))
    for index, el in uniqueAttractors.items():
        print(f"\natr {j}")
        for i in attractors[el]:
            print(i)
        j += 1
    print(f"Unique atr {len(uniqueAttractors)}")
    length = 0
    for el in attractors:
        length += len(el)
    print(f"Overage len {length // len(attractors)}")


if __name__ == '__main__':
    main()
