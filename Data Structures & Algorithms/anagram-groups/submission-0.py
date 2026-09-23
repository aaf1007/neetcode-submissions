class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        iter strs[] and strings to ans[]
        strs = ["act","pots","tops","cat","stop","hat"]
                                            ^
                cur = "stop"
        ans = [["act", "cat"],["pots", "tops", "stop"], ["hat"]]
        seen = {
            "act": 0,
            "pots": 1,
            "hat": 2,
        }
        """

        ans = []
        seen = {}
        for cur in strs:
            if "".join(sorted(cur)) in seen:
                i = seen.get("".join(sorted(cur)))
                ans[i].append(cur)
                continue

            # not in seen
            i = len(ans)
            ans.append([cur])
            seen["".join(sorted(cur))] = i

        return ans