class TextEditor:

    # def __init__(self):
    #     # self.textL = ""
    #     # self.textR = ""
    #     self.text = ""
    #     self.curr = 0

    # def addText(self, text: str) -> None:
    #     # osdhyvqxfyackuncqzcqo
    #     if len(self.text) == 0:
    #         self.text += text
    #         self.curr += len(text)
    #         return
    #     self.text= self.text[:self.curr]+text + self.text[self.curr:]
    #     self.curr = self.curr+len(text)

    # def deleteText(self, k: int) -> int:
    #     if k <= self.curr:
    #         self.text = self.text[:self.curr - k] + self.text[self.curr:]
    #         self.curr-=k
    #         return k 
    #     else:
    #         self.text = self.text[self.curr:]
    #         ans = self.curr
    #         self.curr = 0
    #         return ans

    # def cursorLeft(self, k: int) -> str:
    #     self.curr = max(0,self.curr - k)
    #     l = min(10,self.curr)
    #     return self.text[self.curr - l:self.curr]

    # def cursorRight(self, k: int) -> str:
    #     self.curr = min(len(self.text),k + self.curr)
    #     l = min(10,self.curr)
    #     # return self.text
    #     return self.text[self.curr - l:self.curr]

    def __init__(self):
        self.textL = []
        self.textR = []

    def addText(self, text: str) -> None:
        self.textL.extend(text)

    def deleteText(self, k: int) -> int:
        pre = len(self.textL)
        del self.textL[-k:]
        return pre - len(self.textL)

    def text(self) -> str:
        return "".join(self.textL[-10:])

    def cursorLeft(self, k: int) -> str:
        while k and self.textL:
            self.textR.append(self.textL.pop())
            k-=1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.textR:
            self.textL.append(self.textR.pop())
            k-=1
        return self.text()
if __name__ == "__main__":
    t = TextEditor()
    order = ["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
    input_data = [[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
    for i, command in enumerate(order):
        if command == "TextEditor":
            t = TextEditor()  # 初始化一个新的文本编辑器实例
            print("TextEditor initialized.")
        elif command == "addText":
            text = input_data[i][0]
            t.addText(text)  # 调用 addText
            print(f"addText('{text}')")
        elif command == "deleteText":
            k = input_data[i][0]
            deleted = t.deleteText(k)  # 调用 deleteText
            print(f"deleteText({k}) -> {deleted} characters deleted.")
        elif command == "cursorLeft":
            k = input_data[i][0]
            result = t.cursorLeft(k)  # 调用 cursorLeft
            print(f"cursorLeft({k}) -> {result}")
        elif command == "cursorRight":
            k = input_data[i][0]
            result = t.cursorRight(k)  # 调用 cursorRight
            print(f"cursorRight({k}) -> {result}")
# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)