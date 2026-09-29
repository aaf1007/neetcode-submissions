class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for word in strs:
            length = len(word)
            ans += f"{length}#{word}"

        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            ans.append(s[j+1 : j + length + 1])

            i = j + length + 1

        return ans


"""
    "5#Hello5#World" -> "Hello" "World"
           ^
    "#0" -> ""

    "#1 " -> " "

"""