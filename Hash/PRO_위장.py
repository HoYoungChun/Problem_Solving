from collections import defaultdict
from functools import reduce


def solution(clothes):

    # 입력받아서 종류의 수를 list에 저장
    input_dict = defaultdict(int)

    for one_cloth_pair in clothes:
        input_dict[one_cloth_pair[1]] += 1
    cloth_kind_nums = list(input_dict.values())

    one_plus_cloth_kind_nums = list(map(lambda x: x+1, cloth_kind_nums))
    return reduce(lambda x, y: x*y, one_plus_cloth_kind_nums) - 1


# # 시간초과 풀이
# from collections import defaultdict
# from itertools import combinations
# from functools import reduce
#
#
# def solution(clothes):
#     answer = 0
#
#     # 입력받아서 종류의 수를 list에 저장
#     input_dict = defaultdict(int)
#
#     for one_cloth_pair in clothes:
#         input_dict[one_cloth_pair[1]] += 1
#     cloth_kind_nums = list(input_dict.values())
#
#     answer += sum(cloth_kind_nums)  # 1개의 cloth만 입을 때 경우의 수 더하기
#     for wear_cloth_num in range(2, len(cloth_kind_nums) + 1):
#         wear_cloth_idxs = combinations(range(len(cloth_kind_nums)), wear_cloth_num)
#         for wear_cloth_idx_tuple in wear_cloth_idxs:
#             answer += mutiple_on_idxs(cloth_kind_nums, wear_cloth_idx_tuple)
#
#     return answer
#
#
# def mutiple_on_idxs(cloth_kind_nums, wear_cloth_idx_tuple):
#     filtered_cloth_kind_nums = [x for i, x in enumerate(cloth_kind_nums) if i in wear_cloth_idx_tuple]
#     return reduce(lambda x, y: x * y, filtered_cloth_kind_nums)

