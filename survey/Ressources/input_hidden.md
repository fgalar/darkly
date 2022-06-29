EXPLAIN: http://{HOST}/?page=survey
Il s’agit d’un formulaire à choix : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

javascript:this.form.submit() → lorsque qu’une valeur est sélectionnée cela envoie l’input et la valeur sélectionnée au back.

Comment envoyer des données non proposées par le formulaire à choix? 
1. Changer la valeur d'une des options value dans la balise select.
2. cURL
	-X POST → requete POST au serveur
	-d args → envoyer les args ainsi “arg1=lorem&arg2=Ipsum”

le serveur attend deux valeurs :
<input type="hidden" **name**="sujet" value="2">
<select name="valeur" onchange="javascript:this.form.submit();">

curl -d “sujet=20&valeur=20” -X POST http://{HOST}/index.php?page=survey

AVOID
Toujours verifier que les donnees recues correspondent aux donnees attendues
