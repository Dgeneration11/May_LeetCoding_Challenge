 def removeKdigits(self, num, k):
 
        #Greedy approach
        result = []
        for i in range(len(num)):
            while k>0 and result and num[i]<result[-1]:
                print(k,num[i],result)
                result.pop()
                k-=1
            result.append(num[i])
            print(result)
        if k>0:
            result = result[:len(result)-k]
        result = ''.join(result).lstrip('0')

        return result if result!="" else '0'