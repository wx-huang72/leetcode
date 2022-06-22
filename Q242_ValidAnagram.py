class Solution:
    def isAnagram(self, s, t):
        
        return sorted(s) == sorted(t)
    
        if len(s) != len(t):
            return False
        
        s_list = list(s)
        t_list = list(t)
        s_dic = {}
        t_dic = {}
        for i in s_list:
            s_dic[i]= s_list.count(i)
        for j in t_list:
            t_dic[j] = t_list.count(j)
        for c in s_dic:
            if s_dic[c] != t_dic.get(c):
                return False
        return True   

    isAnagram("anagram","nagaram")     
