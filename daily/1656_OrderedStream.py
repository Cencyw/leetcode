# https://leetcode.cn/problems/design-an-ordered-stream/?envType=daily-question&envId=2025-02-24
class OrderedStream:

    def __init__(self, n: int):
        self.lists = [None] * n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.lists[idKey-1]=value
        ret = []
        if self.ptr == idKey - 1 and self.lists[self.ptr]:
            curPtr = self.ptr
            for idx, v in enumerate(self.lists[self.ptr:]):
                # ret.append(idx)
                if v:
                    # pass
                    ret.append(v)
                else:
                    # ret.append(idx)
                    self.ptr = idx + self.ptr
                    # return self.lists
                    break
        return ret 
# os.insert(3, "ccccc"); // 插入 (3, "ccccc")，返回 [] ptr = 0
# os.insert(1, "aaaaa"); // 插入 (1, "aaaaa")，返回 ["aaaaa"] ptr = 1
# os.insert(2, "bbbbb"); // 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"] ptr = 3
# os.insert(5, "eeeee"); // 插入 (5, "eeeee")，返回 []
#ptr = 2
# os.insert(4, "ddddd"); // 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)