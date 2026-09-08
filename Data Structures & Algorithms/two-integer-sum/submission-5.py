class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash = {nums[i]:i} On met num[i] en clé pour trouver les valeur en O(1)
        hash = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash :
                #si on a déja croisé le bon complément on va le chercher en O(1)
                return [hash[diff], i] #toujours le bonne ordre car le hash en retard sur la liste
            else:
                #Sinon on l'ajoute a notre dict
                hash[num] = i