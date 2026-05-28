# Disjoint set union on an interesting problem. 
# It was not clear at first that this was DSU, but mapping
# things to each email makes sense here. 

# Link: https://leetcode.com/problems/accounts-merge/
class DSU:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]

    def find_parent(self, n1):
        if self.parent[n1] != n1:
            self.parent[n1] = self.find_parent(self.parent[n1])
        return self.parent[n1]
    
    def union(self, n1, n2):
        pn1, pn2 = self.find_parent(n1), self.find_parent(n2)
        if pn1 == pn2:
            return False
        if self.size[pn1] < self.size[pn2]:
            n1, n2, pn1, pn2 = n2, n1, pn2, pn1
        self.size[pn1] += self.size[pn2]
        self.size[pn2] = 0
        self.parent[pn2] = pn1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        email_to_index = defaultdict(list)
        parent_to_child = defaultdict(list)
        res = []

        for i, account in enumerate(accounts):
            for email in account[1::]:
                email_to_index[email].append(i)
        
        for email in email_to_index.keys():
            if len(email_to_index[email]) > 1:
                for i in range(len(email_to_index[email]) - 1):
                    dsu.union(email_to_index[email][i],  email_to_index[email][i + 1])
        
        for i in range(len(accounts)):
            parent_to_child[dsu.find_parent(i)].append(i)
        
        for parent in parent_to_child.keys():
            name = accounts[parent][0]
            emails = set()
            for idx in parent_to_child[parent]:
                for cur_email in accounts[idx][1::]:
                    emails.add(cur_email)
            
            new_account = [name] + sorted(list(emails))
            res.append(new_account)
        return res
