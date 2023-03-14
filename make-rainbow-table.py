#!/usr/bin/env python

'''make-rainbow-table.py: Creates a rainbow table of desired hashes
                          of a wordlist using MD5, SHA224, SHA256,
                          SHA384, SHA512, or all.'''

import argparse
import hashlib
import sqlite3
import datetime


HASH_FUNCTIONS = {
    'md5': hashlib.md5,
    'sha224': hashlib.sha224,
    'sha256': hashlib.sha256,
    'sha384': hashlib.sha384,
    'sha512': hashlib.sha512,
}


def create_rainbow_table(db):
    '''Creates a table \'rainbow\' in database with two fields,
       one for hash, one for word.'''
    try:
        db.execute('CREATE TABLE rainbow (hash VARCHAR(255) \
                            PRIMARY KEY, word VARCHAR(255));')
    except sqlite3.OperationalError:
        print('Table \'rainbow\' already exists!')


def append_to_table(db, word_hashed, word):
    '''Inserts a word and its hash into the \'rainbow\' table of our db.'''
    try:
        db.execute('INSERT INTO rainbow (hash, word) VALUES (?, ?);',
                   (word_hashed, word))
    except sqlite3.IntegrityError:
        print('%s is already in the database as hash %s' % (word, word_hashed))


def hash_word(word, hash_type):
    '''Returns hashed word of specified hash type.'''
    if hash_type == 'all':
        return [hash_word(word, ht) for ht in HASH_FUNCTIONS]
    elif hash_type in HASH_FUNCTIONS:
        hash_func = HASH_FUNCTIONS[hash_type]
        return hash_func(word.encode()).hexdigest()
    else:
        raise ValueError('Invalid hash type specified!')


import argparse

def main():
    parser = argparse.ArgumentParser(description='Create rainbow table of desired hash types.')
    parser.add_argument('-w', '--wordlist', type=str, required=True,
                        help='wordlist file to use for creating rainbow table')
    parser.add_argument('-t', '--hash-type', type=str, default='all',
                        help='hash type to use for creating rainbow table (default: all)')
    parser.add_argument('-d', '--database', type=str, default='rainbow.db',
                        help='database file to store rainbow table (default: rainbow.db)')
    parser.add_argument('-o', '--output-file', type=str, default=None,
                        help='output file to save rainbow table (default: None)')
    args = parser.parse_args()

    # Check if hash type is valid
    if args.hash_type != 'all' and args.hash_type not in HASH_FUNCTIONS:
        print('Invalid hash type specified!')
        exit(1)

    # Connect to database
    conn = sqlite3.connect(args.database)
    c = conn.cursor()

    # Create rainbow table
    create_rainbow_table(c)

    # Open wordlist file and hash each word
    with open(args.wordlist, 'r') as f:
        for word in f:
            word = word.strip()
            word_hashed = hash_word(word, args.hash_type)
            append_to_table(c, word_hashed, word)
            if args.output_file:
                with open(args.output_file, 'a') as out_file:
                    out_file.write(f'{word_hashed}:{word}\n')

    # Commit changes and close database connection
    conn.commit()
    conn.close()



if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print('Execution time: %s' % (end_time - start_time))
