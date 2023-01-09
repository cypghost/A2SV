from collections import defaultdict

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domainssub = defaultdict(lambda:0)
    
        for domain in cpdomains:
            subdomain = domain.split(' ')
            domains = subdomain[1].split('.')
            char = 0
            
            while char >= 0:
                char = subdomain[1].find('.', char + 1)
                domainssub[subdomain[1][char + 1:]] += int(subdomain[0])
                
        answer = []
        
        for domain, rep in domainssub.items():
            answer.append(str(rep) + " " + domain)
            
        return answer

