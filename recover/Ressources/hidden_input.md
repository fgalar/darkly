EXPLAIN : http://{host}/?page=recover

On inspect le formulaire, on voit qu'il y a deux input; un hidden, et un submit.

<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>

Lorsque l’on change l’adresse webmaster@borntosec.com, qui est entré en dur, par n’importe quoi et que l’on submit, on obtient le flag.

AVOID

Ne pas utiliser les donnees de formulaire, meme hidden pour contenir des donnees personnelles. Surtout s'il s'agit de d'envoyer un mail. Toutes les balises, html meme dotees de l'attribut hidden, sont visibles par n'importe quel utilisateur dans l'inspecteur.
