from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # char별 최대 인덱스를 hash table에 미리 계산해두기
        ch_max_idx = defaultdict(int)
        for i, ch in enumerate(s):
            ch_max_idx[ch] = max(ch_max_idx[ch], i)

        ans = []
        first_index = 0
        last_index = 0
        for i, ch in enumerate(s):
            # last_index 갱신
            last_index = max(last_index, ch_max_idx[ch])

            # 끝나는 위치면
            if i == last_index:
                ans.append(last_index - first_index + 1)
                first_index = i + 1
                last_index = i + 1

        return ans


# 개선 전 풀이(해시테이블을 이용하지 않은)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        first_index = 0
        last_index = 0
        for i, ch in enumerate(s):
            # last_index 갱신
            for j in range(i + 1, len(s)):
                if s[j] == ch:
                    last_index = max(last_index, j)

            # 끝나는 위치면
            if i == last_index:
                ans.append(last_index - first_index + 1)
                first_index = i + 1
                last_index = i + 1

        return ans