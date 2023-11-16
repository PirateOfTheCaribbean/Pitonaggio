## Never forget
- cyberchef
- crackstation
- dcode.fr




### Sium aggiuntivo
Browser:
- Ispeziona - Tasto Destro 
- Usare il debugger e impostare break sulle diverse variabili
- Controllare i cookie e modificare "User" con "Admin" se utile
- Controllare i cookie per trovare stringhe base64 o md5
- Usare la console del browser per iniettare funzioni/codice malevolo
- Esaminare il codice presente/funzioni per trovare cose utili
- Andare ad indirizzi del browser (es: challenge/debug o challenge/flag)

Wireshark:
- frame contains "<string>" (esaminare i pacchetti e trovare una stringa in base64)
- File->Export Objects->HTTP

Fetch (usando curl):
- curl <address>
- curl --cookie "<cookie_name>=<cookie_value>" <uri>
- curl <url> -X POST --data "<param1>=<val1>&<param2>=<val2>"

SQL injection
Enter 'OR 1=1-- in login form
On the server this will evaluate to SELECT * FROM Users WHERE User = '' OR 1=1--' AND Pass = ''
1=1 evaluates to true, which satisfies the OR statement, and the rest of the query is commented out by the --

### Da fiup
Link utili:
- Solver vari -> https://www.dcode.fr/en
- Substitution Solver -> https://www.guballa.de/substitution-solver - https://www.quipqiup.com/ -
- Crack Hash -> https://crackstation.net/
- Base64 -> https://www.base64decode.org/
- Vigenere -> https://www.guballa.de/vigenere-solver
- Caesar Cipher -> https://www.dcode.fr/caesar-cipher

Altro insieme di strumenti:
- https://project-awesome.org/apsdehal/awesome-ctf

Esami, testi e riferimento FIUP del corso:
- https://github.com/FIUP/Cybersecurity-UNIPD

Per riferimento a molti esercizi:
- https://github.com/augustozanellato/Cybersec2021/

Per riferimento a strumenti utili:
- https://github.com/trincaw/CybersecurityUnipd
- https://github.com/matnut2/CybersecurityToolsUNIPD
