class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} # key: sorted anagram value: index in the output
        ans = []

        for cur in strs:
            sorted_cur = "".join(sorted(cur))
            if sorted_cur not in seen:
                ans.append([cur])
                seen[sorted_cur] = len(ans) - 1
                continue

            # in seen
            ans[seen[sorted_cur]].append(cur)

        return ans

            
