#Time_Complexity: O(n)
#Space_Complexity: O(n)


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]* n   #Initialize indegree array of 0s to n
        for person, trusted in trust:   #For every person and trusted in trust list
            indegree[person-1] -= 1 #Subtract the value of person in indegree by 1
            indegree[trusted-1] += 1    #Add the value of trusted by 1
            
        for i in range(len(indegree)):  #Continue till the lenf=ght of indegree
            if indegree[i] == n-1:  #If the value of indegree is equal to n-1
                return i+1  #Return index+1 which gives the Town Judge

        return -1   #If there is not Tonw Judge then return False
     
        