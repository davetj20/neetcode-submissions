class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss={}
        st={}
        for x in s :
            ss[x]=ss.get(x,0)+1
        for x in t :
            st[x]=st.get(x,0)+1
        print(ss)
        print(st)
        if (ss == st) and (len(s) == len(t)):
            return True
        return False