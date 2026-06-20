class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)#mapping char count to list of anagrams

        for s in strs:
            count = [0]*26 #a .. to Z for every position

            for c in s.lower():
                count[ord(c) - ord('a')] +=1
            
            res[tuple(count)].append(s)

        return list(res.values())