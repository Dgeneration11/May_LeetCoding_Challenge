class StockSpanner(object):   
    def __init__(self):
        self.stack = []

    def next(self, price):
        ans = 1
        print(self.stack)
        while self.stack and self.stack[-1][0] <= price:
            print(self.stack[-1][0])
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))
        return ans
        
#         self.prices.append(price)
#         counter = 0

#         for i in self.prices[::-1]:
#             # print(i,price)
#             if i<=price: counter+=1
#             else: break
#         return counter
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)