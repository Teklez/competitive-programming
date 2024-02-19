class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(operand1, operand2, operator):
            result = 0
            if operator == "+":
                result = operand1 + operand2
            elif operator == "-":
                result = operand1 - operand2
            elif operator == "*":
                result = operand1 * operand2
            else:
                result = int(operand1 / operand2)
            return result
        expression = []
        operators = {"*", "-", "+", "/"}
        for token in tokens:
            if token in operators:
                operand2 = expression.pop()
                operand1  = expression.pop()
                expression.append(evaluate(operand1, operand2, token))
            else:
                expression.append(int(token))
        return expression[-1]



