class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1]*len(nums)

        # logique : le produit recherché pour un élément d'indice i est le produit
        # des éléments d'indices strictement supérieures et inférieures (préfixes 
        #et suffices)
        
        prefixe = 1
        for i in range(len(nums)):
            output[i] *= prefixe
            prefixe = nums[i]*prefixe #produit des éléments d'indice inf

        suffixe = 1
        for i in range(len(nums)-1, -1,-1):
            output[i] *= suffixe  
            suffixe = nums[i]*suffixe #produit des éléments d'indice sup
        
        
        return output

