class UrlNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        homepage = UrlNode(homepage)
        self.homepage = homepage
    def visit(self, url: str) -> None:
        newUrl = UrlNode(url)
        self.homepage.next = newUrl
        newUrl.prev = self.homepage
        self.homepage = newUrl
    def back(self, steps: int) -> str:
        curr = self.homepage
        i = 0
        while curr.prev and i < steps:
            curr = curr.prev
            i += 1
        self.homepage = curr
        return curr.val
    def forward(self, steps: int) -> str:
        curr = self.homepage
        i = 0
        while curr.next and i < steps:
            curr = curr.next
            i += 1
        self.homepage = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)