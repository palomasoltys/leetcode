class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                
        if strs == [""]:
            return [[""]]
        
        anagrams = {}
        
        for i in range(len(strs)):
            
            s = sorted(strs[i])
            s = "".join(s)

            if s in anagrams.keys():
                anagrams[s] += [strs[i]]
            else:
                anagrams[s] = [strs[i]]
      
        return anagrams.values()