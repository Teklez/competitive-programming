class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_parenthesis = []
        def generate(generated, open, close):
            if open == close == 0:
                all_parenthesis.append(generated)
                return     
            if open == close:
                generate(generated+"(",open - 1, close)
            elif close > open and open != 0:
                generate(generated+"(",open - 1, close)
                generate(generated+")",open, close - 1)
            elif close > open and open == 0:
                generate(generated+")",open, close - 1)
        generate('', n, n)
        return all_parenthesis


                



                