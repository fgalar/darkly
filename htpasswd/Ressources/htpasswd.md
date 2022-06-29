EXPLAIN
Dans le fichier robots.txt, nous voyons que le dossier whatever est interdit a l'indexation.
http://{HOST}/whatever/htpasswd > root:8621ffdbc5698829397d97767ac13db3
md5 decrypt : dragon
Avec Dirb, on voit qu'il existe une page de log dans /admin.
On rentre root/dragon

AVOID
Empecher l'acces a ce genre de fichier sensible avec htaccess.
