class Trie:

    def __init__(self, key=None, next_dict=None):
        self.key = key # "a"
        # 가변 매개변수를 기본값으로 놓으면 객체간 공유를 해서 이곳에
        # {"a": Trie(), "b": Trie(), ...}
        self.next_dict = next_dict if next_dict else dict() # {"a": Trie(), "b": Trie(), ...}

    def insert(self, word: str) -> None:
        now = self # root값
        for w in word:
            if w not in now.next_dict:
                next = now.next_dict[w] = Trie(w)
            else:
                next = now.next_dict[w]
            now = next
        now.next_dict["end"]= True # 끝나는 지점 표시

    def search(self, word: str) -> bool:
        now = self # root값
        for w in word:
            if w not in now.next_dict:
                return False
            else:
                now = now.next_dict[w]
        return "end" in now.next_dict

    def startsWith(self, prefix: str) -> bool:
        now = self # root값
        for p in prefix:
            if p not in now.next_dict:
                return False
            else:
                now = now.next_dict[p]
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
