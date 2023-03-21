class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        def cmp(plant, grow):
            plant1 = max(plant[0] + grow[0] + grow[1], plant[0] + plant[1])
            grow1 = max(grow[0] + plant[0] + plant[1], grow[0] + grow[1])
        
            return plant1 - grow1

        indices = sorted(zip(plantTime, growTime), key=functools.cmp_to_key(cmp))
        curr = 0
        latest = 0

        for plant, grow in indices:
            latest = max(latest, plant + grow + curr)
            curr += plant
        
        return latest