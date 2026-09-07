class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
        #Dictionnaire vide ou l'on gardera la valeur du mot trié par ordre croissant en clé et en valeur la liste des indices de ses annagrammes
        hash = defaultdict(list)
        for i, string in enumerate(strs) :
            #Si l'annagramme du mot est déja dans le dict, on ajoute l'indice dans le strs du nouvel annagrame trouvé dans le dict;
             #Sinon on cree la liste 
            hash[str(sorted(string))].append(i)       
        output = []
        for indexs in hash.values() :
            anagram = []
            for index in indexs:
                anagram.append(strs[index])
            output.append(anagram)
        return output
            


        