from typing import List
import Trie

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        trie = Trie.Trie()
        for w in dictionary:
            trie.insert(w)
        for w in range(0,len(words)):
            word = trie.get(words[w])
            if(word != -1):
                words[w] = word
        return " ".join(words)
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dictionary,sentence))
dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(Solution().replaceWords(dictionary,sentence))
dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(Solution().replaceWords(dictionary,sentence))