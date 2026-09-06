class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)
        for i in strs:
            s = ''.join(sorted(i))
            r[s].append(i)
        return list(r.values())
        