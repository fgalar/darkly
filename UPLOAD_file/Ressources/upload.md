EXPLAIN: http://{HOST}/?page=upload
- pas de protection lorsque le fichier est trop grand. MAX_FILE_SIZE défini dans un autre input ??? donc ne protège pas upload.
- on voit que note fichier est stocké dans /tmp sur le serveur …
- pas de protection sur le contenu submit : type=”file”, mais n’utilise pas l’attribut accept
    - A priori d’apres le doc [https://developer.mozilla.org/fr/docs/Web/HTML/Element/input/file](https://developer.mozilla.org/fr/docs/Web/HTML/Element/input/file)
    
    ❝ L'attribut `accept`ne permet pas de valider/contrôler le type réel du/des fichier(s) sélectionné(s). Il fournit simplement une indication au navigateur pour aider l'utilisateur à sélectionner les bons fichiers. Toutefois, dans la plupart des cas, l'utilisateur peut toujours choisir une option dans le sélecteur afin de pouvoir choisir un fichier d'un autre type. ❞
    
    On utilise une fonction `validFileType()`afin de vérifier si le fichier est bien du bon type (c'est-à-dire qu'il respecte les extensions d'image indiquées dans l'attribut `accept`
    ). pour vérifier le type mime : `overrideMimeType()`
    

En utilisant [curl](https://curl.se/docs/manpage.html), nous avons besoin de trois éléments:

- l’adresse url ou se trouve le formulaire : http://X.X.X.X/index.php?page=upload
- l’adresse local de notre programme
- le nom de formulaire

curl \ 

-F "uploaded=@$PWD/file.php;type=image/jpg" \

-F "Upload=Upload" 

"http://192.168.1.17/index.php?page=upload" | grep flag
