from collections import Counter
class stats:
    def __init__(self, lst):
        self.lst = lst

    def mean(self):
        summer = sum(lst)
        n = len(lst)
        mean = summer / n
        return "Mean : " + str(mean)
    
    def median(self):
        n = len(lst)
        lst_sort = lst
        lst_sort.sort()
        median = lst_sort[n//2]
        return "Median : " + str(median)
    
    def mode(self):
        lister = lst
        n = len(lst)
        data = Counter(lister)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

        if len(mode) == n:
            get_mode = "Node mode found"
        else: 
            get_mode = "Mode is / are: " + ', '.join(map(str,mode))
        return get_mode
    
    def answer(self):
        ans = []
        mean_ans = self.mean()
        median_ans = self.median()
        mode_ans = self.mode()
        ans.append(mean_ans)
        ans.append(median_ans)
        ans.append(mode_ans)
        return ans
    
n = 0
lst = []
while True:
    n = int(input("Enter an odd number : "))
    if(n%2 != 0):
        break

for i in range(0,n):
    a = int(input("Enter a number : "))
    lst.append(a)

print(lst)

stat = stats(lst)

print(stat.answer())