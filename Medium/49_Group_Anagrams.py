##Q49 Group Anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        grp={}
        for item in strs:
            key = "".join(sorted(item))
            grp[key]=grp.get(key,[])
            grp[key].append(item)
        return grp.values()
