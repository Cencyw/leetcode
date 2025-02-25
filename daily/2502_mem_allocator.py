class Allocator:

    def __init__(self, n: int):
        self.mem = [0]*n


    def allocate(self, size: int, mID: int) -> int:
        free = 0
        for i, idx in enumerate(self.mem):
            if idx > 0:
                free = 0
                continue
            free += 1
            if free == size:
                # return free
                self.mem[i - free + 1:i + 1] = [mID]*size
                return i - free + 1
        return -1


    def freeMemory(self, mID: int) -> int:
        free = 0
        for i,idx in enumerate(self.mem):
            if idx == mID:
                free+=1
                self.mem[i] = 0
        return free

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)