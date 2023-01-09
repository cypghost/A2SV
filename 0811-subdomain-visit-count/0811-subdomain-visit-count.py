from collections import defaultdict

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # stores the reps and domains to prepare them for later operations
        domainssub = defaultdict(lambda:0)
    
        # determine the rep, d1.d2.d3 from the sub domains
        for domain in cpdomains:
            subdomain = domain.split(' ')
            domains = subdomain[1].split('.')
            char = 0
            
            # if there exists same domains, adds reps with same domains
            while char >= 0:
                char = subdomain[1].find('.', char + 1)
                domainssub[subdomain[1][char + 1:]] += int(subdomain[0])
                
        answer = []
        
        # joins the reps and domains to append it to answer
        for domain, rep in domainssub.items():
            answer.append(str(rep) + " " + domain)
        
        # returns the cpdomains 
        return answer

