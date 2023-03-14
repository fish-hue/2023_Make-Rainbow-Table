# Rainbow-Table-Tools-2023

A collection to gather hashes, generate rainbow tables, and search against them using the tools included in this repository.

## Collecting Hashes

You can utilize thecollector.py to comb URLs for any hashes and save them as a file for later use.

    $ python thehashcollector.py

## Make-Rainbow-Table
A simple rainbow table generator supporting MD5, SHA224, SHA256, SHA384, and SHA512, written in **Python 2.7**.

## Usage

    $ python make-rainbow-table.py [-h] [-o DATABASE] [-w WORDLIST] [-t HASHTYPE]
    
**Arguments:** 

    -h, --help                                                  show this help message and exit
  
    -o DB_NAME, --db=DB_NAME, --database=DB_NAME                Database to fill with hashes. (default='rainbow.db')
                        
    -w WORD_LIST_NAME, --wordlist=WORD_LIST_NAME                Wordlist to read from and hash. (default='linux.words')
                        
    -t md5|sha224|sha256|sha384|sha512|all, --type=HASHTYPE     Type of hash to use. (default='all')


## Examples

By default, the program will create a database called rainbow.db and use its local wordlist 'linux.words.' It will hash each word using all hash-types included in this program.
    
    $ python make-rainbow-table.py

You can specify what you feel necessary, however.
    
    $ python make-rainbow-table.py -o rainbow.db -w linux.words -t all
    
    $ python make-rainbow-table.py -t md5
    
    $ python make-rainbow-table.py -o rbdatabase.db -w mycustom.list -t sha256

If the specified database does not exist, then it will be created for you.


## Search for hashes the Generated Rainbow Table

You can just run this command in the terminal, add chmod +x if you prefer. You will need your table, and your hashes from previous steps.

    $ bash htcheck.sh
    
This is an overly simple script that will search a given database for a given hash, and provide the plaintext output found, if any.
