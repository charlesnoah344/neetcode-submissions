class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
        #Dictionnaire vide ou l'on gardera la valeur du mot trié par ordre croissant en clé et en valeur la liste des indices de ses annagrammes
        hash = defaultdict(list) # permet de créer un dictionnaire qui attends des listes en valeurs
        for string in strs :
            #Si l'annagramme trié du mot est déja dans le dict, on ajoute le nouvel annagrame trouvé en tant que valeur;
             #Sinon on cree la liste vide en temps que valeur et l'anagramme trié en clé
            hash[str(sorted(string))].append(string)

        return list(hash.values())       
        
            


        