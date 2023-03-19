## python3
# Maksims Jakusevs 221RDB376

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        sift_down(i, data, swaps)

    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    r_child = 2 * i + 2
    l_child = 2 * i + 1

    incorrect_child_candidate = 0

    if l_child < len(data):
        if r_child >= n or not correct_parent_to_child_relation(data[r_child], data[l_child]):
            incorrect_child_candidate = l_child
        else:
            incorrect_child_candidate = r_child

        if not correct_parent_to_child_relation(data[i], data[incorrect_child_candidate]):
            swaps.append([i, incorrect_child_candidate])
            data[i], data[incorrect_child_candidate] = data[incorrect_child_candidate], data[i]
            sift_down(incorrect_child_candidate, data, swaps)
        


def correct_parent_to_child_relation(parent, child):
    if parent <= child:
        return True
    else:
        return False

def main():

    input_type = input()
    if 'I' in input_type:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in input_type:
        file_name = str(input())
        path = "tests/" + file_name
        if not "a" in path:
            with open(path, 'r') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    else:
        exit()
    assert len(data) == n
    swaps = build_heap(data)

    print(len(swaps))
    if not 'F' in input_type:
        for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()