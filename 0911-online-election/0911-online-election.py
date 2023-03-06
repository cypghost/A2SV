class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.lead = [0] * len(self.times)
        self.leader = persons[0]
        self.votes = defaultdict(int)

        for index in range(len(persons)):
            self.votes[self.persons[index]] += 1
            
            if self.votes[self.persons[index]] >= self.votes[self.leader]:
                self.leader = self.persons[index]
            
            self.lead[index] = self.leader
    
    def q(self, t: int) -> int:
        index = bisect_left(self.times, t)
        
        if index > len(self.times) - 1:
            return self.lead[index - 1]
        
        if self.times[index] == t:
            return self.lead[index]
            
        return self.lead[index - 1]
                


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)