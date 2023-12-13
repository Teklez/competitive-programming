class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenId = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenId[tokenId] = currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenId:
            if self.tokenId[tokenId] + self.timeToLive > currentTime:
                self.tokenId[tokenId] = currentTime
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key, value in self.tokenId.items():
            if value + self.timeToLive > currentTime:
                count += 1
        return count


        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)