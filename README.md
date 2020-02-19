#Hill Cipher

Ce programme permet de chiffrer avec le chiffrement de Hill un suite de caracteres. 
A noter :
Les espaces sont retirés et pour les mots comportant un nombre impair de lettres, le caractere '_' est ajouté pour permettre un chiffrement plus facile. le caractere '_' est référencé dans encodingChar tel que encodingChar[26] = '_'.
Ainsi on fait les operations modulo 27 pour ajouter ce caractere. On utilise donc la meme methode de calcul mais l'alphabet est modifié.


Pour l'encodage, utiliser une matrice qui ne possede pas d'inverse ne pose pas de probleme, cependant il ne sera pas possible de decoder le message.

Il n'est pour le moment pas possible de decoder le message. A ajouter dans la prochaine MaJ. 
La fonction decode() ne fonctionne pas correctement.
