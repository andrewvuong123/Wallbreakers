from collections import Counter
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # General Idea: Initialize a Counter. Iterate through cpdomains and separate domain from count using split, then separate each subdomain by splitting by ".". Nested loop through the range of the resulting subdomain list and join by "." using each subdomain and add that item plus the count to the counter. 
        
        c = Counter()
        for domain in cpdomains:
            count, domain = domain.split() # split count from domain
            count = int(count) # convert str to int
            sub = domain.split(".")
            for i in range(len(sub)):
                c[".".join(sub[i:])] += count

        return [str(count)+" "+str(domain) for domain, count in c.items()]
        