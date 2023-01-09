from collections import defaultdict

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
#         domainssub = defaultdict()
        
#         for domain in cpdomains:
#             rep, domain = domain.split()
            
#             rep = int(rep)
#             subdomain = domain.split('.')
            
#             for char in range(len(subdomain)):
#                 domainssub[".".join(subdomain[char:])] += rep
                
#         return ["{rep} {domain}" for domain, rep in domainssub.items()]
    
#         domainssub = defaultdict()
        
#         for domain in cpdomains:
            
#             domain = domain.split(' ')
#             subdomain = domain[1].split('.')
            
#             char = 0
#             while char != -1:
#                 char = domain[1].find('.', char + 1)
#                 domainssub[domain[1][char + 1:]] += int(domain[0])
                
#         answer = []
        
#         for rep, domain in domainssub.items():
#             answer.append(str(rep) + " " + domain)
            
#         return answer


        domainssub = defaultdict(lambda:0)
    
        for domain in cpdomains:
            subdomain = domain.split(' ')
            domains = subdomain[1].split('.')
            char = 0
            
            while char != -1:
                char = subdomain[1].find('.', char + 1)
                domainssub[subdomain[1][char + 1:]] += int(subdomain[0])
                
        answer = []
        
        for domain, rep in domainssub.items():
            answer.append(str(rep) + " " + domain)
            
        return answer

