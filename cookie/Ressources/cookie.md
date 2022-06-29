EXPLAIN: 
Dans les cookies on voit un cookie I_am_admin 

Lorsque qu’on décrypte ce md5 (**68934a3e9455fa72420237eb05902327**): false

encrypte true : **b326b5062b2f0e69046810717534cb09**

on set cette nouvelle valeur dans le cookie 

on recharge la page:

**df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3**

AVOID
1. MD5 n’est plus considerer comme un algo de hash secure, preferez des hash avec un sel.
2. Dans les cookies: pas d’informations sensibles. 
    L’utilisation d’un cookie doit avoir des buts limites dans le temps et ne doit pas permettre des privileges admin.
3. Preferez un systeme d'echange de jeton, JWT = json web token.
