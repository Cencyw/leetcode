class BrowserHistory:

    def __init__(self, homepage: str):
        self.histrory = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.histrory = self.histrory[:self.cur+1]
        self.histrory.append(url)
        self.cur = len(self.histrory) - 1

    def back(self, steps: int) -> str:
        if steps <= self.cur:
            self.cur = self.cur - steps
            return self.histrory[self.cur]
        self.cur = 0
        return self.histrory[0]

    def forward(self, steps: int) -> str:
        x = len(self.histrory) - 1 - self.cur
        if steps <= x:
            self.cur = self.cur + steps
            return self.histrory[self.cur]
        self.cur = len(self.histrory) - 1
        return self.histrory[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)