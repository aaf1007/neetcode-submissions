class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'}' : '{', ']' : '[', ')' : '('}
        stack = []

        for c in s:
            if c in hashmap:
                # closing bracket
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if hashmap[c] != popped:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else: 
            return False
