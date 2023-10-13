class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(s):
            parts = s.split('.')
            
            if len(parts) != 4:
                return False
            
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (len(part) > 1 and part[0] == '0'):
                    return False
                
            return True

        def is_valid_ipv6(s):
            parts = s.split(':')
            
            if len(parts) != 8:
                return False
            
            for part in parts:
                if not (1 <= len(part) <= 4) or not all(c in '0123456789abcdefABCDEF' for c in part):
                    return False
                
            return True

        if "." in queryIP and ":" in queryIP:
            return "Neither"
        
        elif "." in queryIP and is_valid_ipv4(queryIP):
            return "IPv4"
        
        elif ":" in queryIP and is_valid_ipv6(queryIP):
            return "IPv6"
        
        else:
            return "Neither"