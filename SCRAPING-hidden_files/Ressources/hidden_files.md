EXPLAIN: http://192.168.1.87/.hidden/

Robots.txt, est une ressource de format texte qui peut être placée à la racine d'un site web, et qui contient une liste des ressources du site qui ne sont pas censées être indexées par les robots d'indexation des moteurs de recherche.

Ici:
	User-agent: *
	Disallow: /whatever
	Disallow: /.hidden

Def :

Lorsqu’un robot veut inspecter votre site internet, il commence par rechercher /robots.txt et voici ce qu’il trouve :

User-agent: Spécifie les robots autorisés à scanner le site (voire la [liste](http://www.robotstxt.org/db.html)).

Disallow: Empêche le robot d’indexer les repertoires spécifiés.

Si, on va voir dans /.hidden, on voit tout un tas de repertoires imbriqués, contenant des README. Les ouvrir un a un prendrait un temps interminable, il nous faut utiliser une méthode de scrapping.

lorsqu’on en ouvre plusieurs; on voit ce genre de message: 

- Demande à ton voisin
- Non ce n'est toujours pas bon …
- Toujours pas tu vas craquer non ?
- Tu as besoin d’aide ? Nous aussi !

On veut récupérer tous les autres messages. 

**[Apprendre le Web Scraping avec Python Français - Partie 1](https://www.youtube.com/watch?v=Wvc2ZqdIPpk)**

IMPACT : 
 Avec le scraping, on peut recuperer des mails, des numeros de telephone, sur de nombreuses pages web. 
