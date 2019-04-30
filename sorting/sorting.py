from random import randrange


# 插入排序 O(N^2) Insertion sorting
# 具有稳定性，适应性
def insertion_sort(array):
    for i in range(1, len(array)):
        # 当前元素 key
        key = array[i]
        j = i - 1
        # 关键点：保证当前元素前面的元素都是已经排序好了的；
        # 当前元素大于前一个元素时，前一个元素顺序后移一位；
        # 等号保证了排序的稳定性
        # keys: assure the element preceding the current element is already sorted.
        while j >= 0 and key <= array[j]:
            array[j + 1] = array[j]
            j -= 1
        # 当前元素大于前一个元素时，将当前元素插入
        array[j + 1] = key
    return array


# 归并排序 O(n * lgn) merge insort
# 并不是原址排序
# 在python中，切片是强大的工具
def merge_sort(array, left, right):
    # 关键点：不能取等号，当left = right时，会出现死循环。
    # 当left > right时停止二分。
    if left < right:
        # 整除[向下取整]
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        # mid + 1 避免了重复取元素，以及由于整除操作造成的死循环。left = mid = right - 1
        merge_sort(array, mid + 1, right)
        # 归并阶段
        return merge(array, left, mid, right)


def merge(array, left, mid, right):
    array_left = array[left:mid + 1]
    array_right = array[mid + 1:right + 1]
    array_left_len = len(array_left)
    array_right_len = len(array_right)
    le, r, i = 0, 0, 0
    # 当前序号未超过上界；
    while i < array_left_len + array_right_len:
        # 左序号未超过上界且右序号未超过上界且当前左边元素更小；
        if le < array_left_len and r < array_right_len and array_left[le] < array_right[r]:
            array[left + i] = array_left[le]
            le += 1
            i += 1
        # 左序号未超过上界且右序号未超过上界且当前右边元素更小；
        elif le < array_left_len and r < array_right_len:
            array[left + i] = array_right[r]
            r += 1
            i += 1
        # 右序号超过上界
        elif le < array_left_len:
            array[left + i] = array_left[le]
            le += 1
            i += 1
        # 左序号超过上界
        else:
            array[left + i] = array_right[r]
            r += 1
            i += 1
    return array


# 快速排序 O(N^2)
def quick_sort(array, left, right):
    # 设计思想
    if left > right:
        return array
    key = array[left]
    # 失误1
    i, j = left, right
    while i != j:
        # 失误2 IndexError: list index out of range
        while i != j and array[j] > key:
            # i, j的顺序执行可能会导致错过i == j,当i, j进行增减时，应时刻保持i != j
            j -= 1
        array[i] = array[j]
        while i != j and array[i] <= key:
            i += 1
        array[j] = array[i]
    # 失误3
    array[i] = key
    # 失误4
    quick_sort(array, left, i - 1)
    quick_sort(array, i + 1, right)
    return array


# 递归形式的快速排序
def quick_sorting(array, left, right):
    if left < right:
        q = paratition(array, left, right)
        quick_sorting(array, left, q - 1)
        quick_sorting(array, q + 1, right)
    return array


def paratition(array, left, right):
    q = left + 1
    key = array[q]
    for i in range(left + 1, right + 1):
        if array[i] < array[left]:
            array[q] = array[i]
            array[i] = key
            if q < right:
                q += 1
                key = array[q]
    if q == right and array[q] < array[left]:
        array[q] = array[left]
        array[left] = key
    else:
        q = q - 1
        key = array[q]
        array[q] = array[left]
        array[left] = key
    return q


# 计数排序 O(M + N)
def count_keys_equal(array, m):
    array_len = len(array)
    equal = [0 for i in range(m)]
    for i in range(array_len):
        equal[array[i]] += 1
    return equal


def count_keys_less(equal):
    equal_len = len(equal)
    less = [0 for i in range(equal_len)]
    for i in range(1, equal_len):
        less[i] = less[i - 1] + equal[i - 1]
    return less


def count_sort(array, less):
    array_len = len(array)
    count_array = [0 for i in range(array_len)]
    for i in range(array_len):
        count_array[less[array[i]]] = array[i]
        less[array[i]] += 1
    return count_array


def count_key_sort(array, m):
    equal = count_keys_equal(array, m)
    less = count_keys_less(equal)
    return count_sort(array, less)


# 基数排序
def radix_sort(array):
    radix = {}
    length = len(array)
    maxs = 0
    for i in range(length):
        m = 1
        while array[i] // (10 ** m) != 0:
            m += 1
        if m > maxs:
            maxs = m
    t = 1
    while t <= maxs:
        i, j, k = 0, 0, 0
        if t <= 1:
            while i < length:
                if radix.get(array[i] % (t * 10)) is None:
                    radix[array[i] % (t * 10)] = [array[i]]
                else:
                    radix[array[i] % (t * 10)].append(array[i])
                i += 1
            while k < length:
                if radix.get(j) is not None:
                    if len(radix[j]) >= 2:
                        for i in range(len(radix[j])):
                            array[k] = radix[j][i]
                            k += 1
                        j += 1
                    else:
                        array[k] = radix[j][0]
                        k += 1
                        j += 1
                else:
                    j += 1
            radix = {}
        else:
            while i < length:
                if radix.get(array[i] // ((t - 1) * 10)) is None:
                    radix[array[i] // ((t - 1) * 10)] = [array[i]]
                else:
                    radix[array[i] // ((t - 1) * 10)].append(array[i])
                i += 1
            while k < length:
                if radix.get(j) is not None:
                    if len(radix[j]) >= 2:
                        for i in range(len(radix[j])):
                            array[k] = radix[j][i]
                            k += 1
                        j += 1
                    else:
                        array[k] = radix[j][0]
                        k += 1
                        j += 1
                else:
                    j += 1
            radix = {}
        t += 1
    return array


# 基数排序(改进)
def radix_sorting(array):
    radix = {}
    length = len(array)
    # 得到待排序的元素中最大值的位数
    m = 1
    max_num = max(array)
    while max_num // (10 ** m) != 0:
        m += 1
    t = 1
    while t <= m:
        i, j, k = 0, 0, 0
        while i < length:
            # num: 待求的数；
            # t: num的位数
            # 计算每一位的基数：(num // (10^(t - 1))) % (t * 10)
            if radix.get((array[i] // (10 ** (t - 1))) % (t * 10)) is None:
                radix[(array[i] // (10 ** (t - 1))) % (t * 10)] = [array[i]]
            else:
                radix[(array[i] // (10 ** (t - 1))) % (t * 10)].append(array[i])
            i += 1
        while k < length:
            if radix.get(j) is not None:
                if len(radix[j]) >= 2:
                    for i in range(len(radix[j])):
                        array[k] = radix[j][i]
                        k += 1
                    j += 1
                else:
                    array[k] = radix[j][0]
                    k += 1
                    j += 1
            else:
                j += 1
        radix = {}
        t += 1
    return array


# 拓扑排序
def topological_sort(V, E):
    i = 0
    e_num = len(E)
    v_num = len(V)
    while V:
        res = False
        if i < v_num:
            if e_num == 0:
                print(V[i], end=' ')
                del V[i]
                v_num -= 1
            j = 0
            while j < e_num and V[i] != E[j][1]:
                j += 1
                if j == e_num:
                    j = 0
                    while j < e_num and V[i] != E[j][0]:
                        j += 1
                        if j == e_num:
                            print(V[i], end=' ')
                            del V[i]
                            v_num -= 1
                    j = 0

                    while j < e_num and i < v_num:
                        if V[i] == E[j][0]:
                            del E[j]
                            e_num -= 1
                            res = True
                            j = 0
                            continue
                        j += 1
                    if res:
                        print(V[i], end=' ')
                        del V[i]
                        v_num -= 1

                    break

            i += 1
            continue
        i = 0


# 选择排序
def select_sort(array):
    for i in range(len(array) - 1):
        key = i
        for j in range(i, len(array)):
            if array[key] > array[j]:
                key = j
        temp = array[key]
        array[key] = array[i]
        array[i] = temp
    return array


# 冒泡排序
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array


# 冒泡排序（优化）
def bubble_sorting(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
            elif j == len(array) - 1 - i:
                break
    return array


# 分析排序算法的正确性
def correct_test(funa, funb, num):
    times = 0
    count = 0
    while count < num:
        m = [randrange(0, 10) for i in range(10)]
        n = m[:]
        funa(m)
        funb(n)
        # funb(n, 0, len(n) - 1)
        i, j = len(m) - 1, len(n) - 1
        if i == j:
            while i >= 0:
                if m[i] != n[j]:
                    break
                i -= 1
                j -= 1
            # 又一次，若判断条件为i == 0会错误，因为在i = 0之后，i又发生了变化
            if i == -1:
                times += 1
        count += 1
    return str((times / count) * 100) + '%'


# 堆排序
def heap_sort(array):
    def siftdown(array, begin, end, e):
        i, j = begin, begin * 2 + 1
        while j <= end:
            if j + 1 <= end and array[j] < array[j + 1]:
                j += 1
            if e > array[j]:
                break
            array[i], array[j] = array[j], array[i]
            i, j = j, j * 2 + 1
        array[i] = e

    array_len = len(array)
    for i in range(array_len - 1, -1, -1):
        siftdown(array, i, array_len - 1, array[i])
    for j in range(array_len - 1, -1, -1):
        array[j], array[0] = array[0], array[j]
        siftdown(array, 0, j - 1, array[0])
    return array


def _test():
    pass
    # 排序算法正确性测试
    print(correct_test(insertion_sort, heap_sort, 100000))
    # print(correct_test(insertion_sort, select_sort, 100000))
    # print(correct_test(insertion_sort, quick_sorting, 100000))
    # print(correct_test(insertion_sort, bubble_sorting, 100000))

    # 测试：插入排序
    # print("插入排序:O(N^2)")
    # test_array_a = [randrange(0, 10) for i in range(10)]
    # print(insertion_sort(test_array_a))

    # 测试：归并排序
    # print("归并排序:O(n * lgn)")
    # test_array_b = [randrange(0, 10) for j in range(10)]
    # print(merge_sort(test_array_b, 0, len(test_array_b) - 1))

    # 测试：快速排序
    # print("快速排序:O(N^2)")
    # test_array_c = [randrange(0, 10) for m in range(10)]
    # print(quick_sort(test_array_c, 0, len(test_array_c) - 1))

    # 测试：基数排序
    # print("基数排序:O(N^2)")
    # test_array_d = [randrange(0, 10) for n in range(10)]
    # print(radix_sort(test_array_d))

    # 测试：选择排序
    # test_array_e = [randrange(0, 10) for n in range(10)]
    # print(select_sort(test_array_e))

    # 测试：快速排序(递归)
    # print("快速排序(递归):O(N^2)")
    # test_array_f = [randrange(0, 10) for n in range(10)]
    # print(quick_sorting(test_array_f, 0, len(test_array_f) - 1))

    # 测试：计数排序
    # print("计数排序:O(N + M)")
    # test_array_g = [randrange(0, 10) for n in range(10)]
    # print(count_key_sort(test_array_g, 10))

    # 测试：基数排序(改进)
    # print("基数排序:O(N^2)(改进)")
    # test_array_h = [randrange(0, 10) for n in range(10)]
    # print(radix_sorting(test_array_h))

    # 测试：冒泡排序
    # print("冒泡排序:O(N^2)")
    # test_array_i = [randrange(0, 10) for n in range(10)]
    # print(bubble_sort(test_array_i))

    # 测试：冒泡排序(优化)
    # print("冒泡排序(优化):O(N^2)")
    # test_array_j = [randrange(0, 10) for n in range(10)]
    # print(bubble_sorting(test_array_j))

    # 测试：冒泡排序(优化)
    print("冒泡排序(优化):O(N^2)")
    test_array_k = [randrange(0, 10) for n in range(10)]
    print(heap_sort(test_array_k))

    # 测试：拓扑排序
    # print("拓扑排序:")
    # V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # E = [(3, 0), (3, 2), (2, 1), (2, 5), (0, 8), (0, 7), (2, 9), (5, 8)]
    # topological_sort(V, E)


if __name__ == "__main__":
    _test()
