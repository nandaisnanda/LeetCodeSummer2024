class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        awal = strs[0]
        
        for s in strs[1:]:
            while s[:len(awal)] != awal and awal:
                awal = awal[:-1]
            if not awal:
                return ""
        
        return awal
