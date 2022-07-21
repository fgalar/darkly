EXPLAIN: http://{HOST}/index.php?page=feedback

Sur cette page on va pouvoir laisser un commentaire a la vu de tous.

**NON PERSISTANT (code injecté non sauvegardé mais s’execute à sa lecture)**

1 ) onsubmit = return validate_form(this) **VS** onclick = return checkForm() 

- validate_form : regarde si les inputs ne sont pas vides
- la fonction checkForm() n’existe pas

⇒ On peut changer les fonctions de validation et envoyer un formulaire vide 

Pour plus de sécurité, il vaut mieux gérer les vérifications de formulaire dans le back, afin que les functions de vérifications ne soit pas modifiable par les utilisateurs.

**PERSISTANT (code conservé sur une base de donnée ou tout autre stockage)**

2 ) On voit que l’input name prend en compte les balises HTML, et les exécute. 

- <u>name
    ⇒ Name est souligné

- <script>alert(”coucou”)</script>
    ⇒ la balise script est supprimée

- <sCrIpT>alert(”lol”)</ScrIpt>
    ⇒ On affiche bien lol en alerte

DANGER :
on envoie : document.location="http://mon-site"
Et on peut renvoyer l'utilisateur sur notre propre site tout en recuperant tous ses cookies par exemple.

BUG CTF:  
- a en commentaire
- e en name sans commentaire
