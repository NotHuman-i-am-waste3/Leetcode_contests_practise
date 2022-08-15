class Solution:
    def largestLocal(self,l):
        m=len(l)-2
        ans=[]
        for k in range(m):
         mat=[];i=0
         while(i<len(l)-2):
            s=[]
            for p in range(i,i+3):
                a=l[p][k:k+3];s+=a
            i+=1
            mat+=[max(s)]
         ans+=[mat]
        ans1=[[j[i] for j in ans] for i in range(m)]
        return ans1
          