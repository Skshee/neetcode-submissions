class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
            elif char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(char)
            elif char == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(char)
        if stack == []:
            return True
        else:
            return False
                    
        