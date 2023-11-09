class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                stack.append((current_string, k))  # 지금까지만든 문자열, 뒤에서 만들어질 문자열에 곱할 값
                current_string = ""
                k = 0
            elif char == "]":
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string  # 시간복잡도?
            elif char.isdigit():
                k = k * 10 + int(char)  # 2자리 이상일 수 있으니
            else:
                current_string += char

        return current_string