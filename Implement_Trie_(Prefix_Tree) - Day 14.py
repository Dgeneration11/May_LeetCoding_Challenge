# from collections import defaultdict
# class Trie(object):

    
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = defaultdict(set)

#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
        
#         self.trie[word[0]].add(word[1:])
#         # print(self.trie)
#         # t = self.trie
#         # for i in word:
#         #     if i not in t: t[i] = {}
#         #     t = t[i]
#         # t["-"] = True
        
#         # if word not in self.trie:       
#         #     self.trie.append(word)
#         # # print(self.trie)

#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         # print(self.trie[word[0]])
#         return word[1:] in self.trie[word[0]]
#         # if word in self.trie:
#         #     return True
#         # return False

#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         # for i in self.trie:
#         #     if prefix in i:
#         #         return True
#         # return False
#         for i in self.trie[prefix[0]]:
#             start = prefix[1:]
#             if not start:
#                 return True # Single character prefix
            
#             if i.startswith(start):
#                 return True
            
#         return False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        t = self.trie
        
        for w in word: 
            if w not in t: 
                t[w] = {}
            t = t[w]
        t['#'] = True
        print(self.trie)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for w in word: 
            if w not in t: 
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for w in prefix: 
            if w not in t: 
                return False
            t = t[w]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)