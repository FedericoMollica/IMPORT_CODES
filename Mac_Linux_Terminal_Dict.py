'''

MAC LINUX TERMINAL DICTIONARY

'''

(base) MacBook-di-Federico:~ Federico$ pwd
#codice per mostrare la folder in cui ci si trova

(base) MacBook-di-Federico:~ Federico$ man
#codice per leggere la documentazione di un comando dal terminale 

(base) MacBook-di-Federico:~ Federico$ cd
#codice per navigare in una cartella della mia directory

(base) MacBook-di-Federico:~ Federico$ cd ..
#codice per tornare una directory indietro

(base) MacBook-di-Federico:~ Federico$ ls
#codice per mostrare direttamente il contenuto di una specifica directory

(base) MacBook-di-Federico:~ Federico$ ls -a
#codice per mostrare anche i file nascosti della mia cartella

(base) MacBook-di-Federico:~ Federico$ ls -l
#codice per mostrare tutte le informazioni dei file nella mia cartella

(base) MacBook-di-Federico:~ Federico$ ls -la
#codice per mostrare tutte le informazioni anche dei file nascosti nella cartella

(base) MacBook-di-Federico:~ Federico$ ls -lah
#codice per mostrare il contenuto di una cartella con tutti i byte

(base) MacBook-di-Federico:~ Federico$ mkdir
#codice per creare una directory  dal terminale 

(base) MacBook-di-Federico:~ Federico$ touch
#codice per creare un file dal terminale

(base) MacBook-di-Federico:~ Federico$ echo -e 'testo da inserire' >> 
#codice per scrivere su un file txt dal terminale

(base) MacBook-di-Federico:~ Federico$ touch test.txt
(base) MacBook-di-Federico:Downloads Federico$ echo -e 'Ciao Amico' >> test.txt
(base) MacBook-di-Federico:~ Federico$ open test.txt
#codici per creare, modificare ed aprire un file test dal terminale

(base) MacBook-di-Federico:~ Federico$ cp
#codice per copiare un file dal terminale

(base) MacBook-di-Federico:~ Federico$ cp -R
#codice per copiare una directory  dal terminale

(base) MacBook-di-Federico:~ Federico$ mv 
#codice per spostare o rinominare file o directory 

(base) MacBook-di-Federico:~ Federico$ rm
#codice per eliminare un file dal terminale

(base) MacBook-di-Federico:~ Federico$ rm -R
#codice per eliminare una directory dal terminale

(base) MacBook-di-Federico:~ Federico$ find . -type d
#codice per trovare tutte le directory nella directory

(base) MacBook-di-Federico:~ Federico$ find . -type d -maxdepth 1
#codice per trovare tutte le directory di primo grado presenti nella mia directory

(base) MacBook-di-Federico:~ Federico$ find . -type f
#codice per trovare tutti i file nella directory

(base) MacBook-di-Federico:~ Federico$ find . -type f -iname 'term*'
#codice per trovare i file con nome contenente 'ter'

(base) MacBook-di-Federico:~ Federico$ find . -type f -iname '*.py'
#codice per trovare i file con nome contenente '.py' quindi le estenzioni

(base) MacBook-di-Federico:~ Federico$ find . -empty
#codice per trovare tutti le directory o i file vuoti

(base) MacBook-di-Federico:~ Federico$ open
(base) MacBook-di-Federico:~ Federico$ open ~/Downloads/terminal2.py
#codice per aprire un file con software predefinito

(base) MacBook-di-Federico:~ Federico$ open -a 'nome app' 
(base) MacBook-di-Federico:~ Federico$ open -a 'Sublime Text' ~/Downloads/terminal2.py
(base) MacBook-di-Federico:~ Federico$ open -a 'VLC' ~/Desktop/MARINO.mov
#codice per aprire con una app specifica uno specifico file presente in una specifica directory

(base) MacBook-di-Federico:~ Federico$ open -t 
#codice per aprire un file con il text editor di default

(base) MacBook-di-Federico:~ Federico$ open -c
#codice per aprire un file con il text editor di default
