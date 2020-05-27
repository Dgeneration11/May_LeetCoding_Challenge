def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = collections.Counter(s)
        fin = []
        
        for char,freq in freq.most_common():
            fin.extend([char]*freq)
            
        return "".join(fin)
        
#         res = {}
#         fin = ""
#         lis = []
        
#         for i in s:
#             lis.append((i,s.count(i)))            
#             res[i]=s.count(i)

#         sorLis = sorted(lis,key = itemgetter(1),reverse = True)
#         sorLis = set(sorLis)
#         newSorLis = sorted(sorLis,key = itemgetter(1),reverse = True)

#         for i in newSorLis:
#             # print(i[1],fin.count(i[0]))
#             while fin.count(i[0])<i[1]:
#                 fin += i[0]

#         # print(fin)
#         return fin
