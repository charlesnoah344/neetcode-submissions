class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # la clé c'est c'est le nombre num et la valeur c'est le nombre d'occurences
        hash = {}
        for num in nums :
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        occ = sorted(list(hash.values()))
        occ = occ[-k:]

        output = []
        for num in hash.keys():
            if hash[num] in occ:
                output.append(num)
        
        return output
                